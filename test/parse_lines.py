#encoding: utf-8

from nose.tools import *

import sys
sys.path.append('..')

from lib.gravity import parse_lines


def setup():
    global data
    data = ["Earth, 6367445, 5515", "Mars, 3386000, 3934"]

def test_parse_lines_takes_a_list_as_argument():
    assert_raises(TypeError, parse_lines)

#Detta test kan kommenteras bort om man inte vill testa 'Undantagshantering' på C- eller A-nivå
def test_parse_lines_raises_ValueError_with_correct_error_message_if_list_is_too_short():
    with assert_raises(ValueError) as e:
        parse_lines([])
    assert_equal(e.exception.message, 'can not parse empty list')


@with_setup(setup())
def test_parse_lines_returns_a_dict_with_correct_keys():
    assert_equal(encode_line(example_list).keys(), ['planet', 'radius', 'density'])


@with_setup(setup())
def test_parse_lines_returns_the_list_correctly_encoded_as_a_hash():
    assert_equal(encode_line(data), example_dict, {'planet': 'Earth', 'radius': 6367445, 'density': 5515} , {'planet': 'Mars','radius': 3386000, 'density': 3934} )
