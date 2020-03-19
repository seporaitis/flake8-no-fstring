import sys

import pytest

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version


python_3_6_plus = pytest.mark.skipif(sys.version_info < (3, 6), reason="Python 3.6+")


def test_version(flake8dir):
    result = flake8dir.run_flake8(["--version"])
    version_string = "flake8-no-fstring: " + version("flake8-no-fstring")
    assert version_string in result.out_lines[0]


# NF001


def test_NF001_catch_singlequote(flake8dir):
    flake8dir.make_example_py("f''")
    result = flake8dir.run_flake8()
    assert result.out_lines == ["./example.py:1:1: NF001 No f-strings."]


def test_NF001_catch_doublequote(flake8dir):
    flake8dir.make_example_py('f""')
    result = flake8dir.run_flake8()
    assert result.out_lines == ["./example.py:1:1: NF001 No f-strings."]


def test_NF001_format(flake8dir):
    flake8dir.make_example_py('"{val}".format(1)')
    result = flake8dir.run_flake8()
    assert result.out_lines == []
