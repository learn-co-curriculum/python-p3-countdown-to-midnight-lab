import io
import sys

from countdown import countdown, countdown_with_sleep

class TestCountdown:
    '''Function countdown() in countdown.py'''

    def test_counts_down_prints_happy_new_year(self):
        '''counts down from number and prints "HAPPY NEW YEAR!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        countdown(5)
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "5 SECOND(S)!\n4 SECOND(S)!\n" + \
            "3 SECOND(S)!\n2 SECOND(S)!\n1 SECOND(S)!\nHAPPY NEW YEAR!\n")

class TestCountdownWithSleep:
    '''Function countdown_with_sleep() in countdown.py'''

    def test_counts_down_prints_happy_new_year(self):
        '''counts down from number and prints "HAPPY NEW YEAR!"'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        countdown_with_sleep(5)
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "5 SECOND(S)!\n4 SECOND(S)!\n" + \
            "3 SECOND(S)!\n2 SECOND(S)!\n1 SECOND(S)!\nHAPPY NEW YEAR!\n")
