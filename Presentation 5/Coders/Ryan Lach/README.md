### Normal Squares, toggleable features 
-   This code creates a series of squares around the all exterior contours of a cell, normal to its outline, that can then be extracted into images
-   second_pass and variable_length can be toggled for additional overlap accuracy and varying lenghts of squares, respectively
-   smarter_squares and sharon_code can also be toggled for alternate square generation and pathc corner creation, respectively
    - smarter_squares aims to deprecate a number of hyperparameters concerned with dense square creation
    - All created polygons are now set to be squares
-   Grid Search functionality optimizes coverage and minimizes blank pixels in patches in a rudimentary fashion

-   This approach has the benefit of automatically adjusting the rotation of the squares over the cell
-   Next steps include vectorizing epithelium width detection and implementing local checks to ensure proper normal alignment into epithelium
