from Cipher_Module.cipher import encrypt, decrypt, read_txt, get_message, get_filepath
from Scripts.run_cipher import run_cipher
import pytest
import mock
import builtins


def test_run_cipher():
    assert callable(run_cipher)


def test_encrypt():
    assert callable(encrypt)
    assert isinstance(encrypt('Hello', 'This project is fun!'), str)

    # test encrypt with simple string as key instead of actual file
    assert encrypt('b', 'c') == "%"
    assert encrypt('Hello', 'This project is fun!') == "FÎ_EÖ"

    # edge case with empty message and file
    assert encrypt("", "") == ""

    # testing if exception is raised if message is larger than key
    with pytest.raises(Exception):
        encrypt("ab", "c")


def test_decrypt():
    assert callable(decrypt)
    assert isinstance(decrypt('Hello', 'This project is fun!'), str)

    # test decrypt with simple string as key instead of actual file
    assert decrypt('%', 'c') == "b"
    assert decrypt('FÎ_EÖ', 'This project is fun!') == "Hello"

    # edge case with empty message and file
    assert decrypt("", "") == ""

    # testing if exception is raised if encrypted message is larger than key
    with pytest.raises(Exception):
        encrypt("ab", "c")


def test_get_message():
    # mocking the get_message() function with a correct input
    with mock.patch.object(builtins, 'input', lambda _: 'Hello'):
        # execute function with "e" flag
        message = get_message("e")
        assert message == 'Hello'

    # mocking the get_message() function with a correct input
    with mock.patch.object(builtins, 'input', lambda _: 'Bye'):
        # execute function with "d" flag
        message = get_message("d")
        assert message == 'Bye'

    # mocking the get_message() function with an empty input
    with mock.patch.object(builtins, 'input', lambda _: ''):
        # execute function with "e" flag and expecting exception
        with pytest.raises(Exception):
            get_message("e")

    # mocking the get_message() function with an empty input
    with mock.patch.object(builtins, 'input', lambda _: ''):
        # execute function with "d" flag and expecting exception
        with pytest.raises(Exception):
            get_message("d")


def test_get_filepath():
    # mocking the get_filepath() function with a correct input
    with mock.patch.object(builtins, 'input', lambda _: './Test.txt'):
        # execute function
        filepath = get_filepath()
        assert filepath == './Test.txt'

    # mocking the get_filepath() function with an empty input
    with mock.patch.object(builtins, 'input', lambda _: ''):
        # execute function and expecting exception
        with pytest.raises(Exception):
            get_filepath()

    # mocking the get_filepath() function with a wrong filetype
    with mock.patch.object(builtins, 'input', lambda _: './Test.pdf'):
        # execute function and expecting exception
        with pytest.raises(Exception):
            get_filepath()


def test_read_txt():
    assert callable(read_txt)
    assert isinstance(read_txt('Test.txt', 4), str)

    # test read_txt with short .txt file
    assert read_txt('Test.txt', 4) == "This"

    # testing if exception is raised if size passed to function is larger than the number of bytes in file
    with pytest.raises(Exception):
        read_txt('Test.txt', 25)
