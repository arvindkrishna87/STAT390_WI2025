# Presentation 3 - Anna's patching code modifications


## Overview


This folder contains the two edited versions of Alyssa's patching algorithm from presentation 2 and a new file called Anna_PatchingNoIteration. Go to the readme from presentation 2 to learn about the other two files.


### Anna_PatchingNoIteration


This algorithm differs from Alyssa's because it no longer iterates patch size. Instead, it calculates the width of the epithelium and draws patches to match that width exactly (or be slightly larger if the user prefers).


The first block of code is entirely the same as in the last presentation, which simply inputs an image of a mask and the tissue slice and returns a red mask with a white stroma and black background. We output the image of the epithelium in red instead of its original colored image to avoid any possible issues of white and black pixels in the epithelium being picked up by any of our algorithms.


The second code block contains parts of Alyssa's algorithm but is mainly new. The major changes are in the function calculate_epithelium_width, which now utilizes the numpy function np.diff to understand where in the image sections of epithelium start and end.


This code still determines orientation of the epithelium slice (horizontal or vertical) globally instead of locally. See Presentation 3/Thinkers/Kota Suzuki/kotap3_patching_code.ipynb for a versio of this code that determines orientation locally.


This code currently takes 1 second to run, which is slightly longer than Alyssa's code. Optimizing this algorithm is a work in progress.
