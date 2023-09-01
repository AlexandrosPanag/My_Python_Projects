import copy
import random

class Hat:
    def __init__(self, **kvargs):
        self.contents = []
        for key, value in kvargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num):
        removed = []
        if(num > len(self.contents)):
            return self.contents
        for i in range(num):
            removed_el = self.contents.pop(int(random.random() * len(self.contents)))
            removed.append(removed_el)
        return removed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        ex_copy = copy.deepcopy(expected_balls)
        color_get = hat_copy.draw(num_balls_drawn)

        for color in color_get:
            if(color in ex_copy):
                ex_copy[color] -= 1
        
        if(all(value == 0 for value in ex_copy.values())):
            count += 1
    return count / num_experiments
