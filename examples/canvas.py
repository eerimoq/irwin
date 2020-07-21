import irwin

canvas = irwin.Canvas(40, 20, 0, 0, 10, 10)

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

print(canvas.render())
