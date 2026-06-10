from calculator import square

"""
         Name all the test functions like
         test_<function_name>() for using pytest 
"""
def test_positive():
    assert square(2) == 4
    assert square(2.5) == 6.25

def test_negative():
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0


"""
               Call it like
        pytest test_calc_pytest.py
"""