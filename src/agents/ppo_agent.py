import torch
import torch.nn as nn

class PPOAgent(nn.Module):
    """Actor-Critic implementation for Proximal Policy Optimization."""
    def __init__(self, state_dim: int, action_dim: int):
        super().__init__()
        self.actor = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim),
            nn.Softmax(dim=-1)
        )
        self.critic = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )

    def act(self, state):
        return self.actor(state)

    def evaluate(self, state):
        return self.critic(state)
