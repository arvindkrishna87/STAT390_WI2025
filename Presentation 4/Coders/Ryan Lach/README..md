### Normal Squares, toggleable features 
-   This code creates a series of squares around the all exterior contours of a cell, normal to its outline, that can then be extracted into images
-   second_pass and variable_length can be toggled for additional overlap accuracy and varying lenghts of squares, respectively
    - All created polygons are now set to be squares
-   Grid Search functionality optimizes coverage and minimizes blank pixels in patches in a rudimentary fashion

-   This approach has the benefit of automatically adjusting the rotation of the squares over the cell
-   Next steps include refining the square creation and selection algorithms 
