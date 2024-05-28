"""
Dutch National Flag Problem

Implement a function that sorts a list of 0s, 1s and 2s.
This is called the Dutch National Flag Problem. Since the number O
can be represented by the blue color, 1 by the white color, and 2 as the red color,
the task is to transform the list input to the Dutch flag.

Try solving this problem **in-place** and in linear time without using any extra space.
"""


def dutch_national_flag(lst):
    """
    A function to solve Dutch National Flag Problem
    :param lst: A list of integers
    :return: A list of solved Dutch National Flag Problem
    """
    BLUE = 0
    WHITE = 1
    RED = 2

    blue, white, red = 0, 0, len(lst) - 1
    # correct order
    # Blue -> White -> Red

    while white <= red:
        if lst[white] == BLUE:
            if lst[blue] != BLUE:
                lst[blue], lst[white] = lst[white], lst[blue]
            white += 1
            blue += 1
        elif lst[white] == WHITE:
            white += 1
        else:
            if lst[red] != RED:
                lst[white], lst[red] = lst[red], lst[white]
            red -= 1

    return lst


# Driver to test above code
if __name__ == '__main__':

    lst = [2, 2, 2, 0, 1, 0]

    print(dutch_national_flag(lst))