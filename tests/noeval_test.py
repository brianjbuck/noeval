import os

import noeval


def build_path(filename):
    return os.path.join(os.path.abspath(os.path.curdir), "tests", filename)


def test_simple():
    """
    Ensure that a simple call to eval() fails with return code 1.
    """
    assert noeval.main([build_path("fixture_01.py")]) == 1


def test_nested():
    """
    Ensure that the RegEx works with eval() nested inside a block.
    """
    assert noeval.main([build_path("fixture_02.py")]) == 1


def test_indented():
    """
    Ensure that the RegEx works with eval() that has indentations after
    the opening paren.
    """
    assert noeval.main([build_path("fixture_03.py")]) == 1


def test_white_space():
    """
    Ensure that the RegEx works with eval() that has white space before
    the opening paren.
    """
    assert noeval.main([build_path("fixture_04.py")]) == 1


def test_ast_eval():
    """
    Ensure that `ast.literal_eval()` doesn't get caught.
    """
    assert noeval.main([build_path("fixture_05.py")]) == 0


def test_regular_module():
    """
    Ensure that a Python module that does not include eval() passes.
    """
    assert noeval.main([build_path("fixture_06.py")]) == 0
