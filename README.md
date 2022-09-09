# Countdown to Midnight Lab

## Learning Goals

- Build a `while` loop.

***

## Key Vocab

- **Interpreter**: a program that executes other programs. Python programs
require the Python interpreter to be installed on your computer so that they
can be run.
- **Python Shell**: an interactive interpreter that can be accessed from the
command line.
- **Data Type**: a specific kind of data. The Python interpreter uses these
types to determine which actions can be performed on different data items.
- **Exception**: a type of error that can be predicted and handled without
causing a program to crash.
- **Code Block**: a collection of code that is interpreted together. Python
groups code blocks by indentation level.
- **Function**: a named code block that performs a sequence of actions when it
is called.
- **Scope**: the area in your program where a specific variable can be called.

***

## Review

This lab is going to test your skills in writing while loops. Remember, a
`while` loop will execute your block of code only _while_ your defined condition
evaluates as `True`.

For example, this script:

```py
x = 1
while x < 10:
    print(f'{x} is less than 10.')
    x += 1
```

Will print this:

```console
1 is less than 10.
2 is less than 10.
3 is less than 10.
4 is less than 10.
5 is less than 10.
6 is less than 10.
7 is less than 10.
8 is less than 10.
9 is less than 10.
```

And _return_ `None`.

### f-Strings

Starting a string with `f` tells the Python interpreter that that string is
going to be **f**ormatted with variable values. Passing variable names into an
f-string with curly brackets `{}` _interpolates_ that variable's value into the
string.

### Add-and-Assign (`+=`)

Add-and-assign is a shorthand used to increment the value of a numeric variable.
It is very useful for while loops because it can push you toward your condition
becoming `False`. _(We don't want our loop to run forever!)_

You can also subtract-and-assign (`-=`), multiply-and-assign (`*=`), and
divide-and-assign (`/=`).

***

## Instructions

This is a **test-driven lab**. Run `pipenv install` to create your virtual
environment and `pipenv shell` to enter the virtual environment. Then run
`pytest -x` to run your tests. Use these instructions and `pytest`'s error
messages to complete your work in the `lib/` folder.

Write a function `countdown()` that takes in an integer argument and uses a
while loop to countdown from that integer to 1, outputting `f'{number}
SECOND(S)!'` in each iteration of the loop. The function should `print()` "HAPPY NEW
YEAR!" after the loop finishes:

```console
# => 10 SECOND(S)!
# => 9 SECOND(S)!
# => 8 SECOND(S)!
# => 7 SECOND(S)!
# => 6 SECOND(S)!
# => 5 SECOND(S)!
# => 4 SECOND(S)!
# => 3 SECOND(S)!
# => 2 SECOND(S)!
# => 1 SECOND(S)!
# => HAPPY NEW YEAR!
```

Our Python program executes so quickly that it doesn't actually count down at the
speed of one second per number. Write a second function called
`countdown_with_sleep()` that also takes one integer argument for the countdown
and makes the loop pause for one second each trip around ([hint][sleep]).

***

## Resources

- [Python While Loops - W3schools](https://www.w3schools.com/python/python_while_loops.asp)
- [Python sleep(): How to Add Time Delays to Your Code](https://realpython.com/python-sleep/)

[sleep]: https://realpython.com/python-sleep/
