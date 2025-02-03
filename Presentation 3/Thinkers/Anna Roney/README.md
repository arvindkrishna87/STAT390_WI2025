# Presentation 2 - Anna's patching code modifications

## Overview

This folder contains two edited versions of Alyssa's patching algorithm: Anna_PatchingOnMask and Anna_PatchingOnMaskDynamic. 

### Anna_PatchingOnMask

This algorithm differs from Alyssa's because it no longer takes images from Prashant's epithelium extraction algorithm as input. Instead, it takes two images, the first one being a png file of the epithelium annotated and exported from Qupath, and the second one being a jpg of the tissue slice. The first block of code is entirely new and combines these two images and creates an output (placed in a location that the user specifies) of an image of the epithelium highlighted in red. We output the image of the epithelium in red instead of its original colored image to avoid any possible issues of white and black pixels in the epithelium being picked up by the patching algorithm.

The second code block is Alyssa's algorithm. The only minor change to the code is that initial_size was changed to 2 in order to accommodates thin epithelia. 

The last block of code creates a histogram showing the distribution of patch dimensions. This data for a single image is not extremely insightful but the code will be used in the future to display the distribution and modality of patch size for our entire dataset. 

### Anna_PatchingOnMaskDynamic

This file differs from Anna_PatchingOnMask because it utilizes a dynamic initial_size initialization written by Kota. 