#!/usr/bin/env python
'''
Provide basic services for programs, including logging, config files and options.
'''

import argparse
import logging
import sys

class Boilerplate:
  def __init__(self, main_function, description):
    self.main_function = main_function
    self.log = logging.getLogger(sys.argv[0])
    self.parser = argparse.ArgumentParser(description=description)
    self.args = None
    pass

  def parse_args(self):
    self.parser.add_argument('--verbose', '-v', 
      choices=[
        'DEBUG', 'INFO', 'WARNING', 
        'ERROR', 'CRITICAL'], 
        default='WARNING',
        help='Set the logging verbosity level')
    self.args = self.parser.parse_args()
    levels = {
      'DEBUG':logging.DEBUG,
      'INFO':logging.INFO,
      'WARNING':logging.WARNING,
      'ERROR':logging.ERROR,
      'CRITICAL':logging.CRITICAL}
    logging.basicConfig(level=levels[self.args.verbose])
    pass

  def main(self):
    self.parse_args()
    self.log.info('Starting program.')
    result = self.main_function(self, self.args)
    self.log.info('Stopping program.')
    return result

pass

def sample_func(self, args):
  print("This is a sample program, written with boilerplate.")
  self.log.info('You can only see me with --verbose=INFO or higher.')
  return 0

if __name__ == '__main__':
  plate = Boilerplate(sample_func, 'Test program')
  plate.main()
  pass
