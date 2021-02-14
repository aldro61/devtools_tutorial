import pytest
import torch

from demo import DummyNet


def test_init():
    """
    Test that the network can be initialized correctly

    """
    # As long as this doesn't fail, the test will pass.
    # Note: This is a pedagogical example, we don't usually test this.
    DummyNet()


def test_forward_input_validation():
    """
    Test that input valiatin works in the forward pass

    """
    m = DummyNet()

    with pytest.raises(ValueError):
        m(torch.ones(10,))


def test_forward_output():
    """
    Test that the forward pass outputs values in [0, 1]

    """
    m = DummyNet()

    for _ in range(100):
        inp = torch.rand(5, 10) * torch.randint(0, 1000, (1,))
        out = m(inp)
        assert (out > 1).sum() == 0
        assert (out < 0).sum() == 0
