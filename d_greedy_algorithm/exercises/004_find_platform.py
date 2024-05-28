"""
Implement a function that returns the minimum number of platforms that are required for the train
so that none of them waits.

Note: A train will wait if the arrival time of one train overlaps with the arrival time of the other.
So, the problem is to find the minimum number of platforms,
so that if the trains have an overlapping arrival time, they do not collide.
"""


def find_platform(arrival, departure):
    """
    Finds the minimum number of platforms required for a railway Station
    :param arrival: A list of arrival Timing
    :param departure: A list of departure Timing
    :return: Minimum number of platforms required for a railway Station
    """

    # Write your code here!
    pass


# Driver code to test above function
if __name__ == '__main__':
    arrival = [900, 940, 950, 1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]

    print(find_platform(arrival, departure))

    arrival = [200, 210, 300, 320, 350, 500]
    departure = [230, 240, 320, 430, 400, 520]

    print(find_platform(arrival, departure))
