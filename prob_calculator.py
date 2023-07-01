import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **hats):
        self.contents = []
        for key, val in hats.items():
            for i in range(val):
                self.contents.append(key)
        

    def draw(self, num):
        if len(self.contents) <= num:
            return self.contents
        
        rm_balls = []
        for i in range(num):
            removed = random.sample(self.contents, 1) #can also use choices(), randrange(), randint() giving the same result
            rm_balls += removed
            for j in removed:
                if j in self.contents:
                    self.contents.remove(j)
            
        return rm_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        expected = []
        for p, q in expected_balls.items():
            for color in range(q):
                expected.append(p)
        new_hat = copy.deepcopy(hat)
        sample = new_hat.draw(num_balls_drawn)
        for color in sample:
            if color in expected:
                expected.remove(color)
        if len(expected) == 0:
            count += 1
    return count / num_experiments