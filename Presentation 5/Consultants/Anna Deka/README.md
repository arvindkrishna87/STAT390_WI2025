# Patching Code Improvement

## Issues Identified/Fixed: 
Smoothing Size Sensitivity:
As discussed in class, the patches in the current patching code are sensitive to the parameter called “smoothing size.” This is currently being used to calculate the tangents based on two points and does not contribute to smoothing, which is why the goal is to generalize the algorithm to remove this ad-hoc parameter. 

Tiny, “Dot-Like” Patches: 
Some of the patches resulting from the original patching code were very small and inconsistent, in that they were placed in areas where larger patches could have been. These tiny patches sometimes appeared in clusters that did not cover much of the epithelium, thus preventing larger patches from being placed there. They were also usually located in areas where the epithelium was narrower/thinner in comparison to the rest of the slice.


## Update Made: 
In the original patching code, the tangent is calculated using the “previous” and “next” indices, and the `smoothing_size` parameter was part of the calculation for these indices. Since `smoothing_size` was originally set to 100, this meant that the tangents were based on points that were farther away. 

- To generalize the algorithm, I changed the tangent calculation to approximate based on immediate neighbors 
instead of skipping points by adding and subtracting `smoothing_size`. 
- I found the previous and next points dynamically by just adding and subtracting 1 instead
- Deleted the `smoothing_size` parameter

By making this change, I noticed that the Total Epithelium Coverage and Score Percentage increased for a majority of the slices, with almost all my slices reaching > 90% epithelium coverage. I did also notice, however, that the Background Pixel Percentage did tend to increase as well, but not by an unreasonable amount and in most cases the total score still increased regardless.

## Update Location:

Within the for loop that computes the tangent vectors at each point along the contours of the binary mask. 


    for contour in contours:

        contour_points = contour.reshape(-1,2)
        num_contour_points = len(contour_points)
        tangents = np.zeros_like(contour_points, dtype = float)

        for i in range(num_contour_points):
        
            prev_idx = (i - 1) % num_contour_points  # (NEW CHANGE)
            next_idx = (i + 1) % num_contour_points  # (NEW CHANGE)
        
            tangent = contour_points[next_idx] - contour_points[prev_idx]
        
            tangent = tangent / (np.linalg.norm(tangent) + 1e-8)
            tangents[i] = tangent            

