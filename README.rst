Irwin
=====

Plotting data in the terminal.

Project homepage: https://github.com/eerimoq/irwin

Installation
------------

.. code-block:: python

   $ pip install irwin

Examples
--------

Command line
^^^^^^^^^^^^

The plot subcommand
"""""""""""""""""""

Read all data from given file and plot it. Data points are separated
by any whitespace character.

.. code-block:: text

   $ echo "0,2 1,1 2,0 3,-1 4,1 5,3 6,5 7,7" > data.txt
   $ irwin plot data.txt

.. image:: https://github.com/eerimoq/irwin/raw/master/docs/plot.gif

Give ``-t scatter`` to create a scatter plot.

.. code-block:: text

   $ python3 -c "import math, random, numpy ; \
         x = numpy.linspace(0, 3 * math.pi, 200) ; \
         y = [v + random.random() / 4 for v in numpy.cos(x)] ; \
         print(' '.join([f'{x},{y}' for x, y in zip(x, y)]))" > data.txt
   $ irwin plot -t scatter data.txt

.. image:: https://github.com/eerimoq/irwin/raw/master/docs/scatter.gif

Add more samples by running ``python3 -c "import random ;
print(f'{random.random()},{random.random()}')`` periodically.

.. code-block:: text

   $ irwin plot -t scatter \
         -c "python3 -c \"import random ; print(f'{random.random()},{random.random()}')\"" \
         data.txt

.. image:: https://github.com/eerimoq/irwin/raw/master/docs/scatter-command.gif

The watch subcommand
""""""""""""""""""""

Run ``cat /proc/uptime | awk '{ print \$1 }'`` periodically any plot
its output.

.. code-block:: text

   $ irwin watch "cat /proc/uptime | awk '{ print \$1 }'"

.. image:: https://github.com/eerimoq/irwin/raw/master/docs/uptime.gif

This is how to plot the CPU load on a machine with 4 CPUs.

.. code-block:: text

   $ irwin watch -a delta -y 0 -Y 100 -s -0.25 -o 100 \
         "head -1 /proc/stat | awk '{ print \$5 }'"

.. image:: https://github.com/eerimoq/irwin/raw/master/docs/cpu.gif

Scripting
^^^^^^^^^

Using a canvas
""""""""""""""

Draw on the canvas and render it. Print the rendered canvas.

.. code-block:: python

   import irwin

   canvas = irwin.Canvas(width=40,
                         height=20,
                         x_min=0,
                         x_max=10,
                         y_min=0,
                         y_max=10)

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

The output:

.. code-block:: text

   ⡟⢍⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⡩⢻
   ⡇⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⢸
   ⡇⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⢸
   ⡇⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⢸
   ⡇⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⢸
   ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
   ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
   ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
   ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
   ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
   ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠑⢄⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
   ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
   ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
   ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
   ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
   ⡇⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⢸
   ⡇⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⢸
   ⡇⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⢸
   ⡇⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⢸
   ⣧⣊⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣑⣼

Line plot
"""""""""

Not yet implemented.

.. code-block:: python

   import math
   import numpy
   import irwin

   x = numpy.linspace(0, 2 * math.pi)
   y = numpy.sin(x)

   print(irwin.plot(x, y))

Scatter plot
""""""""""""

Not yet implemented.

.. code-block:: python

   import math
   import random
   import numpy
   import irwin

   x = numpy.linspace(0, 2 * math.pi)
   y = [v + random.random() / 4 for v in numpy.cos(x)]

   print(irwin.scatter(x, y))
