#encoding: utf-8

from nose.tools import *
import sys
#sys.path.append('..')
from lib.gravity import calculate_weight

def setup():
    global mercury, imaginary_planet
    mercury = {'planet': 'Mercury', 'radius': 2439700, 'density': 5427}
    imaginary_planet = { 'planet': 'Braygh', 'radius': 2818000, 'density': 4358 }


def test_calculate_weight__takes_a_mass_and_a_dict_of_planetary_information_as_argument():
    assert_raises(TypeError, calculate_weight)
    assert_raises(TypeError, calculate_weight(100))


@with_setup(setup())
def test_calculate_weight_returns_a_string():
    assert_is_instance(split_line(100, mercury), string)


@with_setup(setup())
def test_calculate_weight_returns_a_string_with_the_name_of_the_planet_and_the_calculated_weight():
    assert_equal((75, mercury), 'Mercury: 277.442')
    assert_equal((100, imaginary_planet), 'Braygh: 343.117')