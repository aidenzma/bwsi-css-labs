import pytest
from labs.lab_1.lab_1d import two_sum

def test():
    assert two_sum([1, 2, 3, 4], 7) == [2, 3]
    assert two_sum([6, 7, 5, 2], 12) == [1, 2]


if __name__ == "__main__":
    pytest.main()