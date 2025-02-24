# Presentation 4 - Kota's patching code modifications
### kotap4_patching_code.ipynb

The motivation for this week's work was combining the Coder's patching algorithm and the Thinker's epithelium width calculation into one. This would fix the iterative issue of the Coder's patching algorithm while still maintaining the tangent logic. By calculating the epithelium width along the normal line perpendicular to the tangent, we can create patches that inherently rotate according to the shape of the outer contour while also measuring the width accordingly. 

The main change I made was altering Ryan's `calculate_square_corners` function into `calculate_patch_corners`. It returns the output as his original code, but instead of running iteratively, it calculates the width of the epithelium using the points (and in turn the pixel values) found along the normal line. 

This allows us to get rid of two parameters that the algorithm used to have: `step` and `square_size`. We no longer need these parameters as we already have the square size calculated and no longer need an iterative process. 
