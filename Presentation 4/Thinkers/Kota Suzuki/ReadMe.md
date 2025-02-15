# Presentation 3 - Kota's patching code modifications
### kotap3_patching_code.ipynb

I use Anna's patching codebase as a base, which calculates the width of the epithelium utlizing numpy functions. I improve her base code by adding logic that determines orientation locally instead of globally. 

The logic is very simple: 
* The function `determine_orientation` remains exactly the same 
* Instead of tinkering with the function itself, I apply a local mask around the balanced points of Alyssa's code. By applying a local mask to the point that we are patching, I can then call the `determine_orientation` function on the mask to determine orientation locally. 