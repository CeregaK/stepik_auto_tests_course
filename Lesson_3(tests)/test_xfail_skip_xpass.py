import pytest

@pytest.mark.xfail(strict=True, reason="этот тест сделали fall хотя он pass")
def test_succeed():
    assert True


@pytest.mark.xfail(reason="этот тест мы сами уронили")
def test_not_succeed():
    assert False


@pytest.mark.skip(reason="этот тест мы пропустили")
def test_skipped():
    assert False