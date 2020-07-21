import irwin

canvas = irwin.Canvas(width=4000,
                      height=2000,
                      x_min=0,
                      y_min=0,
                      x_max=10,
                      y_max=10)

# Draw the canvas edges.
canvas.draw_line(0, 0, 0, 10, irwin.RED)
canvas.draw_line(0, 10, 10, 10, irwin.RED)
canvas.draw_line(10, 10, 10, 0, irwin.RED)
canvas.draw_line(10, 0, 0, 0, irwin.RED)

# Draw a cross.
canvas.draw_line(0, 0, 10, 10, irwin.CYAN)
canvas.draw_line(0, 10, 10, 0, irwin.CYAN)

# Draw four points.
canvas.draw_point(5, 2.5)
canvas.draw_point(5, 7.5)
canvas.draw_point(2.5, 5)
canvas.draw_point(7.5, 5)

canvas.render()
