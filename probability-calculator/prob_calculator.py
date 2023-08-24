import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **balls):
    self.balls = balls
    self.contents = []
    for key in balls:
      for i in range(balls[key]):
        self.contents.append(key)
  
  def draw(self, num):
    if num > len(self.contents):
      return self.contents
    
    strs = []
    for i in range(num):
      r = random.randint(0, len(self.contents)-1)
      strs.append(self.contents.pop(r))       
    return strs

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  for n in range(num_experiments):
    c_hat = copy.deepcopy(hat)
    s_draw = c_hat.draw(num_balls_drawn)
    count = 0
    for b in expected_balls:
      if s_draw.count(b) >= expected_balls[b]:
        count +=1
    if count == len(expected_balls):
      m += 1
  return m / num_experiments