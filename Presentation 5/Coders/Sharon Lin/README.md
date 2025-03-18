# Presentation 5 - Sharon

## Goal
As neural networks become deeper, their performance improves but at the cost of increased complexity. ResNet addresses this by using skip connections to reduce the number of parameters, resulting in better performance with lower complexity. In this presentation, I train an image classifier with ResNet to classify H&E patches into benign or high-grade CMIL cases.

## Approach
I used ResNet50, which is a version of ResNet with 50 layers. I froze the model weights for the top layers to utilize the existing architecture, and replaced the final layer of the model with two layers for fine-tuning: (1) a fully connected layer to adjust the output dimensions, and (2) a log softmax layer to calculate the probability of each image being classified into benign or high-grade CMIL. I use a cross entropy loss function to train my model and the Adam optimizer which is known for relativeyl fast convergence. The model is trained on patches of four H&E slices, two of which are benign and two of which are high-grade CMIL. I split these patches into train, validation, and test sets to evaluate the goodness of fit of my model.

My approach is based off of this article: https://medium.com/@anglilian/image-classification-with-resnet-pytorch-1e48a4c33905

My model can be found in the "resnet50_sharon.ipynb" file.

## Findings
I find that my model is yielding a test accuracy of 100%. However, I am extremely suspicious of this high performance as my model might be heavily overfitting to the current data, as I am training on only four slices total. Hopefully, this issue of overfitting can be resolved as more slices are used for training, and we can see the true generalizability of this model.

# Presentation 6 - Sharon

## Approach
In this presentation, I refine the resnet50 model I created in Presentation 5 to:

1) Split the patches into training/validation/test sets based on patients (so that all patches belonging to the same patient are in the same dataset, and the trained model is tested on patches of patients that the model has not seen before)
2) Predict accuracy of cases on a patient level to determine how good model works on each patient
3) Incorporate a random oversampling technique and implement to existing model to overcome data imbalance of benign/high-grade CMIL cases

My model without oversampling can be found in the "resnet50_sharon_final.ipynb" file.
My model with oversampling can be found in the "resnet50_sharon_final.ipynb" file.
Keep in mind that these models are now adapted to be run on Google Colab rather than locally (more specific instructions are in the notebooks themselves)

## Findings
I find when testing my model on all patches, splitting data on a patient-level rather than patch-level, that the accuracy of my model significantly decreases compared to that of Presentation 5 due to reduced overfitting. However, my new model struggles to identify benign classes due to data imbalance (there is a larger number of high-grade CMIL classes and much fewer benign patches to train with). I attempt to solve this problem by oversampling the benign patches, but have yet to test this method due to limited computational resources on Google Colab.