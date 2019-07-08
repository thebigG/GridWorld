# GridWorld
GridWorld project for AI class.

*Make sure you have python3*

Fire up your favorite terminal/shell and run the script as follows:

$python3 ./GridWorld.py HEURISTIC DIMENSIONS PROBABILITY RUN_THIS_MANY_TIMES

HEURISTIC can be manhattan_distance, chebyshev_distance or euclidean_distance
The script will take 'm' for manhattan_distance; 'c' for chebyshev_distance; and 'e' for euclidean_distance

DIMENSIONS is just a number and the grid generated will be DIMENSIONS X DIMENSIONS

PROBABILITY is a float between 0 and 1. Make sure this number is between 0 and 1 (like 0.1, 0.24, 0.3, etc), otherwise your data WILL BE corrupted, as such your A* search will not execute as expected.
For instance DO NOT input numbers like 10, 20, 90, etc. These should be floats like .10, .20, .90, etc.


RUN_THIS_MANY_TIMES is just a number that tells the script to run A* on the provided Grid (DIM X DIM) that many times.
This number could be 100 or 30000! Go wild! Let it run over night!

P.S. The developers of this algorithm are not responsible for CPU damage.
