"""
PRACTICE Test 1, problem 2 -- SOLUTION.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and SOLUTION by David Mutchler.  September 2015.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem2a()
    test_problem2b()


def test_problem2a():
    """ Tests the   problem2a   function. """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this TEST function.
    #   It TESTS the  problem2a  function defined below.
    #   Include at least **   3   ** tests, of which
    #      ***  at least TWO tests are on ONE window and
    #      ***  at least ONE test is on a DIFFERENT window.
    #
    # Use the same 4-step process as for previous TEST functions.
    #
    # HINT: Consider using the same test cases as suggested by
    #       the pictures in    problem2a_picture.pdf  in this project.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2a   function:')
    print('--------------------------------------------------')
    print('See the windows that pop up.')

    # Window 1:
    window1 = rg.RoseWindow(400, 300, 'Test with a yellow circle')

    # Test 1 (it is on window 1):
    yellow_circle = rg.Circle(rg.Point(150, 150), 80)
    yellow_circle.fill_color = 'yellow'
    problem2a(window1, yellow_circle)

    window1.close_on_mouse_click()

    # Window 2:
    window2 = rg.RoseWindow(500, 300,
                            'Two tests: no-fill circle, then black circle')

    # Test 2 (it is on window 2):
    no_fill_circle = rg.Circle(rg.Point(200, 150), 120)
    problem2a(window2, no_fill_circle)

    # Test 3 (it is also on window 2):
    black_circle = rg.Circle(rg.Point(420, 200), 50)
    black_circle.fill_color = 'black'
    problem2a(window2, black_circle)

    window2.close_on_mouse_click()


def problem2a(window, circle):
    """
    See   problem2a_picture.pdf   in this project for pictures that may
    help you better understand the following specification:

    1. Draws four rg.Circle's on the given rg.RoseWindow, as follows:

        a. The first rg.Circle is the given rg.Circle.

        b. The second rg.Circle is a new rg.Circle whose center
           is the same as the center of the given rg.Circle
           but whose radius is HALF the radius of the given rg.Circle.
           Also, this second rg.Circle has 'red' as its fill color.

        c. The third rg.Circle is a new rg.Circle that:
             -- has the same radius as the second (red) circle
             -- is immediately to the LEFT of, and barely touching,
                the second (red) circle, and
             -- has 'green' as its fill color.

        d. The fourth rg.Circle is a new rg.Circle that:
             -- has the same radius as the second (red) circle
             -- is immediately to the RIGHT of, and barely touching,
                the second (red) circle, and
             -- has 'blue' as its fill color.

    2. Waits for a mouse-click,
         with an appropriate message displayed to prompt the user.

    3. UN-draws all of the rg.Circle's just drawn,
       one at a time with a 1 second pause between each un-draw.

    Note: Drawing the circles in the order listed ensures that
    the new ones are visible on top of the (larger) first one drawn.

    Preconditions:
        :type window: rg.RoseWindow
        :type circle: rg.Circle
      and the circle fits inside the window.
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    # CAUTION:
    #    **  Do NOT attempt to use loops to solve this problem. **
    # It is simpler (at this point of the course) if done WITHOUT loops.
    # ------------------------------------------------------------------
    circle.attach_to(window)

    circle2 = rg.Circle(circle.center, circle.radius / 2)
    circle2.fill_color = 'red'
    circle2.attach_to(window)

    circle3 = rg.Circle(rg.Point(circle2.center.x - (2 * circle2.radius),
                                 circle2.center.y),
                        circle2.radius)
    circle3.fill_color = 'green'
    circle3.attach_to(window)

    circle4 = rg.Circle(rg.Point(circle2.center.x + (2 * circle2.radius),
                                 circle2.center.y),
                        circle2.radius)
    circle4.fill_color = 'blue'
    circle4.attach_to(window)

    window.render()
    window.continue_on_mouse_click()

    circle4.detach_from(window)
    window.render(1)
    circle3.detach_from(window)
    window.render(1)
    circle2.detach_from(window)
    window.render(1)
    circle.detach_from(window)
    window.render()


def test_problem2b():
    """ Tests the   problem2b  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2b   function:')
    print('--------------------------------------------------')
    print('See the windows that pop up.')

    # ------------------------------------------------------------------
    # In the following test, your code should place ** 4 ** dots
    # (i.e., small filled circles) where the user clicks.
    # The 5th click should close the window.
    # ------------------------------------------------------------------
    problem2b(4)  # 4 dots should appear

    # ------------------------------------------------------------------
    # In the following test, your code should place ** 7 ** dots
    # (i.e., small filled circles) where the user clicks.
    # The 8th click should close the window.
    # ------------------------------------------------------------------
    problem2b(7)  # 7 dots should appear


def problem2b(n):
    """
    See   problem2b_SampleRuns.mp4  in this project for a short video
    that may help you better understand the following specification:

    -- Constructs a new rg.RoseWindow and allows the user
         to click the mouse in that window repeatedly.
    -- Each time the user clicks, draws a small filled circle (a "dot")
         whose center is at the location of the mouse click.
    -- After  n  mouse clicks (where n is the given argument)
         and hence  n  dots, the NEXT click causes the window to close.

    Preconditions: The given argument is a non-negative integer.
    """
    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # IMPORTANT:
    #   The   rg.RoseWindow   class has a method
    #   called   get_next_mouse_click   that you will need to call.
    #   Use the DOT trick to learn about it.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(300, 300, 'Problem 2b.')

    for _ in range(n):
        point = window.get_next_mouse_click()
        print(point)
        point.attach_to(window)
        window.render()

    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
