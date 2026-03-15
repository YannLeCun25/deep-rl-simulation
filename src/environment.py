import numpy as np

class CustomAIEnv:
    """Standardized environment for Reinforcement Learning training."""
    def __init__(self):
        self.state = np.random.rand(4)

    def reset(self):
        self.state = np.random.rand(4)
        return self.state

    def step(self, action):
        # Mock reward and next state logic
        reward = 1.0 if action == 1 else -0.1
        self.state = np.random.rand(4)
        done = False
        return self.state, reward, done, {}
