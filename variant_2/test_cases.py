import pytest

from variant_2.logger_print import LoggerOutput
from variant_2.test_func import TestFunc

test_func = TestFunc()


@pytest.mark.parametrize('file_path, n, expected_result', [
    pytest.param('resources/file.txt', 3, 'amet,\nconsectetur\nadipiscing elit.', id='Three lines'),
    pytest.param('resources/file1.txt', 3, 'File not found', id='Incorrect file path'),
    pytest.param('resources/file.zip', 3, 'Incorrect file format', id='Unreadable file format'),
    pytest.param('resources/file.txt', 0, '', id='Zero lines'),
    pytest.param('resources/file.txt', 1, 'adipiscing elit.', id='One row'),
    pytest.param('resources/file.txt', 5, 'Lorem ipsum\ndolor sit\namet,\nconsectetur\nadipiscing elit.',
                 id='Read six of 5 lines'),
    pytest.param('resources/file.txt', 'w', 'n should be integer', id='Not integer format'),
    pytest.param('resources/empty_file.txt', 3, '', id='Empty file'),
    pytest.param('resources/special_char.txt', 5, '@#\n$%\n^&\n*(\n!!!', id='Specific symbols')
])
def test_all_cases(file_path, n, expected_result):
    with LoggerOutput() as output:
        test_func.func_for_test(file_path, n)
    assert '\n'.join(output) == expected_result, 'Incorrect text is displayed'
