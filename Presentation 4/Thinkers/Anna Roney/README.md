# Presentation 4 - Modifications to Ryan's Contour_Normal_Toggleable Code


## Overview

This folder contains an edited versions of Ryan's patching algorithm.


### Anna_Contour_Normal_Toggleable

One issue with Ryan's algorithm is that for tissue slices with small unattached epithelium areas, the normal vector is sometimes drawn outward of the cell instead of inward (see patching presentation 4 for examples). This algorithm differs from Ryan's because it calculates each contour's centroid using cv2.moments and makes sure all normal vectors point towards the centroid.

This code still determines the width of each patch iteratively. Look in Presentation 4/Thinkers/Kota Suzuki for a version of this code that determines patch width by calclating the epithelium. These two versions of Ryan's code should be combined as the next step.

Optimizing this entire algorithm to run faster is a work in progress.
