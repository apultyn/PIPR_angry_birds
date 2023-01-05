
def change_angle(key, current_angle):
    angle = current_angle
    if key == 'E':
        if angle != 0 and angle != 180:
            if angle > 0 and angle < 180:
                angle -= 10
            else:
                angle += 10
    if key == 'N':
        if angle != 90 and angle != 270:
            if angle < 270 and angle > 90:
                angle -= 10
            else:
                angle += 10
    if key == 'W':
        if angle != 180 and angle != 0:
            if angle < 360 and angle > 180:
                angle -= 10
            else:
                angle += 10
    if key == 'S':
        if angle != 270 and angle != 90:
            if angle > 90 and angle < 270:
                angle += 10
            else:
                angle -= 10
    if angle < 0:
        angle += 360
    if angle >= 360:
        angle -= 360
    return angle
