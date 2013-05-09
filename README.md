Boilerplate
===========

A Python framework for short, readable, command line programs in Python.

By Sean R. Spillane
-------------------

See file License.txt for the software license.

Introduction
------------

I have been programming Python command line scripts for some time now, and one thing I really hate to do is to type out the argparse options, config.parse options, os.environ options, hook up the logger, and create a --verbose option to set logging levels. Every single program must get this treatment. There is no good reason why I shouldn't be able to use a single facade object to abstract away this nonsense. Nevertheless, I couldn't find what I wanted online. Therefore, I decided to write one myself! Meet *Boilerplate*, this Command LIne (CLI) abstraction library. With this library, you can write your command scripts cleanly and simply, while knowing that you have the full power of argparse options, automatic RC files, and optional environment defaults at your fingertips. Programs are shorter, more tightly coupled and more coherent. Code is split neatly into option set up and main functionality.

While this code is definitely alpha, or even pre-alpha stage, it is good enough that I can use it in my own work, so I decided to put it up for everyone. As time goes by, I will add testing code and better instructions soon!

Bug Reports
-----------

If you spot any bugs, and I'm certain you will, please either report them via GitHub, or fix it and send me a pull request. Thank you!
