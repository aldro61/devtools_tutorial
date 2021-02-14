import torch
import torch.nn as nn


class DummyNet(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        if len(x.shape) != 2:
            raise ValueError("Shape must be 2 dim.")

        return torch.sigmoid(x)
