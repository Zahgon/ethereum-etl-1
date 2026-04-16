# MIT License
#
# Copyright (c) 2018 Evgeny Medvedev, evge.medvedev@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from ethereumetl.utils import pairwise


class GraphOperations(object):
    def __init__(self, graph):
        """x axis on the graph must be integers, y value must increase strictly monotonically with increase of x"""
        self._graph = graph
        self._cached_points = []

    def get_bounds_for_y_coordinate(self, y):
        """given the y coordinate, outputs a pair of x coordinates for closest points that bound the y coordinate.
        Left and right bounds are equal in case given y is equal to one of the points y coordinate"""
        pass

    def _get_bounds_for_y_coordinate_recursive(self, y, start, end):
        pass

    def _get_point(self, x):
        pass

    def _get_first_point(self):
        pass

    def _get_last_point(self):
        pass


def find_best_bounds(y, points):
    pass


def interpolate(point1, point2, y):
    pass


def bound(x, bounds):
    pass


class OutOfBoundsError(Exception):
    pass


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({},{})'.format(self.x, self.y)

    def __repr__(self):
        return 'Point({},{})'.format(self.x, self.y)
