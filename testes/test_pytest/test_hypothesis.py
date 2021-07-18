from hypothesis import given, strategies as st


@given(st.integers(min_value=0))
def test_float(integer: int):
    print('Integer:', integer)
    assert isinstance(integer, int)
