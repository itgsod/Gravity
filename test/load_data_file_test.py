#encoding: utf-8

from nose.tools import assert_equal
from nose.tools import assert_is_instance
from nose.tools import assert_raises

import sys
sys.path.append('..')

from lib.gravity import load_data_file

def test_load_data_file_takes_a_path_as_argument():
    assert_raises(TypeError, load_data_file)


def test_load_data_file_raises_ValueError_with_correct_error_message_if_path_is_empty():
    with assert_raises(ValueError) as e:
        load_data_file('')
    assert_equal(e.exception.message, 'path must not be empty')

#Detta test kan kommenteras bort om man inte vill testa 'Undantagshantering' på C- eller A-nivå
def test_load_data_file_raises_IOError_with_correct_message_if_file_does_not_exist():
    with assert_raises(IOError) as e:
        load_data_file('nonexisting.file')
    assert_equal(e.exception.message, 'file does not exist')

def test_load_data_file_reads_the_file_and_returns_an_array_of_all_rows_():
    assert_equal(load_data_file('test/test.dat'), ["Earth, 6367445, 5515", "Mars, 3386000, 3934", "Pluto, 1173000, 2050"])

