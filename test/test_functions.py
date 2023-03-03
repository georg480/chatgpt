import pytest

from models.functions import mal, minus, plus, teilen


def test_plus():
    result = plus(3, 1)
    assert result == 4
