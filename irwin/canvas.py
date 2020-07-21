INDEXES_TO_BIT = (
    (1 << 6, 1 << 7),
    (1 << 2, 1 << 5),
    (1 << 1, 1 << 4),
    (1 << 0, 1 << 3)
)


class Canvas:

    def __init__(self, width, height, x_min, y_min, x_max, y_max):
        self._width = width
        self._height = height
        self._x_dots = 2 * width
        self._y_dots = 4 * height
        self._x_min = x_min
        self._y_min = y_min
        self._x_to_dot = (self._x_dots - 1) / (x_max - x_min)
        self._y_to_dot = (self._y_dots - 1) / (y_max - y_min)
        self._canvas = [bytearray(width) for _ in range(height)]

    def draw_point(self, x, y):
        x_dot = self._value_to_dot_x(x)
        y_dot = self._value_to_dot_y(y)
        self._draw_dot(x_dot, y_dot)

    def draw_line(self, x0, y0, x1, y1):
        if x0 > x1:
            x = x0
            x0 = x1
            x1 = x
            y = y0
            y0 = y1
            y1 = y

        x0_dot = self._value_to_dot_x(x0)
        y0_dot = self._value_to_dot_y(y0)
        x1_dot = self._value_to_dot_x(x1)
        y1_dot = self._value_to_dot_y(y1)
        x_diff = (x1_dot - x0_dot + 1)
        y_diff = (y1_dot - y0_dot + 1)
        steps = max(abs(x_diff), abs(y_diff))

        if steps > 0:
            x_slope = x_diff / steps
            y_slope = y_diff / steps

        if y0_dot > y1_dot:
            y0_dot -= 1

        for i in range(steps):
            self._draw_dot(int(x0_dot + x_slope * i), int(y0_dot + y_slope * i))

    def _draw_dot(self, x_dot, y_dot):
        if not 0 <= x_dot < self._x_dots:
            return

        if not 0 <= y_dot < self._y_dots:
            return

        x_col, x_index = divmod(x_dot, 2)
        y_row, y_index = divmod(y_dot, 4)
        self._canvas[y_row][x_col] |= INDEXES_TO_BIT[y_index][x_index]

    def _value_to_dot_x(self, value):
        return int((value - self._x_min) * self._x_to_dot)

    def _value_to_dot_y(self, value):
        return int((value - self._y_min) * self._y_to_dot)

    def render(self):
        lines = []

        for row in self._canvas:
            line = ''.join([chr(0x2800 + value) for value in row])
            lines.insert(0, line)

        lines.append('')

        return '\n'.join(lines)
