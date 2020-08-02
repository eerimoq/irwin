import unittest
import math
import numpy

import irwin


class CanvasTest(unittest.TestCase):

    def assertCanvas(self, actual, expected):
        if actual != expected:
            print('Actual:')
            print(actual)
            print('Expected:')
            print(expected)
            self.fail()

    def test_render_empty_canvas(self):
        canvas = irwin.Canvas(15, 10, 0, 1, 0, 1)

        self.assertCanvas(canvas.render(),
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')

    def test_draw_point(self):
        canvas = irwin.Canvas(2, 2, 0, 1, 0, 1)

        canvas.draw_point(0, 0)
        canvas.draw_point(0, 1)
        canvas.draw_point(1, 0)
        canvas.draw_point(1, 1)

        self.assertCanvas(canvas.render(),
                          '⠁⠈\n'
                          '⡀⢀')

    def test_draw_line(self):
        canvas = irwin.Canvas(10, 10, 0, 2, 0, 2)

        canvas.draw_line(0, 0, 1, 1)
        canvas.draw_line(2, 0, 1, 1)

        canvas.draw_line(0.5, 0, 1, 1)
        canvas.draw_line(1.5, 0, 1, 1)

        canvas.draw_line(0, 0, 2, 2)

        canvas.draw_line(0, 0, 0, 2)
        canvas.draw_line(0, 2, 2, 2)
        canvas.draw_line(2, 2, 2, 0)
        canvas.draw_line(2, 0, 0, 0)

        self.assertCanvas(canvas.render(),
                          '⡏⠉⠉⠉⠉⠉⠉⠉⠉⣽\n'
                          '⡇⠀⠀⠀⠀⠀⠀⠀⡜⢸\n'
                          '⡇⠀⠀⠀⠀⠀⠀⡜⠀⢸\n'
                          '⡇⠀⠀⠀⠀⠀⡜⠀⠀⢸\n'
                          '⡇⠀⠀⠀⠀⡜⠀⠀⠀⢸\n'
                          '⡇⠀⠀⠀⣼⡄⠀⠀⠀⢸\n'
                          '⡇⠀⠀⣼⠃⢟⢄⠀⠀⢸\n'
                          '⡇⠀⡜⡜⠀⠘⡌⢆⠀⢸\n'
                          '⡇⡜⢰⠁⠀⠀⢱⠈⢢⢸\n'
                          '⣟⣀⣇⣀⣀⣀⣀⣇⣀⣻')

    def test_draw_line_odd_height(self):
        canvas = irwin.Canvas(10, 9, 0, 2, 0, 2)

        canvas.draw_line(0, 0, 1, 1)
        canvas.draw_line(2, 0, 1, 1)

        canvas.draw_line(0.5, 0, 1, 1)
        canvas.draw_line(1.5, 0, 1, 1)

        canvas.draw_line(0, 0, 2, 2)

        canvas.draw_line(0, 0, 0, 2)
        canvas.draw_line(0, 2, 2, 2)
        canvas.draw_line(2, 2, 2, 0)
        canvas.draw_line(2, 0, 0, 0)

        self.assertCanvas(canvas.render(),
                          '⡏⠉⠉⠉⠉⠉⠉⠉⢉⢿\n'
                          '⡇⠀⠀⠀⠀⠀⠀⢀⠎⢸\n'
                          '⡇⠀⠀⠀⠀⠀⢠⠊⠀⢸\n'
                          '⡇⠀⠀⠀⠀⢠⠃⠀⠀⢸\n'
                          '⡇⠀⠀⠀⣠⠃⠀⠀⠀⢸\n'
                          '⡇⠀⠀⡰⡏⡧⡀⠀⠀⢸\n'
                          '⡇⠀⡰⡹⠀⠸⡑⡄⠀⢸\n'
                          '⡇⡜⢠⠃⠀⠀⢣⠈⢆⢸\n'
                          '⣟⣀⣎⣀⣀⣀⣈⣆⣀⣻')

    def test_draw_line_partly_outside_canvas(self):
        canvas = irwin.Canvas(10, 10, 0, 2, 0, 2)

        canvas.draw_line(-1000000000, -1000000000, 3000000000, 3000000000)

        self.assertCanvas(canvas.render(),
                          '⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎\n'
                          '⠀⠀⠀⠀⠀⠀⠀⢀⠎⠀\n'
                          '⠀⠀⠀⠀⠀⠀⢀⠎⠀⠀\n'
                          '⠀⠀⠀⠀⠀⢀⠎⠀⠀⠀\n'
                          '⠀⠀⠀⠀⢀⠎⠀⠀⠀⠀\n'
                          '⠀⠀⠀⢀⠎⠀⠀⠀⠀⠀\n'
                          '⠀⠀⢀⠎⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀')

    def test_draw_line_partly_outside_canvas_2(self):
        canvas = irwin.Canvas(10, 10, 0, 2, 0, 2)

        canvas.draw_line(-1, -3, 3, 5)

        self.assertCanvas(canvas.render(),
                          '⠀⠀⠀⠀⠀⠀⢀⠇⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⡸⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⢀⠇⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⡸⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀')

    def test_draw_line_partly_outside_canvas_3(self):
        canvas = irwin.Canvas(10, 10, 0, 2, 0, 2)

        canvas.draw_line(-1, 5, 3, -3)

        self.assertCanvas(canvas.render(),
                          '⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀')

    def test_draw_line_partly_outside_canvas_4(self):
        canvas = irwin.Canvas(10, 10, 0, 2, 0, 2)

        canvas.draw_line(-2, 0, -1, 0)

        self.assertCanvas(canvas.render(),
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')

    def test_draw_line_partly_outside_canvas_5(self):
        canvas = irwin.Canvas(10, 10, 0, 2, 0, 2)

        canvas.draw_line(1, 1, 3, -1)

        self.assertCanvas(canvas.render(),
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠘⢄')

    def test_draw_line_length_zero(self):
        canvas = irwin.Canvas(10, 10, 0, 2, 0, 2)

        canvas.draw_line(1, 1, 1, 1)

        self.assertCanvas(canvas.render(),
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')

    def test_draw(self):
        canvas = irwin.Canvas(40, 20, 0, 10, 0, 10)

        # Draw the canvas edges.
        canvas.draw_line(0, 0, 0, 10)
        canvas.draw_line(0, 10, 10, 10)
        canvas.draw_line(10, 10, 10, 0)
        canvas.draw_line(10, 0, 0, 0)

        # Draw a cross.
        canvas.draw_line(0, 0, 10, 10)
        canvas.draw_line(0, 10, 10, 0)

        # Draw four points.
        canvas.draw_point(5, 2.5)
        canvas.draw_point(5, 7.5)
        canvas.draw_point(2.5, 5)
        canvas.draw_point(7.5, 5)

        self.assertCanvas(canvas.render(),
                          '⡟⢍⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⡩⢻\n'
                          '⡇⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⢸\n'
                          '⡇⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⢸\n'
                          '⡇⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⢸\n'
                          '⡇⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⢸\n'
                          '⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸\n'
                          '⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸\n'
                          '⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸\n'
                          '⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸\n'
                          '⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸\n'
                          '⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠑⢄⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸\n'
                          '⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸\n'
                          '⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸\n'
                          '⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸\n'
                          '⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸\n'
                          '⡇⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⢸\n'
                          '⡇⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⢸\n'
                          '⡇⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⢸\n'
                          '⡇⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⢸\n'
                          '⣧⣊⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣑⣼')

    def test_plot(self):
        canvas = irwin.Canvas(40, 20, 0, 2 * math.pi, -1, 1)
        x = numpy.linspace(0, 2 * math.pi)
        y = numpy.sin(x)
        canvas.draw_lines(x, y)

        self.assertCanvas(canvas.render(),
                          '⠀⠀⠀⠀⠀⠀⠀⢀⠔⠒⠒⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⡔⠁⠀⠀⠀⠀⠘⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠈⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢄⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢢⠀⠀⠀⠀⠀⢀⠎⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⣀⣀⣀⠔⠁⠀⠀⠀⠀⠀⠀⠀')
