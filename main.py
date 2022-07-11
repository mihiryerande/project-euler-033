# Problem 33:
#     Digit Cancelling Fractions
#
# Description:
#     The fraction 49/98 is a curious fraction,
#       as an inexperienced mathematician in attempting to simplify it
#       may incorrectly believe that 49/98 = 4/8,
#       which is correct, is obtained by cancelling the 9s.
#
#     We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
#     There are exactly four non-trivial examples of this type of fraction,
#       less than one in value,
#       and containing two digits in the numerator and denominator.
#
#     If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

from fractions import Fraction
from functools import reduce
import operator
from typing import List, Tuple


def is_curious(numerator: int, denominator: int) -> bool:
    """
    Returns True iff the fraction (`numerator`/`denominator`) is 'curious'

    Args:
        numerator   (int): Double-digit natural number
        denominator (int): Double-digit natural number, greater than `numerator`

    Returns:
        (bool): True iff (`numerator`/`denominator`) is 'curious'

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(numerator) == int and 9 < numerator < 100
    assert type(denominator) == int and 10 < denominator < 100
    assert denominator > numerator

    # Find common digit(s)
    num_digits = set(map(int, list(str(numerator))))
    den_digits = set(map(int, list(str(denominator))))
    common_digits = num_digits.intersection(den_digits)

    # Check if removal of this digit keeps fraction the same
    for d in common_digits:
        # Get new fraction by removing common digit
        num_new = list(str(numerator))
        num_new.remove(str(d))
        num_new = int(''.join(num_new))
        den_new = list(str(denominator))
        den_new.remove(str(d))
        den_new = int(''.join(den_new))

        # Check if new fraction equals original
        if num_new * denominator == den_new * numerator:
            return True
    return False


def get_lcd(fractions: List[Tuple[int, int]]) -> int:
    """
    Returns the LCD of the product of `fractions`

    Args:
        (List[Tuple[int, int]]): List of fractions represented as (numerator, denominator)

    Returns:
        (int): LCD of product of `fractions`
    """
    fs = map(lambda t: Fraction(*t), fractions)
    product = reduce(operator.mul, fs)
    print(product)
    return product.denominator


def main():
    """
    Returns a list of the four non-trivial, double-digit, 'curious' fractions,
      as well as the LCD (least-common-denominator) of their product.

    Returns:
        (Tuple[List[Tuple[int, int]], int]):
            Tuple of...
              * List of 4 non-trivial, double-digit, curious fractions
                  * Each represented as Tuple of numerator and denominator
              * LCD of product of those fractions
    """
    digits = [str(d) for d in range(1, 10)]

    # Find all curious fractions
    cfs = set()
    for denominator in range(11, 100):
        # Only need to consider numerators sharing a digit (not 0) with denominator
        numerator_candidates = set()
        for d_den in str(denominator):
            if d_den != '0':
                for d_new in digits:
                    numerator_candidates.add(int(d_den + d_new))
                    numerator_candidates.add(int(d_new + d_den))

        # Only consider numerators less than denominator
        for numerator in numerator_candidates:
            if numerator < denominator and is_curious(numerator, denominator):
                cfs.add((numerator, denominator))

    cfs = list(cfs)
    cfs.sort(key=lambda f: f[::-1])

    # Get LCD of product
    lcd = get_lcd(cfs)
    return cfs, lcd


if __name__ == '__main__':
    curious_fractions, curious_LCD = main()
    print('All non-trivial, double-digit, curious fractions:')
    for cf in curious_fractions:
        print('  {} / {}'.format(*cf))
    print('Least-common-denominator of their product:')
    print('  {}'.format(curious_LCD))
