# Biweekly Update 2

# Tasks Completed
- [x] Watched lecture videos and attended virtual lecture for 9/11 and 9/18
- [x] Completed practice Python exercises on my VM
- [x] Was able to successfuly access PACE ICE cluster
- [x] Completed biweekly literature review
- [x] Peer-reviewed update 1s

*Please reference the rest of the files in this folder of this repository for my completed exercises.

# To- do List
- [x] Watch assigned lecture videos, take notes, and attend lecture on 9/25
- [x] Complete practice exercises
- [x] Find a more chemistry-heavy paper for the literature review
- [x] Become more comfortable with using ASE

# Contribution Description
The Linux and the Python skills that I learned throughout this week will be incredibly applicable to any further research projects,
since I am exploring these capabilities, especially with ASE. These provide the foundational groundwork for future endeavors,
so I will be able to utilize these skills in the future. 

# Literature Review
Paper: Lehtovaara, L., Havu, V., Puska, M. (2009). All-electron density functional theory and time-dependent density functional theory 
with high order finite elements. The Journal of Chemical Physics 131(054103). 

1). Summary: This paper utilizes static and time-density DFT to calculate the all-electron energies for bases made out of finite-elements. 
It creates a method to combine atomic meshes into molecular meshes to have a unified scheme, to represent the core and the valence states as one.
This allows for pseudopotentials to not be necessary, as well as for boundary effects to be avoided.

2). Figure: I found Figure 4 to be the most interesting, because it provides a visual representation for a molecular *and* and an atomic mesh 
for a molecule. Also, this is an example of a refined mesh, so the quality of the elements is ensured. 
![image](https://github.com/user-attachments/assets/8ba7aff4-64eb-4997-8963-afa613e99248)


3). Strongest Point: The paper does a great job of providing example calculations, such as those for the convergence properties for various
molecules. Also, it lists several incredibly useful applications for this newly created method, such as for the time-propagation TDDFT. 

4). Weakest Point: This paper utilizes LDA approximations for DFT calculations, but there have been previous studies that have shown GGA
approximations for similar calculations to be substantially more accurate. The paper doesn't create a visual for the procedure to
create an empty space between atoms in the meshes, so it could improve on that. 

5). Relation: This paper relates to our research project because it develops a scheme for all-electron DFT calculations using the combination
of atomic and molecular meshes and finite-element bases. This allows for relatively accurate determinations of properties for molecules such as
carbon monoxide and benzene. This method could be implemented in further projects if similar calculations are needed, although I believe that the
calculations should be reliant on GGA, rather than LDA. 
