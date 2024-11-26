from ase.build import molecule
from ase.units import Hartree
from sparc import SPARC
import numpy as np

# Create a water molecule and define its simulation box
atoms = molecule('H2O')
atoms.cell = [[8, 0, 0], [0, 8, 0], [0, 0, 8]]
atoms.center()

# Specify calculator settings
calc_settings = {
    'EXCHANGE_CORRELATION': 'GGA_PBE',
    'D3_FLAG': 1,  # Enable Grimme D3 dispersion correction
    'SPIN_TYP': 0,  # Non-spin-polarized calculation
    'KPOINT_GRID': [1, 1, 1],  # Single k-point for molecular calculations
    'ECUT': 500 / Hartree,  # Energy cutoff in Hartree units
    'TOL_SCF': 1e-5,  # Convergence tolerance for SCF
    'RELAX_FLAG': 1,  # Relax atomic positions
    'PRINT_FORCES': 1,  # Print forces on atoms
    'PRINT_RELAXOUT': 1  # Output relaxation details
}

calc = SPARC(atoms=atoms, **calc_settings)

# Attach the calculator to the atomic structure
atoms.calc = calc

# Function to introduce a specific deformation to the atomic structure
def apply_deformation(atoms, mode, magnitude):
    deformed_atoms = atoms.copy()  # Work on a copy of the atoms
    if mode == 'uniaxial':
        deformed_atoms.cell[0, 0] *= (1 + magnitude)  # Stretch along x-axis
    elif mode == 'shear':
        deformed_atoms.cell[0, 1] += magnitude * deformed_atoms.cell[1, 1]  # Shear in the xy-plane
    else:
        raise ValueError(f"Deformation type '{mode}' is not recognized.")
    deformed_atoms.set_calculator(calc)  # Attach the calculator to the deformed structure
    return deformed_atoms

# Function to compute stiffness constants based on energy-strain relationships
def compute_stiffness(atoms, deformation_modes, strain_values):
    energy_results = []
    for mode in deformation_modes:
        energies = []
        for strain in strain_values:
            # Apply deformation and calculate energy
            deformed_atoms = apply_deformation(atoms, mode, strain)
            energies.append(deformed_atoms.get_potential_energy())
        energy_results.append(np.array(energies))

    # Fit quadratic energy-strain curves to derive stiffness coefficients
    stiffness_coeffs = []
    for energy_curve in energy_results:
        fit_params = np.polyfit(strain_values, energy_curve, 2)
        stiffness_coeffs.append(fit_params[0])  # The quadratic term corresponds to stiffness
    return stiffness_coeffs, energy_results

# Define deformation modes and strains to apply
deformation_modes = ['uniaxial', 'shear']
strain_values = np.linspace(-0.02, 0.02, 5)  # Example range of strain magnitudes

# Perform stiffness calculation
stiffness_coefficients, energy_curves = compute_stiffness(atoms, deformation_modes, strain_values)

# Display the computed stiffness constants
print("Elastic stiffness constants (GPa):", stiffness_coefficients)
