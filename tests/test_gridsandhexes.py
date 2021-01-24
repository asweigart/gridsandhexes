from __future__ import division, print_function
import pytest
import gridsandhexes


def test_basic():
    gridsandhexes.grid(filename='deleteme-default.png')
    gridsandhexes.grid(filename='deleteme-default.png', cols=10, rows=10)
    gridsandhexes.grid(filename='deleteme-default.png', cols=10, rows=10, width=1, height=1, unit='in')
    gridsandhexes.grid(filename='deleteme-default.png', cols=10, rows=10, width=1, height=1, unit='cm')
    gridsandhexes.grid(filename='deleteme-default.png', cols=10, rows=10, width=50, height=50, unit='px')

    gridsandhexes.grid(filename='deleteme-default.pdf')
    gridsandhexes.grid(filename='deleteme-default.pdf', cols=10, rows=10)
    gridsandhexes.grid(filename='deleteme-default.pdf', cols=10, rows=10, width=1, height=1, unit='in')
    gridsandhexes.grid(filename='deleteme-default.pdf', cols=10, rows=10, width=1, height=1, unit='cm')
    gridsandhexes.grid(filename='deleteme-default.pdf', cols=10, rows=10, width=50, height=50, unit='px')







if __name__ == "__main__":
    pytest.main()
