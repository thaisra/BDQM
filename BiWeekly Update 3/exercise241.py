from ase.atoms import Atoms 
from ase.visualize import view


import matplotlib.pyplot as plt
from ase.visualize.plot import plot_atoms
from ase.io import read
import ase.io as aio
from ase.constraints import FixAtoms
MOF = aio.read('CaLTA.cif', format = 'cif')
print(MOF)

c = FixAtoms(mask=[atom.symbol == 'Am' for atom in MOF])

fig, axs = plt.subplots(figsize = [5,2])
plot_atoms(MOF, rotation = '10x, 2y, 2z')

view(MOF)

print(f"Number of atoms: {len(MOF)}")
for i, MOF in enumerate(MOF):
    print(f"Atom {i+1}: {MOF.symbol}")
    

#atomic_numbers= MOF.get_atomic_numbers()
#print(atomic_numbers)

MOF.set_pbc((True, True, False))

view(MOF)
