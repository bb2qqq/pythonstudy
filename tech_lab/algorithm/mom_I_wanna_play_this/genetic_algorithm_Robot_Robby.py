# coding: utf-8
"""
QUESTION:

You are in a room made of 10*10 squares(or huger, or more irregular), which rubbish cans are thrown randomly spread these squares.
You are asked to clean the room with Robot Robby.
He got a weak sight, which allows him to saw only 1 adjacent square around him.
Respectively on his forward, behind, left and right.
Your task is to design a program for Robot Robby.
So that put him in any place of the room, he can clean the room effectively.


----------------------------------------------------------------------------------------------------------------------------------------------------------


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
import random
import copy
from matplotlib import pyplot as plt

######################      BASIC TOOLS     #####################

def n_pos_with_m_status(status_list, r, cur_combo=()):
    """ 有r个位置，每个位置有若干种状态,  每个位置的状态集是相同的。
        一个位置编号+该位置状态=该位置属性，
        找出所有不同位置属性的组合
        这是我写的第一个recursion函数，
                                        Tue Jul  7 17:59:34 CST 2015
    """
    r -= 1
    temp_list = []
    for i in status_list:
        if r > 0:
            temp_list = temp_list + n_pos_with_m_status(status_list, r, cur_combo + (i,))
        else:
            temp_list.append(cur_combo + (i,))
    return temp_list


POSITION_LIST = ['North', 'South', 'East', 'West', 'Mid']
POS_STATUS_LIST = ['empty', 'wall', 'can']
ACTION_LIST = ['Go north', 'Go south', 'Go east', 'Go west', 'Pick']
ACTION_COORDINATE_DICT = dict(zip(ACTION_LIST[:4], [(0, 1), (0, -1), (1, 0), (-1, 0)]))
ALL_STATUS_COMBINATION = n_pos_with_m_status(POS_STATUS_LIST, len(POSITION_LIST))



############################    ADVANCE ABSTRACTION     #########################
class Map(object):
    pass

class Robot(object):

    def __init__(self, action_point=100, init_map={}, genome=None, start_position=None):
        """ action_point decides how many actions can a robto do """
        self.action_point = action_point
        self.track = []  # track the movement of robot
        self.score = 0  # calucate the performance of rubbish collection
        self.REWARD = 10  # Reward score for good behaviour
        self.PUNISHMENT = -10  # Punishment for bad behaviour
        self.positive_score = 0  # statistic for how many positive scores the machine get
        self.negative_score = 0  # statistic for how many negative scores the machine get 
        copied_map = copy.deepcopy(init_map)
        self.init_map = copied_map
        self.current_map = self.init_map
        self.calc_map_score(self.init_map)  # Get the maximum & standard map score for current map
        self.genome = genome or self.generate_genome(ALL_STATUS_COMBINATION, ACTION_LIST)
        self.current_position = start_position or random.choice(init_map.keys())

    def calc_map_score(self, target_map):
        """ calculate the max possible score and standard score for given map """
        cans_num = self.init_map.values().count(1)
        ideal_pickups = self.action_point/2
        if ideal_pickups > cans_num:
            self.max_map_score = cans_num * self.REWARD
        else:
            self.max_map_score = ideal_pickups * self.REWARD
        self.standard_map_score =  ideal_pickups * (float(cans_num)/len(self.init_map)) * self.REWARD
        if self.standard_map_score > self.max_map_score:
            self.standard_map_score = self.max_map_score


    def generate_genome(self, condition_list, strategies):
        genome = {}
        for condition in condition_list:
            genome[condition] = random.choice(strategies)
        return genome

    def mating(self, another_robot, tendency=0.5, mutation_rate=0.01, wild=False, random_slice=False):
        """ mate two robots, generate a new genome for its child
            tendency is used to determing how much you want to keep current genome,
            the value is between 0 and 1
            mutation_rate is to make child slight different with their parents
            if wild flag is True, two parent genomes will be mixed randomly.
            if wild flag is False, parents genomes will be sliced into two large piece, then composed together.
            if random slice is True, the slice can start from the middle, otherwise slice starts from head.
        """
        if wild:
            child_genome = {}
            for condition in ALL_STATUS_COMBINATION:
                if random.random() < tendency:
                    action = self.genome[condition]
                else:
                    action = another_robot.genome[condition]
                if random.random() < mutation_rate:  # Gene mutation judgement
                    action = random.choice(ACTION_LIST)
                child_genome[condition] = action

        else:  # composing slice strategy
            self_gnome_items = sorted(self.genome.items(), key=lambda x: x[0])
            mother_gnome_items = sorted(another_robot.genome.items(), key=lambda x: x[0])
            slice_length = int(len(self.genome) * tendency)
            if random_slice:
                selected_index = random.choice(range(0, len(self.genome) - slice_length))
            else:
                selected_index = 0
            
            end_index = selected_index + slice_length
            father_slice = self_gnome_items[selected_index : end_index]
            mother_slice = mother_gnome_items[0 : selected_index] + mother_gnome_items[end_index : ]
            child_slice = father_slice + mother_slice
            child_genome = dict(child_slice)

        if len(child_genome) != len(self.genome):
            print 'Wrong child genome number!'

        return child_genome

    def get_feedback(self):
        """ give robot positive or negative score about his behaviours """
        pass

    def look(self, x, y):
        """ Robot looks 1 sites adjacent to him. """
        map_dict = {0: 'empty', 1: 'can'}
        if x < 0 or y < 0 or self.current_map.get((x,y)) == None:
            status = "wall"
        else:
            status = map_dict[self.current_map[(x,y)]]
        return status

    def get_current_condition(self, current_position=None):
        x, y = current_position or self.current_position
        current_pos_status = self.look(x, y)
        north_status = self.look(x, y+1)
        south_status = self.look(x, y-1)
        east_status = self.look(x+1, y)
        west_status = self.look(x-1, y)
        current_condition = (north_status, south_status, east_status,
            west_status, current_pos_status)

        return current_condition

    def interact(self, current_position, action, target_map):
        """ Robot doing chosen action in chosen map """
        self.action_point -= 1
        x, y = current_position
        if action.startswith('Go'):  # Robot choose to Move
            mod_x, mod_y = ACTION_COORDINATE_DICT[action]  # Convert string action to digital move
            target_x = x + mod_x
            target_y = y + mod_y
            target_status = self.look(target_x, target_y)
            if target_status == 'wall':  # Hit a wall 
                self.score += self.PUNISHMENT  # Punishment for negative behaviour
                self.negative_score += self.PUNISHMENT
            else:  # Walkable
                self.current_position = (target_x, target_y)    
        else:  # Robot choose to Pick
            have_can = self.current_map[current_position]
            if not have_can:  # No can there.
                self.score += self.PUNISHMENT  # Try to pick cans in an empty place is stupid
                self.negative_score += self.PUNISHMENT
            else:  # Picked up a can! Nice!
                self.score += self.REWARD
                self.positive_score += self.REWARD
                self.current_map[current_position] = 0  # Remove can from map

        self.track.append(self.current_position)

    def exploring_map(self):
        """ current code only support 2 dimension exploring 
            The imaginary map looks like:
             ...   ...  ...
            [0,1] [1,1] ...
            [0,0] [0,1] ...
        """
        # when action_point used up, can't explore
        if not self.action_point:
            return

        current_condition = self.get_current_condition()
        chosen_action =  self.genome[current_condition]
        self.interact(self.current_position, chosen_action, self.current_map)

    def start_task(self, limit=0):
        while self.action_point > limit:
            self.exploring_map()

############################       PREPERATION       ############################
"""
FACTORS WHICH INFLUENCES THE EVOLUTION SPEED:
    1. Feedback strategies(how robot been rewarded and punished)
    2. Mating strategy(some strategies did better in passing their advantages to children)
    3. Child gene mutation rate.
    4. Group size.
"""

def generate_map(border_range, can_chance=0.5, dimension = 2, irregular=False):
    """ can_chance is a value between 0 and 1 
        irregular parameter is for future extension of irregular map     
        dimension paramter is for future extension of 3 dimension exploring
    """
    map_dict = {}
    space_dimension_list = n_pos_with_m_status(range(border_range), dimension)
    for coordinate in space_dimension_list:
        if random.random() < can_chance:
            have_can = 1
        else:
            have_can = 0
        map_dict[coordinate] = have_can

    return map_dict


# First generation robot pool
def initialize_group(robot_nums, target_map):
    robot_pool = []
    for i in range(robot_nums):
        agent_instance = Robot(init_map=match_map)
        agent_instance.start_task()
        robot_pool.append(agent_instance) 
    return robot_pool


def breeding(robot_pool, robot_nums, wild=False, random_slice=False):
    """ Choose the top 10 of each generation, mating them to reproduce."""
    ranked_pool = sorted(robot_pool, key=lambda x:x.score, reverse=True)
    # No.1 will get 10 copies in the breeding pool, No.2 get 9 copies, ..., No.10 get 1 copy in the breeding pool.
    winners = ranked_pool[:10]
    best_score = winners[0].score  # best score for last generation
    winners.reverse()
    breeding_pool = []
    robot_pool = []
    for i in winners:
        copy_number = winners.index(i) + 1
        breeding_pool.extend([i] * copy_number)
    for i in range(robot_nums):
        papa, mama = random.sample(breeding_pool, 2)
        child_genome = papa.mating(mama, wild=wild, random_slice=random_slice)
        agent_instance = Robot(init_map=match_map, genome=child_genome)
        agent_instance.start_task()
        robot_pool.append(agent_instance) 
    return robot_pool, best_score


def artificial_select(robot_pool, select_generations, robot_nums, wild=False, random_slice=False):
    """ Doing evolution for given generations with a given group size """
    statistic_record = []
    for i in range(select_generations):
        robot_pool, best_score = breeding(robot_pool, robot_nums, wild=wild, random_slice=random_slice)
        statistic_record.append(best_score)

    ranked_pool = sorted(robot_pool, key=lambda x:x.score, reverse=True)
    winners = ranked_pool[:10]
    for i in [(i.score, i.standard_map_score, i.max_map_score) for i in winners]:
        print i

    return robot_pool, winners, statistic_record


def show_record_plot(statistic_record):
    L = zip(range(len(statistic_record)), statistic_record)
    for x, y in L:
        plt.scatter(x, y)
    plt.show()


robot_nums = 100
select_generations = 1000
match_map = generate_map(10)  # make a 10 * 10 map

robot_pool = initialize_group(robot_nums, match_map)
robot_pool, winners, statistic_record = artificial_select(robot_pool, select_generations, robot_nums, wild=True)

a = winners[0]
