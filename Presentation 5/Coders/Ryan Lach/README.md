### Normal Squares, No Smoothing Size
-   This code creates a series of squares around the all exterior contours of a cell, normal to its outline, that can then be extracted into images
-   The only paramters passed into the function is overlap_threshold


-   This approach has the benefit of automatically adjusting the rotation of the squares over the cell
-   This approach uses gradient calculation and gaussian smoothing for accurate tangents at all contour points
