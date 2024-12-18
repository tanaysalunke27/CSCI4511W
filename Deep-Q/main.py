import os
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for matplotlib
os.environ["SDL_VIDEODRIVER"] = "dummy"  # Prevent pygame GUI conflicts on macOS

import matplotlib.pyplot as plt

from agent import Agent

if(__name__ == "__main__"):
    a = Agent(source_path='model.pth', dest_path='model.pth')
    #a.train(num_episodes=1000)
    a.play(num_episodes=10)
    
    #a.play()
