# Presentation 3 - Sharon

## Goal
Debug current algorithm so that patches cover the entire epithelium width.

## Approach
Create three alternative definitions of "covering epithelium width," which currently does not have a concrete definition, and test all definitions on various tissue slices to examine which definition results in the best patches being made.

## Alternative Definitions of Covering Epithelium Width
1. At least two opposite corners are outside epithelium
2. At least two points on opposite sides of patch are outside epithelium
3. At least two points on any two sides of patch are outside epithelium

## Instructions
Using the "Normal_Squares_Toggleable_sharon" notebook, replace the "calculate_square_corners" function call in "create_dense_squares" function with "calculate_square_corners1", "calculate_square_corners2", or "calculate_square_corners3" to test patches drawn using the respective alternative definitions, and re-run the notebook to get results.

## Findings
It seems that definition 2 yields the most reasonable results from limited testing on five tissue slices. Definition 1 seems like too strict of a definition, resulting in patches larger than necessary to cover the epithelium width, and definition 3 seems like too lenient of a definition, resulting in patches that do not cover the epithelium width. 
