# coding: utf-8
"""
QUESTION:

You are in a room made of 10*10 squares(or huger, or more irregular), which rubbish cans are thrown randomly spread these squares.
You are asked to clean the room with Robot Robby.
He got a weak sight, which allows him to saw only 1 adjacent square around him.
Respectively on his forward, behind, left and right.
Your task is to design a program for Robot Robby.
So that put him in any place of the room, he can clean the room effectively.
"""



"""
ANSWER:
At any given moment, the robot is on a square and have 5 choices: Move front/behind/left/right or stay and try pick a can.
A square may containing 3 status: empty, have a can, wall(out of the box, like when your robot is on 0-0, his west and north side square status is wall).
So, we need to enumerate all the square status combinations. And distribute choices to them.
We got 243 possible status combinations.
And assign actions for this status combinations, you'll got a strategy for your robot.


Then you need to make a reward-punishment rule for your robot.

Get a can, nice! +10 points.
Try pick a can in an empty place, not good, -10 points.
Hit a wall? Whoops, -20 points.
(You know what, I think `reward pick a can correctly` was a strong enough rule to evolve an efficient robot, without any other rules, others just accelerate the process, or maybe not, we can test it.)


OK, now we start to produce a bunch of robots with different strategies.
Let's say we'll produce 100 robots.
And we made 100 genomes with 243 genes.

We put these robots into test, let them do 200 actions, watch their scores.
We pick samples among those best scorers, let them interchange their genes to produce offspring.
And maybe add some small random change in offspring to accelerate the evolution.
Until we got a new generation of 100 robots. 


After 1000 or more evolutions, you can get the final generation robots.
Pick the best of it, let him PK with your "well-designed" program.
Then you know how powerful he is.


Yeah, genetic algorithm is that simple, but monstrously powerful, and it's result is often hard to understand by human beings.
"""


def make_square_combination(square_vectors, status):
    """ 遍历做出一个combination """
    result = []
    for square in square_vectors:

