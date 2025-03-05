I added a minimum patch length value so that the small dots would disappear. I found that it works with any variable however it needs to be at least 5 to get ride of a dot
This may mean that the minimum patch length is actually 5 pixels. But I am not sure. I realized that increasing it to 8 did take out all of the small dots that I have, however one or two remain in all of my samples. 
This may be a mask issue instead of an issue with the code. The ones that remain arnet small dots but dots that are a little bigger and form small squares 
This change can be seen on line 13

The next change is on line 103. 
I created an if statement that skips the current iteration but does not stop the loop completely. This will only skip the invalid patches but not stop the process for the entire counter

Next change is line 129. 
I made sure the patches were an array because it was causing errors before. 
I am extracting the patches from all_patches instead of counter because the counter may not have all valid points

Next change is line 134:
I made sure all patches have four corners just in case they were dots and not super small points
Therefore (4,2) means four corners and both x/y coordinates 
