import math
class PLayer:
    is_alive = True
    run_speed = 0.6
    position_x = 0
    position_y = 0

    def set_position(self, x, y):
        self.position_x = x
        self.position_y = y
        return self.position_x, self.position_y


class Enemy:
    is_alive = True
    run_speed = 0.6
    position_x = 0
    position_y = 0


class Projectile:
    run_speed = 1.0
    position_x = 0
    position_y = 0


def get_distance(x1, x2, y1, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
