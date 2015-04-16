# coding: utf-8

import random
import pickle

VALID_INPUTS = ['R', 'S', 'P', 'r', 's', 'p',
                'rock', 'scissors', 'paper',
                'Rock', 'Paper', 'Scissors']
EXIT_COMMANDS = ['exit', 'quit', 'q', 'Q', 'esc', 'ESC']
WINNING_MAP = {'R': 'S', 'S': 'P', 'P': 'R'}
LOSING_MAP = {'S': 'R', 'P': 'S', 'R': 'P'}

player_record = {'win': 0, 'lose': 0, 'draw': 0}


class Robot(object):
    """ R is short for Rock, S is short for Scissors, P is short for paper."""

    def __init__(self):
        self.long_memory = {'R': 0, 'S': 0, 'P': 0}
        self.short_memory = []
        self.SHORT_MEMORY_LIMIT = 20
        self.match_history = {'win': 0, 'lose': 0, 'draw': 0}

    def think(self):
        # Simple thinking based on short_memory
        if self.short_memory:
            predict_user_choice = random.choice(self.short_memory)
            decision = LOSING_MAP[predict_user_choice]
        else:
            decision = random.choice(['R', 'S', 'P'])
        return decision

    def record(self, robot_choice, user_choice):
        result = compare(robot_choice, user_choice)
        self.match_history[result] += 1
        self.short_memory.append(user_choice)
        self.long_memory[user_choice] += 1
        if len(self.short_memory) > self.SHORT_MEMORY_LIMIT:
            del self.short_memory[0]

        self.save()

    def save(self):
        saving_data = pickle.dumps(self)
        save_file = open('robot_cache.py', 'w')
        save_file.write('robot_cache=%r' % saving_data)
        save_file.close()


def fight():
    user_choice = ''

    user_choice = raw_input('Rock, Paper or Scissors?')
    # 如果输入退出命令，则退出比赛界面
    if user_choice in EXIT_COMMANDS:
        return False

    # 无效输入需重新输入，将来需补充提示信息
    while user_choice not in VALID_INPUTS:
        user_choice = raw_input('Rock, Paper or Scissors?')

    user_choice = choice_convert(user_choice)

    robot_choice = robot.think()
    result = compare(user_choice, robot_choice)
    robot.record(robot_choice, user_choice)
    if result == 'win':
        player_record['win'] += 1
    elif result == 'draw':
        player_record['draw'] += 1
    else:
        player_record['lose'] += 1

    print 'Robot gives ' + robot_choice + ', ' + 'you ' + result + '!'
    return True  # 继续下一轮比赛


def choice_convert(choice):
    if choice[0] in ['r', 'R']:
        choice = 'R'
    if choice[0] in ['p', 'P']:
        choice = 'P'
    if choice[0] in ['s', 'S']:
        choice = 'S'
    return choice

def compare(choice1, choice2):
    if choice1 == choice2:
        return 'draw'
    if WINNING_MAP[choice1] == choice2:
        return 'win'
    else:
        return 'lose'

def stats():
    total_match_times = 0
    for result, times in player_record.iteritems():
        print result, times
        total_match_times += times
    if total_match_times:
        win_time = player_record.get('win')
        lose_time = player_record.get('lose')
        win_rate = float(win_time)/total_match_times
        lose_rate = float(lose_time)/total_match_times

def go_battle():
    fight_flag = True
    while fight_flag:
        fight_flag = fight()

def match_machine():
    """ 制定策略，与机器人比赛 """
    pass


if __name__ == '__main__':
    try:
        agent = importlib.import_module('robot_cache')
        robot = pickile.loads(agent.__dict__['robot_cache'])
    except:
        robot = Robot()

go_battle()
