from ase.atoms import Atoms
import matplotlib.pyplot as plt
from ase.visualize.plot import plot_atoms
from ase.visualize import view

from ase.build import molecule, bulk
#from ase.data.pubchem import pubchem_atoms_search

water = molecule('H2O')
print(water)
print(water.positions)
view(water) 

fig, axs = plt.subplots(figsize=[5,2])
plot_atoms(water,rotation='10x,20y,2z')
