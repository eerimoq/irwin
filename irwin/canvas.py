import re


INDEXES_TO_BIT = (
    (1 << 6, 1 << 7),
    (1 << 2, 1 << 5),
    (1 << 1, 1 << 4),
    (1 << 0, 1 << 3)
)

RE_SPLIT = re.compile(r'⠀*([^⠀]+)')


class Canvas:

    def __init__(self, width, height, x_min, x_max, y_min, y_max):
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

        if y0_dot > y1_dot:
            y1_dot -= 1

        x_diff = (x1_dot - x0_dot + 1)
        y_diff = (y1_dot - y0_dot + 1)
        steps = max(abs(x_diff), abs(y_diff))
        x_slope = x_diff / steps
        y_slope = y_diff / steps
        offset = 0

        # Crop for better performance when the line is mostly outside
        # the canvas.
        if x0_dot < 0:
            offset = int(-x0_dot / x_slope)

        if x1_dot > self._x_dots:
            steps -= int((x1_dot - self._x_dots) / x_slope)

        for i in range(offset, steps):
            self._draw_dot(int(x0_dot + x_slope * i), int(y0_dot + y_slope * i))

    def draw_points(self, x, y):
        for xv, yv in zip(x, y):
            self.draw_point(xv, yv)

    def draw_lines(self, x, y):
        if len(x) == 0 or len(y) == 0:
            return

        x0 = x[0]
        y0 = y[0]

        for x1, y1 in zip(x[1:], y[1:]):
            self.draw_line(x0, y0, x1, y1)
            x0 = x1
            y0 = y1

    def draw_rectangle(self, x0, y0, x1, y1):
        self.draw_line(x0, y0, x0, y1)
        self.draw_line(x0, y1, x1, y1)
        self.draw_line(x1, y1, x1, y0)
        self.draw_line(x1, y0, x0, y0)

    def calc_point_row_and_col(self, x, y):
        x_col = self._value_to_dot_x(x) // 2
        y_row = self._value_to_dot_y(y) // 4

        return self._height - y_row - 1, x_col

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
        return '\n'.join(self.render_lines())

    def render_lines(self):
        for row in reversed(self._canvas):
            yield ''.join([chr(0x2800 + value) for value in row])

    def render_segments(self):
        for row, line in enumerate(self.render_lines()):
            for mo in RE_SPLIT.finditer(line):
                yield (row, mo.start(1), mo.group(1))
