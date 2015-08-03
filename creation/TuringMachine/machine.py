BLANK_STATE = 0
TAPE = [BLANK_STATE]   # initialize with BLANK_SYMBOL

STATE_TABLE = {
(0, 'a'): {'state': 'b', 'symbol': 1, 'move': 1},
(1, 'a'): {'state': 'a', 'symbol': 1, 'move': -1},
(1, 'b'): {'state': 'a', 'symbol': 1, 'move': -1},
(0, 'b'): {'state': 'HALT', 'symbol': 1, 'move': -1},
}


def turing_go(state_table, current_pos, current_symbol, current_state):
    action_dict = state_table[(current_symbol, current_state)]
    next_state = action_dict['state']               # Change status     
    TAPE[current_pos] = action_dict['symbol']       # Write symbol
    next_pos = current_pos + action_dict['move']    # Move head
    current_pos = move(next_pos)

    return current_pos, current_symbol, current_state

def move(next_pos):
    if next_pos < 0:
        TAPE.insert(0, BLANK_STATE)
        cur_pos = 0
    elif next_pos > len(TAPE) - 1:
        TAPE.insert(-1, BLANK_STATE)
        cur_pos = next_pos
    else:
        cur_pos = next_pos

    return cur_pos

current_pos = 0
current_symbol = BLANK_STATE
current_state = 'a'

while current_state != "HALT":
    print TAPE, current_pos
    current_pos, current_symbol, current_state = turing_go(STATE_TABLE, current_pos, current_symbol, current_state)
