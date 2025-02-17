# Presentation 4 - Modifications to Ryan's Contour_Normal_Toggleable Code


## Overview

This folder contains two edited versions of Ryan's patching algorithm.

### Anna_Contour_Normal_Toggleable

One issue with Ryan's algorithm is that for tissue slices with small unattached epithelium areas, the normal vector is sometimes drawn outward of the cell instead of inward (see patching presentation 4 for examples). This algorithm differs from Ryan's because it calculates each contour's centroid using cv2.moments and makes sure all normal vectors point towards the centroid.

This code still determines the width of each patch iteratively. 

### kotap4_patching_code_moments.ipynb

This is a version of Ryan's code which combines my addition of calculating the moments of each centroid with Kota's addition of calculating the width of the epithelium to make it less iterative.

Optimizing the algorithms in both of these files to run faster is a work in progress.
