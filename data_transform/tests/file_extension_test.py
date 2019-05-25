from ..util.file_extension import remove_extension


def run_file_ext_tests():
    assert remove_extension("hello.csv") == 'hello'
    assert remove_extension("hello.ext") == 'hello'
    assert remove_extension("hello") == 'hello'
