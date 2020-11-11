import sys
from utils.points import *

try:
    # Trying to read the points from file. This is throw error if file doesn't exist
    points = read_points()
except:
    points = 0  # Set points to 0 if save file doesn't exist


def check_input(inp: str):
    global points
    if inp == 'exit':
        print("Goodbye player!")
        sys.exit(0)
    elif inp == 'show points':
        print(f"Your current point/points is {points}")
    elif inp == 'save':
        save_points(points)
    else:
        points = add_points(points, 1)


def main():
    print("Welcome to PyNaruto\n")
    print(f"Your current chakra point/point's is {points}")
    print("Press enter to get a chakra point. Type 'exit' to exit")
    while True:
        inp = input().lower()
        check_input(inp)


main()
