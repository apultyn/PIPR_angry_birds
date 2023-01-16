def change_angle(key, current_angle):
    """
    Calculates correct angle after inputed key
    """
    angle = current_angle
    if key == 'E':
        if angle != 0 and angle != 180:
            if angle > 0 and angle < 180:
                angle -= 5
            else:
                angle += 5
    if key == 'N':
        if angle != 90 and angle != 270:
            if angle < 270 and angle > 90:
                angle -= 5
            else:
                angle += 5
    if key == 'W':
        if angle != 180 and angle != 0:
            if angle < 360 and angle > 180:
                angle -= 5
            else:
                angle += 5
    if key == 'S':
        if angle != 270 and angle != 90:
            if angle > 90 and angle < 270:
                angle += 5
            else:
                angle -= 5
    if angle < 0:
        angle += 360
    if angle >= 360:
        angle -= 360
    return angle


class GameObject:
    """
    Class GameObject. Contains atributes:

    :param pos: contains starting position of object
    type pos: tuple

    :param rect: contains players rect from pygame
    type rect: Rect
    """
    def __init__(self, pos=tuple):
        self._pos = pos
        self._rect = None

    def __str__(self):
        return str(self._pos)

    def pos(self):
        return self._pos

    def rect(self):
        return self._rect


def get_list_objects(level):
    """
    Returns objects for level inputed
    """
    if int(level) == 1:
        one = GameObject((1000, 600))
        return [one], []
    if int(level) == 2:
        one = GameObject((1000, 600))
        two = GameObject((1000, 400))
        return [one, two], []
    if int(level) == 3:
        one = GameObject((1000, 600))
        two = GameObject((1000, 200))
        three = GameObject((800, 400))
        return [one, two, three], []
    if int(level) == 4:
        one = GameObject((100, 100))
        two = GameObject((1180, 100))
        three = GameObject((1180, 620))
        return [one, two, three], []
    if int(level) == 5:
        one = GameObject((1000, 600))
        barrier1 = GameObject((500, 545))
        return [one], [barrier1]
    if int(level) == 6:
        one = GameObject((800, 600))
        barrier1 = GameObject((600, 545))
        barrier2 = GameObject((1000, 545))
        return [one], [barrier1, barrier2]
    if int(level) == 7:
        one = GameObject((800, 600))
        two = GameObject((1200, 600))
        barrier1 = GameObject((600, 545))
        barrier2 = GameObject((1000, 545))
        return [one, two], [barrier1, barrier2]
