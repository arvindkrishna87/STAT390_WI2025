# Presentation 5 - Sharon

## Goal
As neural networks become deeper, their performance improves but at the cost of increased complexity. ResNet addresses this by using skip connections to reduce the number of parameters, resulting in better performance with lower complexity. In this presentation, I train an image classifier with ResNet to classify H&E patches into benign or high-grade CMIL cases.

## Approach
I used ResNet50, which is a version of ResNet with 50 layers. I froze the model weights for the top layers to utilize the existing architecture, and replaced the final layer of the model with two layers for fine-tuning: (1) a fully connected layer to adjust the output dimensions, and (2) a log softmax layer to calculate the probability of each image being classified into benign or high-grade CMIL. I use a cross entropy loss function to train my model and the Adam optimizer which is known for relativeyl fast convergence. The model is trained on patches of four H&E slices, two of which are benign and two of which are high-grade CMIL. I split these patches into train, validation, and test sets to evaluate the goodness of fit of my model.

My approach is based off of this article: https://medium.com/@anglilian/image-classification-with-resnet-pytorch-1e48a4c33905


## Findings
I find that my model is yielding a test accuracy of 100%. However, I am extremely suspicious of this high performance as my model might be heavily overfitting to the current data, as I am training on only four slices total. Hopefully, this issue of overfitting can be resolved as more slices are used for training, and we can see the true generalizability of this model.