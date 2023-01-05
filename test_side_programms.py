from side_programms import change_angle


def test_switch_0_N():
    angle = change_angle('N', 0)
    assert angle == 10


def test_switch_0_S():
    angle = change_angle('S', 0)
    assert angle == 350


def test_switch_0_E():
    angle = change_angle('E', 0)
    assert angle == 0


def test_switch_0_W():
    angle = change_angle('W', 0)
    assert angle == 0


def test_switch_90_N():
    angle = change_angle('N', 90)
    assert angle == 90


def test_switch_90_S():
    angle = change_angle('S', 90)
    assert angle == 90


def test_switch_90_E():
    angle = change_angle('E', 90)
    assert angle == 80


def test_switch_90_W():
    angle = change_angle('W', 90)
    assert angle == 100


def test_switch_180_N():
    angle = change_angle('N', 180)
    assert angle == 170


def test_switch_180_S():
    angle = change_angle('S', 180)
    assert angle == 190


def test_switch_180_E():
    angle = change_angle('E', 180)
    assert angle == 180


def test_switch_180_W():
    angle = change_angle('W', 190)
    assert angle == 180


def test_switch_270_N():
    angle = change_angle('N', 270)
    assert angle == 270


def test_switch_270_S():
    angle = change_angle('S', 270)
    assert angle == 270


def test_switch_270_E():
    angle = change_angle('E', 270)
    assert angle == 280


def test_switch_270_W():
    angle = change_angle('W', 270)
    assert angle == 260


def test_switch_10_350():
    angle = change_angle('S', 10)
    angle = change_angle('S', angle)
    assert angle == 350


def test_switch_350_10():
    angle = change_angle('N', 350)
    angle = change_angle('N', angle)
    assert angle == 10
