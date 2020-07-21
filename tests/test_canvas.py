import unittest

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
        canvas = irwin.Canvas(15, 10, 0, 0, 1, 1)

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
                          '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n')

    def test_draw_point(self):
        canvas = irwin.Canvas(2, 2, 0, 0, 1, 1)

        canvas.draw_point(0, 0)
        canvas.draw_point(0, 1)
        canvas.draw_point(1, 0)
        canvas.draw_point(1, 1)

        self.assertCanvas(canvas.render(),
                          '⠁⠈\n'
                          '⡀⢀\n')

    def test_draw_line(self):
        canvas = irwin.Canvas(10, 10, 0, 0, 2, 2)

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
                          '⡇⠀⠀⠀⣼⡀⠀⠀⠀⢸\n'
                          '⡇⠀⠀⣼⠃⢗⡄⠀⠀⢸\n'
                          '⡇⠀⡜⡜⠀⠘⡜⢄⠀⢸\n'
                          '⡇⡜⢰⠁⠀⠀⢱⠈⢆⢸\n'
                          '⣟⣀⣇⣀⣀⣀⣀⣇⣀⣻\n')

    def test_draw_line_odd_height(self):
        canvas = irwin.Canvas(10, 9, 0, 0, 2, 2)

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
                          '⡇⠀⠀⡰⡟⣦⠀⠀⠀⢸\n'
                          '⡇⠀⡰⡹⠀⠱⡱⡀⠀⢸\n'
                          '⡇⡜⢠⠃⠀⠀⢣⠘⢄⢸\n'
                          '⣟⣀⣎⣀⣀⣀⣈⣆⣈⣺\n')

    def test_draw_line_partly_outside_canvas(self):
        canvas = irwin.Canvas(10, 10, 0, 0, 2, 2)

        canvas.draw_line(-1, -1, 3, 3)

        self.assertCanvas(canvas.render(),
                          '⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎\n'
                          '⠀⠀⠀⠀⠀⠀⠀⢀⠎⠀\n'
                          '⠀⠀⠀⠀⠀⠀⢀⠎⠀⠀\n'
                          '⠀⠀⠀⠀⠀⢀⠎⠀⠀⠀\n'
                          '⠀⠀⠀⠀⠀⡎⠀⠀⠀⠀\n'
                          '⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀\n'
                          '⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀\n'
                          '⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀\n'
                          '⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀\n'
                          '⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀\n')
