# Reddit-History-Eraser
Using Praw and Python this will erase up to 100 billion posts and comments in one run through. Or however many comments or posts the user has. The user can also specify how many comments and/or posts they would like deleted. 

This script relies on only one library, Praw: https://praw.readthedocs.org/en/v2.1.21/ the Python Reddit Api Wrapper. My recommended way of installing any python library is through pip. 

On most Linux machines, you open up a terminal and can just run "sudo apt-get install pip" and then "pip install praw" and then you're all set up. 
On Mac, you open a terminal and type "sudo easy_install pip" and then "pip install praw" and then you're all set up. I recommend pip to easy_install mainly due to easy_install now not being updated and relatively deprecated. 
Windows is a little more tricky but not too tricky. Basically you will download the easy setup pip script from here: https://bootstrap.pypa.io/get-pip.py. Once downloaded you will find the file in command line and run "python get-pip.py" after which it should install pip. Now while you're still in the command line type "pip install praw" and it should install it.

To run the program, simply open up a terminal, go into the directory it's in, and type "python RedEraser.py" or whatever you called the file. It should give you some output. 


This was written in python 2.7 and has not been tested in python 3 but is almost guaranteed not to work. 

This is still a working progress so any pulls, pushes, commits, or any other interested contributors are more than welcome to contribute. 
