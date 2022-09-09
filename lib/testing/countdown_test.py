import io
import sys

from countdown import countdown, countdown_with_sleep

class TestCountdown:
    '''Function countdown() in countdown.py'''

    def test_(self):
        '''prints the argument passed to it.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        parrot("Hello!")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Hello!\n")

    def test_returns_argument(self):
        '''returns the argument passed to it.'''
        assert(parrot("Hello!") == "Hello!")

    def test_prints_squawk_by_default(self):
        '''prints "Squawk!" if no argument is passed.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        parrot()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Squawk!\n")

    def test_returns_squawk_by_default(self):
        '''returns "Squawk!" if no argument is passed.'''
        assert(parrot() == "Squawk!")
