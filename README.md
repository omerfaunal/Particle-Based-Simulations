# Scientific Particle Simulations

This repository contains three main scientific particle simulations, each implemented using Python and C. These simulations focus on molecular and statistical experiments, including Buffon's Needle, Diffusion Simulation, and Molecular Communication Error Handling.

## Table of Contents

1. Buffon's Needle Simulation
2. Diffusion Simulation
3. Molecular Communication Error Handling
4. References

## 1 - Buffon's Needle Simulation

Buffon's Needle problem is a classical probability problem that estimates the value of π. This simulation uses both Python and C to solve the problem using Monte Carlo methods. The simulation generates random positions and angles for a needle to determine the probability of it crossing lines on a floor, helping estimate the value of π.

- **Files and folders**:
  - `optimized C/`: Contains a C implementation with a Makefile for compilation.
  - `python/`: Python implementation of the Buffon's Needle Simulation.
  - `Pictures/`: Contains graphs showing the convergence of estimated π values.
  - `Buffon's Needle Simulation.pdf`: A detailed report on the Buffon’s Needle problem, including an analytic solution, Monte Carlo simulations, and convergence graphs.
  
Key Results:
- The report describes how Monte Carlo simulations can estimate π with increasing accuracy as the number of trials grows. The accuracy improves due to the law of large numbers, as described in the experiments.
- See the document for further details on the analytical solution and Monte Carlo methodology. 

## 2 - Diffusion Simulation

This simulation models molecular communication by simulating how particles diffuse through a 3D space and interact with absorbing surfaces. It analyzes how particles are absorbed and how their movement can be influenced by obstacles like reflecting lines in a 2D environment.

- **Files and folders**:
  - `codes/`: Python files handling the diffusion simulation, including models for particle behavior and helper functions.
  - `images/`: Placeholder for visual results.
  - `Diffusion Simulation.pdf`: A report explaining molecular communication systems, how diffusion works in 3D, and how obstacles affect diffusion in 2D.
  
Key Results:
- The simulation shows that increasing the diffusion coefficient leads to a faster absorption rate. In the 2D case, reflecting surfaces alter particle paths, increasing absorption efficiency.
- The document provides detailed explanations of system models and algorithms, including pseudo-code for both 3D and 2D simulations with reflecting surfaces.

## 3 - Molecular Communication Error Handling

This simulation focuses on error correction mechanisms in molecular communication, a field that explores how molecules can carry information between nanodevices. The report reviews Hamming codes for error correction and proposes an innovative approach using alternating molecules for efficient communication.

- **Files and folders**:
  - `codes/`: Python scripts that simulate molecular communication error handling, including error-correcting techniques.
  - `3 - Molecular Communication Error Handling.pdf`: A detailed report explaining error correction in molecular communication, focusing on energy-efficient coding strategies and proposing a new method using alternating molecules (A and B).

Key Results:
- The simulation demonstrates that alternating molecules for communication can improve performance, even when compared to traditional error-correcting techniques like Hamming codes.
- Energy efficiency is a critical factor, and the report explores how to optimize the communication process for nanonetworks operating under energy constraints.

## 4 - References
1. M. S. Leeson, M. D. Higgins, “Forward error correction for molecular communications,” Nano Comm. Networks, vol. 3, pp. 1610–167, 2012.
2. Satoshi Hiyama, Yuki Moritani, “Molecular communication: Harnessing biochemical materials to engineer biomimetic communication systems,” Research Laboratories, NTT DOCOMO, Inc., NTT DOCOMO R&D Center, Japan.
3. Sheryl L. Howard, Christian Schlegel, and Kris Iniewski, “Error Control Coding in Low-Power Wireless Sensor Networks: When Is ECC Energy-Efficient?” Department of Electrical & Computer Engineering, University of Alberta, Canada.
4. Mark S. Leeson, Matthew D. Higgins, “Forward error correction for molecular communications,” School of Engineering, University of Warwick, Coventry, UK.
5. Yi Lu, Xiayang Wang, Matthew D. Higgins, Adam Noel, Neophytos Neophytou, Mark S. Leeson, “Energy requirements of error correction codes in diffusion-based molecular communication systems.”
6. M. S. Kuran, H. B. Yilmaz, T. Tugcu, and B. Ozerman, “Energy model for communication via diffusion in nanonetworks,” Nano Comm. Networks, vol. 1, no. 2, pp. 86–95, 2010.
7. H. B. Yilmaz, A. C. Heren, T. Tugcu, and C.-B. Chae, “Threedimensional channel characteristics for molecular communications with an absorbing receiver,” IEEE Commun. Lett., vol. 18, no. 6, pp. 929–932, Jun. 2014.
8. H. B. Yilmaz, (2023, October). Particle Based Simulations [Lecture slides]. Faculty of Computer Engineering, Bogazici University.
