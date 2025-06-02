# ITO Layer Thickness Estimation in Solar Cells

This repository contains the code and dataset for our paper "Using Deep Learning Image Regression Approach and Optical Interference Phenomena for Determining the Thickness of ITO Layers of Solar Cells". 

![Simulation Output](simulation/output.gif)

## Project Description

In this project, we propose a novel approach to estimate the thickness of the ITO layer in solar cells in real-time and without any physical contact. This is achieved by leveraging deep learning techniques and optical interference phenomena. We have developed a Convolutional Neural Network (CNN) model that processes microscopic images of solar cells and predicts the ITO layer thickness. 

The model is trained using a combination of Mean Absolute Error (MAE) and Mean Squared Error (MSE) loss functions. The effectiveness of our approach is demonstrated through experimental results, which show accurate estimation of the ITO layer thickness. This integration of computer vision and deep learning techniques provides a valuable tool for non-destructive testing and quality control in the manufacturing of solar cells.

## Results

After training, the loss of the model was reduced to 0.83. The slope of the test value in the scatter plot with the true value of the ellipsometer is approximately equal to 1, indicating the high reliability of the model.

## Dataset and Code

The dataset used for this project and the code for the CNN model are available in this repository. You can use them to replicate our results or to develop your own models for ITO layer thickness estimation.

## Citation

If you find our work useful, please cite our paper:

Fan, X., Wang, B., Khokhar, M. Q., Zahid, M. A., Pham, D. P., & Yi, J. (2023). Real-Time ITO Layer Thickness for Solar Cells Using Deep Learning and Optical Interference Phenomena. Energies, 16(16), 6049. https://doi.org/10.3390/en16166049


