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


import itertools
import warnings

from ethereumetl.misc.retriable_value_error import RetriableValueError


def hex_to_dec(hex_string):
    pass


def to_int_or_none(val):
    pass

def to_float_or_none(val):
    pass

def chunk_string(string, length):
    pass


def to_normalized_address(address):
    pass


def validate_range(range_start_incl, range_end_incl):
    pass


def rpc_response_batch_to_results(response):
    pass


def rpc_response_to_result(response):
    pass


def is_retriable_error(error_code):
    pass


def split_to_batches(start_incl, end_incl, batch_size):
    """start_incl and end_incl are inclusive, the returned batch ranges are also inclusive"""
    pass


def dynamic_batch_iterator(iterable, batch_size_getter):
    pass


def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    pass


def check_classic_provider_uri(chain, provider_uri):
    pass
