from ase.atoms import Atoms # import the Atoms class from ASE

H2 = Atoms(symbols='HH', positions=[(0,0,0), (0,0,0.75)])
print(H2)

H2 = H2 + Atoms('H2', positions = [(2,0,0), (2,0,0.75)])
print(H2)
print(H2.positions)

H2.positions = H2.positions + [0,0,1]
print(H2.positions)

from ase.visualize import view

view(H2) # removing viewer='ngl' makes a pop-up window

import matplotlib.pyplot as plt
from ase.visualize.plot import plot_atoms

fig, axs = plt.subplots(figsize=[5,2])
plot_atoms(H2,rotation='10x,20y,2z')
#plt.savefig('cell_example.svg')

print(H2[0]) #prints the atom at index 0 of list H2
print(H2[0].position) #prints the position of atom at index 0 of list H2
print(H2[0].symbol) #prints the symbol of atom at index 0 of list H2
