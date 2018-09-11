"""
<describe what this module has/does>

Created on Dec 10, 2015.
Written by: mutchler.
"""


def main():
    """ Calls the   TEST   functions in this module. """
    main0()
    main1()
    main2()


def main0():
    x = foo_11(3, 7)
    print(x)

    y = foo_12(3, 7)
    print(y)


def foo_11(a, b):
    print(a * b)


def foo_12(a, b):
    return (a * b)


def main1():
    x = 5
    y = 3
    print('main A', x, y)
    foo_1(x, y)
    print('main B', x, y)


def main2():
    x = 5
    y = 3
    print('main A', x, y)
    foo_2(x, y)
    print('main B', x, y)


def foo_1(a, b):
    print('foo A', a, b)
    a = 77
    b = 88
    print('foo B', a, b)


def foo_2(x, y):
    print('foo A', x, y)
    x = 77
    y = 88
    print('foo B', x, y)

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
