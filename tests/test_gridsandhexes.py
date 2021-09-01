from __future__ import division, print_function
import pytest
import gridsandhexes


def test_basic():
    gridsandhexes.grid(filename='deleteme-default.png')
    gridsandhexes.grid(filename='deleteme-default.png', cols=10, rows=10)
    gridsandhexes.grid(filename='deleteme-default.png', cols=10, rows=10, width=50, height=50)







if __name__ == "__main__":
    pytest.main()
