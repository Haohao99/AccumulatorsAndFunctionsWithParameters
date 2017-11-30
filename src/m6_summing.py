"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Hao Hu.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.
import math

def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_cosines()
    run_test_sum_square_roots()


def run_test_sum_cosines():
    """ Tests the   sum_cosines   function. """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function.
    #   It TESTS the  sum_cosines  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print('--------------------------------------------------')
    print('Testing the   sum_cosines   function:')
    print('--------------------------------------------------')

    #Test 1
    n = 4
    expect = 0.13416
    actual = sum_cosines(n)
    print('expected :',expect)
    print('actual :',actual)

    #Test 2
    n2 =2
    expect2 = 1.5403
    actual2 = sum_cosines(n2)
    print('expected :',expect2)
    print('actual :',actual2)

    #Test 3
    n3 = 3
    expect3 = 1.12415
    actual3 = sum_cosines(n3)
    print('expected :',expect3)
    print('actual :',actual3)

def sum_cosines(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the cosines of the integers
       0, 1, 2, 3, ... n, inclusive, for the given n.
    Side effects:   None.
    Example:
      If n is 3, this function returns
        cos(0) + cos(1) + cos(2) + cos(3)   which is about 0.13416.
    """
    answer = 0
    for k in range(n):
        answer = round(answer + math.cos(k),5)

    return answer
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_cosines  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------


def run_test_sum_square_roots():
    """ Tests the   sum_square_roots   function. """
    # ------------------------------------------------------------------
    # DONE: 4. Implement this function.
    #   It TESTS the  sum_square_roots  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_square_roots   function:')
    print('--------------------------------------------------')

    #Test 1
    n1 = 5
    expect1 = 11.854408
    actual1 = sum_square_roots(n1)
    print('expected :',expect1)
    print('actual :',actual1)

    #Test 2
    n2 = 4
    expect2 = 8.69213
    actual2 = sum_square_roots(n2)
    print('expected :',expect2)
    print('actual :',actual2)

    #Test 3
    n3 = 3
    expect3 = 5.863703
    actual3 = sum_square_roots(n3)
    print('expected :',expect3)
    print('actual :',actual3)


def sum_square_roots(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the square roots of the integers
       2, 4, 6, 8, ... 2n    inclusive, for the given n.
           So if n is 7, the last term of the sum is
           the square root of 14 (not 7).
    Side effects:   None.
    Example:
      If n is 5, this function returns
         sqrt(2) + sqrt(4) + sqrt(6) + sqrt(8) + sqrt(10),
      which is about 11.854408.
    """
    total = 0
    for k in range(n):
        total = total + math.sqrt(2 + k*2)

    return round(total,6)
    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_square_roots  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
