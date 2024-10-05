import copy
import random

class Hat:
    def __init__(self,**args):
        self.contents=[]
        for color,count in args.items():
            self.contents.extend([color]*count)

    def draw(self, num):
        # Check if the number of balls to draw exceeds the number of balls in the hat
        if num >= len(self.contents):
            # Return all balls if more or equal balls are requested than available
            drawn = self.contents[:]
            self.contents.clear()  # Empty the hat
        else:
            # Draw the specified number of balls randomly
            drawn = random.sample(self.contents, num)
            for ball in drawn:
                self.contents.remove(ball)
        
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected = []
    for color, count in expected_balls.items():
        expected.extend([color] * count)
    
    # Count of successful experiments
    successful_experiments = 0
    
    for _ in range(num_experiments):
        # Copy the hat object for each experiment
        hat_copy = copy.deepcopy(hat)
        
        # Draw balls from the hat
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Count the occurrences of each color in the drawn balls
        drawn_counts = {}
        for ball in drawn_balls:
            if ball in drawn_counts:
                drawn_counts[ball] += 1
            else:
                drawn_counts[ball] = 1
        
        # Check if the drawn balls meet the expected counts
        success = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break
        
        # If the experiment is successful, increment the count
        if success:
            successful_experiments += 1
    
    # Calculate and return the probability
    return successful_experiments / num_experiments