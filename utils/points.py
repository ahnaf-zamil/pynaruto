def add_points(points: int, point: int):
    points += point
    print("You got a chakra point")
    return points


def save_points(pnt):
    with open("savedata.data", "w+") as f:
        f.write(str(pnt))
        print("Your game has been saved")


def read_points():
    with open("savedata.data", "r") as f:
        return int(f.read())
