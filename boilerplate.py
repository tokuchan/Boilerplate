#!/usr/bin/env python
'''
Provide basic services for programs, including logging, config files and options.
'''

import argparse
import configparser
import logging
import os
import string
import sys

class EnvironmentDefault(argparse.Action):
  """
  (Inspired by code from: http://stackoverflow.com/a/10551190)
  Use this class like so:

    import argparse
    from boilerplate import EnvironmentDefault

    parser=argparse.ArgumentParser()
    parser.add_argument(
        "-u", "--url", action=EnvironmentDefault, environment_variable='URL', 
        help="Specify the URL to process (can also be specified using URL environment variable)")
    args=parser.parse_args()
  """
  def __init__(self, environment_variable, required=True, default=None, **kwargs):
    if environment_variable in os.environ:
      default = os.environ[environment_variable]
      pass
    if required and default:
      required = False
      pass
    super(EnvironmentDefault, self).__init__(default=default, required=required, **kwargs)
    pass
  def __call__(self, parser, namespace, values, option_string=None):
    setattr(namespace, self.destination, values)
    pass
  def sanitize(st):
    return st.translate(str.maketrans('','',''.join(set(string.punctuation) - set('_')))).upper()
    pass
  pass

class Boilerplate:
  """
  Use this class to automatically handle configuration and argument
  processing. Simply define a child class that overrides the main_function.
  To add arguments, simply call Boilerplate.parser.add_argument(), which
  is an argparse parser. To get to config file stuff, look in 
  Boilerplate.config.
  """
  def __init__(self, main_function, description):
    self.main_function = main_function
    self.log = logging.getLogger(sys.argv[0])
    self.parser = argparse.ArgumentParser(description=description)
    self.config = configparser.ConfigParser()
    self.args = None
    self.rcname = '{}rc'.format(sys.argv[0])
    self.envbase = EnvironmentDefault.sanitize(os.path.basename(sys.argv[0]))
    self.log.debug('rcname is: {}'.format(self.rcname))
    pass

  def setup_config(self):
    self.config.read([
      '.'+self.rcname, 
      os.path.expanduser('~/.'+self.rcname)], encoding='utf8')
    pass

  def parse_args(self):
    self.parser.add_argument('--verbose', '-v', 
      default='WARNING',
      action=EnvironmentDefault,
      environment_variable=self.envbase+'_VERBOSE',
      choices=[
        'DEBUG', 'INFO', 'WARNING', 
        'ERROR', 'CRITICAL'], 
      help='Set the logging verbosity level')
    self.args = self.parser.parse_args()
    pass

  def main(self):
    self.setup_config()
    self.parse_args()
    levels = {
      'DEBUG':logging.DEBUG,
      'INFO':logging.INFO,
      'WARNING':logging.WARNING,
      'ERROR':logging.ERROR,
      'CRITICAL':logging.CRITICAL}
    logging.basicConfig(level=levels[self.args.verbose])
    self.log.info('Starting program.')
    result = self.main_function(self, self.args)
    self.log.info('Stopping program.')
    return result

pass

def sample_func(self, args):
  print("This is a sample program, written with boilerplate.")
  self.log.info('You can only see me with --verbose=INFO or higher.')
  self.log.info('Foo is: {}'.format(self.args.foo))
  self.log.info('Config sections are: {}'.format(self.config.sections()))
  return 0

if __name__ == '__main__':
  plate = Boilerplate(sample_func, 'Test program')
  plate.parser.add_argument('--foo', help='Sample option.')
  plate.main()
  pass
