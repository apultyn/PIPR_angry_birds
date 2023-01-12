def change_angle(key, current_angle):
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
    def __init__(self, pos):
        self._pos = pos
        self._rect = None

    def __str__(self):
        return str(self._pos)

    def pos(self):
        return self._pos

    def rect(self):
        return self._rect


def get_list_enemies(level):
    if int(level) == 1:
        one = GameObject((1000, 500))
        return [one]
    if int(level) == 2:
        one = GameObject((1000, 600))
        two = GameObject((1000, 400))
        return [one, two]
    if int(level) == 3:
        one = GameObject((1000, 500))
        two = GameObject((1000, 300))
        three = GameObject((800, 400))
        return [one, two, three]
    if int(level) == 4:
        one = GameObject((100, 100))
        two = GameObject((1180, 100))
        three = GameObject((1180, 620))
        return [one, two, three]
