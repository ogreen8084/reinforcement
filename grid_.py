import numpy as np 

class Grid:
    def __init__(self, start_state):
        self.row = start_state[0]
        self.col = start_state[1]
        self.state = (self.row, self.col)

        self.change_states = {
            (0, 0): ('U', 'R'),
            (0, 1): ('U', 'L', 'R'),
            (0, 2): ('L', 'R'),
            (0, 3): ('U', 'L'),

            (1, 0): ('U', 'D', 'R'),
            (1, 1): ('D', 'L'),
            #(1, 2): not valid space 
            (1, 3): ('U', 'D'),

            (2, 0): ('U', 'D'),
            #(2, 1): not valid space
            (2, 2): ('U', 'R'),

            (3, 0): ('D', 'R'),
            (3, 1): ('L', 'R'),
            (3, 2): ('D', 'L', 'R'),

        }
        
        self.all_states = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1),
            (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]

        self.rewards = {(3,3): 1, (2,3): -1 }
        self.step_cost = -0.1

        self.invalid_states = {(2, 1): ' X  ', (1, 2): '  X '}

        self.state_vals = self.update_state_vals(vals={}, default=True)

    def move(self, action):
        if action in self.change_states[self.state]:
            if action == 'U':
                self.row += 1
            elif action == 'D':
                self.row -= 1
            elif action == 'L': 
                self.col -= 1
            elif action == 'R':
                self.col += 1
        self.state = (self.row, self.col)
        return self.state

    def state_rewards(self):
        state_rewards = {}
        for state in self.all_states:
            if state in self.rewards.keys():
                state_rewards[state] = self.rewards[state]
            else:
                state_rewards[state] = ' '
        return state_rewards

    def states(self):
        return self.change_states.keys() + self.rewards.keys()

    def game_over(self):
        return self.state not in self.change_states.keys()

    def print_row(self, col_vals):
        row = '|'
        for i,val in enumerate(col_vals):
            if val in self.invalid_states:
                row += ' '*2 + str(self.invalid_states[val]) + ' '*2
            else:
                add_me = str(self.state_vals[val])
                row += '  ' + add_me + ' '*(6- len(add_me))
            row += '|'
        return row
    def update_state_vals(self, vals, default):
        state_vals = {}
        if default:
            for state in self.all_states:
                state_vals[state] = 0
        for state in self.all_states:
            if state in vals:
                state_vals[state] = np.round(np.max(list(vals[state].values())), 2)
        return state_vals

    def print_rewards(self):
        state_rewards = self.state_rewards()
        print('---------------------')
        for row in range(4):
            row_string = '|'
            for col in range(4):
                add_me = str(state_rewards[(row, col)])
                row_string += ' ' + add_me + ' '*(3 - len(add_me)) + '|'
            print(row_string)
            print('---------------------')
        print('\n')

    def print_grid(self):
        print('-------------------------------------')
        for row in range(4):
            col_vals = [a for a in self.all_states if a[0] == row]
            print(self.print_row(col_vals))

            print('-------------------------------------')
        print('\n')

        