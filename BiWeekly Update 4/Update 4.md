# Biweekly Update 4


# Tasks Completed
- [x] Watched lecture videos and attended virtual lecture for 10/16
- [x] Completed biweekly literature review
- [x] Peer-reviewed update 3s
- [x] Watched electronic structure lectures and took notes
- [x] Practice with ChatDFT

*There were no exercises to complete for this biweekly update. 

# To- do List
- [x] Watch assigned lecture videos, take notes, and attend lecture on 10/25
- [x] Start on practice DFT calculations as early as I can!
- [x] Find a more chemistry-heavy paper for the literature review
- [x] Become more comfortable with using ASE

# Contribution Description
This week, I watched the electronic structure lectures to gain a better understanding of DFT as a whole. The papers that I read
for this update reinforced my understanding, and also exposed me to novel approaches in the realm of DFT. 

# Literature Review 1
Paper: Bowler, D. R. (2018). Building bridges: matching density functional theory with experiment. Contemporary Physics, 59(4), 377–390. https://doi.org/10.1080/00107514.2019.1578079

1). Summary: This paper discusses, in a very general and superficial manner, the concepts and theories that are integral to DFT, in order to provide a working background.
It then expands on these ideas to highlight the intersection between DFT and experimental approaches, in order to get a better understanding for both. The author highlights that the process 
of selecting a system or a model based on experimental findings narrows the scopes of the theoretical techniques that need to be used and expands the capabilities of just experimental processes alone.

2). Figure: I found figure 5 most interesting since it highlights the accuracy of DFT and STM images in comparison to the predicted schematics. Both accurately represent the locations
of the four defects in the TiSe2 crystal lattice, highlighting its periodicity. The figure also highlights that the defects can be analyzed in the context of the charge density wave.


![image](https://github.com/user-attachments/assets/81480d62-6b3f-4b5f-9451-a31d0f42e9d6)



3). Strongest Point: One of the strongest points of this paper is the emphasis on the intersection of DFT and experimental techniques, especially when analyzing complex materials, since the analysis
of this allows for a more comprehensive understanding of both aspects. The paper supports this using specific examples, such as the study of bismuth nanolines on Si(001) surfaces and the investigation
of TiSe2 and its charge density wave. 

4). Weakest Point: One of the weakest points of this paper is its reliance on specific examples to support its perspectives about the usefulness of examining this intersection, but it does not provide
any generalized or overarching ideas, which could be applied to various contexts. Also, the paper could've had a more detailed discussion about the pitfalls and limitations of using DFT as a modeling tool,
since it mentions the dangers of using it as a "black box," but it never expands on this. 

5). Relation: This paper relates to our research project because it employs the same theory that our group does, but for a different applications; this could be useful in promoting inter-disciplinary
collaboration in order to discover new useful applications for DFT. People from different fields could utilize the research from our group and apply it to theirs to gain a better understanding of the 
experimental data that they get, and possibly change their methods to account for DFT data. 


# Literature Review 2
Paper: Fabian MD, Shpiro B, Rabani E, Neuhauser D, Baer R. Stochastic density functional theory. WIREs Comput Mol Sci. 2019; 9:e1412. https://doi.org/10.1002/wcms.1412

1). Summary: This paper introduces an alternative approach to DFT calculation for large-atom systems (many electron), namely stochastic DFT, which randomly samples electron densities to derive the representational
electronic properties applicable to the entire system, substantially decreasing the computational burden by simplifying calculations. The paper then explores the applications of sDFT to study protein-ligand interactions, localized catalytic events, and the effects of impurities on crystals, as well as other applications in material systems. 

2). Figure: I found figure 1 most interesting since it highlights the increasing accuracy of sDFT as the number of random vectors (I) increases. This means that there exists a convergence to deterministic results
with sDFT, which entails that is a very viable method for approximation in many-electron systems. Also, the decreasing error bars show that the standard deviation for this method across expected and measured
results decreases, so it is a reliable method. All of this entails that this is a very computationally efficient method!

![image](https://github.com/user-attachments/assets/d9a767b1-7983-4136-a4db-de6a84e303bd)





3). Strongest Point: One of the strongest points of this paper is its demonstration of sDFTs ability to achieve linear scaling in computational complexity while maintaining accuracy with its calculations. The
entire paper highlights the efficiency for large systems, sDFTs robustness against system size, a comparison of results with those of deterministic DFT, and analytical insights into this method. 

4). Weakest Point: One of the weakest points of this paper is its over-reliance of the stochastic nature of this method, which introduces inherent statistical fluctuations, especially in systems where small 
energy differences are critical. Also, the results of sDFT are consistently higher than exact, known, values. Also, sDFT is not very applicable in systems with strong correlation coefficients. Although
it is expected that such methods are not perfect, the paper does very little to actually address these concerns, nor does it offer viable solutions. 

5). Relation: This paper relates to our research project because it employs the same theory that our group does, but with a different method for approximations used in calculations. Our group could utilize sDFT
if we were to work with many-electron system or more complex/larger material systems, and we could also work on improving its accuracy by decreasing the stochastic fluctuations. This paper also discusses DFT
fragmentation methods, which is something our group could also implement in our own research. 
