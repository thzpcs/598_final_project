# 3d-star-lite

This program implements the D*-lite algorithm in a 3-Dimensional space, utilizing randomly generated dynamic obstacles, allowing the agent to dynamically navigate around obstacles to the end goal in 3D space.

This project is based on original code from mdeyo (https://github.com/mdeyo/d-star-lite) on github, which was based on the original [D* Lite paper](http://idm-lab.org/bib/abstracts/papers/aaai02b.pdf) by Sven Koenig and Maxim Likhachev.

The D* Lite algorithm was written to be a "novel fast replanning method for robot navigation in unknown terrain". It searches "from the goal vertex towards the current vertex of the robot, uses heuristics to focus the search" and 
efficiently uses the priortity queue to minimize reordering.

Written by Skyler Morris (https://github.com/thzpcs/), Stephan Goertzen (https://github.com/szg2633). and Andrew Connors

### Requirements
This project requires Python 3.6, and the only dependency is Numpy (https://www.scipy.org/scipylib/download.html).

### Running

To run the program, simply download or clone the repository from Github, and place them in your preferred directory. Simply run the main.py file, and enter in your specific environment requirements.

