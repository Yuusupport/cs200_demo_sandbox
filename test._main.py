import main
import pytest

def test_foo():
    assert main_foo(0, 0) == pytest.approx(1)
    assert main_foo(1,0) == 1
    assert main_foo(0,1) == 1