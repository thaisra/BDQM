# Biweekly Update 5


# Tasks Completed
- [x] Watched lecture videos and attended virtual lecture for 10/23 and 10/30
- [x] Attempted to completed practice DFT on my VM
- [x] Was able to successfuly download SPARC
- [x] Completed biweekly literature review
- [x] Peer-reviewed update 4s
- [x] Practice with ChatDFT

*Please reference the rest of the files in this folder of this repository for my completed exercises.

# To- do List
- [x] Watch assigned lecture videos, take notes, and attend lecture on 11/6
- [x] Rerun DFT calculations on ICE cluster effectively
- [x] Run stand-alone script provided by Sayan from SLACK
- [x] Complete practice exercises
- [x] Rewatch DFT theoretical videos
- [x] Find a more chemistry-heavy paper for the literature review
- [x] Start on calculations project *early*

# Contribution Description
In this week, I ran practice DFT calculations which is exactly what real research in this field is based on, but on a much higher level.
This gave me an opportunity to practice with different functionals and also a better understanding of SPARC and ICE. 

# Literature Review
Paper: Wan, Z., Wang, Q-D., Liu, D., Liang, J. (2021). Effectively improving the accuracy of PBE functional in calculating the solid bang gap via 
Machine Learning. Computational Materials Science. 198 (110699).

1). Summary: This paper develops a band-gap correction model to accurately determine band gap energies for insulators and semiconductors using the PBE 
functional supplemented with machine learning, since conventional LDA and GGA consistently underestimate it. 

2). Figure: Figure 1 is my most favorite, illustrating correlation coefficient matrix diagrams. It indicates the Pearson relation coefficients for the 
initial 7 descriptors used in this study, showing linear relationships between pairs of descriptors, to determine which ones to use in the ML model.
I really liked how this figure visualizes which descriptors to eliminate for the model based on their correlation values, as someone not too
familiar with ML. 



![image](https://github.com/user-attachments/assets/2635f024-ca6b-4a2a-a0df-d90559817716)




3). Strongest Point: One of the strongest points of this paper its novel use of ML, specifically ANN, to improve DFT calculation accuracy. This approach
allows for the decrease in the underestimation of band gap energies produced by conventional DFT methods, corrects accuracy, and has vast applications
to the field of materials science. 

4). Weakest Point: The weakest part of this paper and/or the model it proposes is its overreliance on the quality and representativeness on the dataset
used for training the ANN. The dataset was only 150 materials, which could be not representative, and there is an overfitting risk. Also, it is very
computationally expensive to train the ANN, despite the paper saying that the computational cost for this model is substantially lower than that of G0W0. 


5). Relation: This paper relates to our research project because it strives to improve on DFT accuracy from various functionals, but it offers a novel approach
to increase accuracy and precision using ML and trained neural networks to develop corrected models. Such an approach could be adopted by our group in order to
have more accurate computations with lower computational costs (after the model is properly trained). 

