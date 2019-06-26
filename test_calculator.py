
import pytest
from calculator import do_calculation


def test_calculator_simple():
    result = do_calculation(1, 10, '')
    assert result == 10.0


@pytest.mark.parametrize('units,price,expected', [
    (1, 100, 106.85),
    (33, 1234.56, 38958.084),
])
def test_calculator_with_taxes(units, price, expected):
    result = do_calculation(units, price, 'UT')
    assert result == expected


def test_calculator_with_taxes_wrong_state():
    result = do_calculation(1, 100, 'TT')
    assert result == 100


def test_calculator_with_discount_and_taxes():
    result = do_calculation(1, 1500, 'UT')
    assert result == 1554.6675
