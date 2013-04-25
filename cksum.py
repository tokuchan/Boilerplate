#!/usr/bin/env python

import argparse
import logging
import sys

log = logging.getLogger(sys.argv[0])

def cksum(input_string):
  log.debug('Input string: {}'.format(input_string))
  cap_string = ''.join([str.capitalize(x) for x in input_string])
  log.debug('Capitalized string: {}'.format(cap_string))
  prefix = cap_string[:2]
  log.debug('Prefix string: {}'.format(prefix))
  suffix_string = cap_string[2:]
  log.debug('Suffix string: {}'.format(suffix_string))
  suffix_sum = sum([ord(x)-ord('A') for x in suffix_string])
  log.debug('Suffix sum: {}'.format(suffix_sum))
  return('{}{}'.format(prefix, suffix_sum % 999))

def parse_args():
  parser = argparse.ArgumentParser(description='Compute simple checksum')
  parser.add_argument('input_string', type=str,
    help='The string to compute the checksum for')
  parser.add_argument('--verbose', '-v', 
    choices=[
      'DEBUG', 'INFO', 'WARNING', 
      'ERROR', 'CRITICAL'], 
      default='WARNING',
      help='Set the logging verbosity level')
  args = parser.parse_args()
  levels = {
    'DEBUG':logging.DEBUG,
    'INFO':logging.INFO,
    'WARNING':logging.WARNING,
    'ERROR':logging.ERROR,
    'CRITICAL':logging.CRITICAL}
  logging.basicConfig(level=levels[args.verbose])
  return args
  pass

def main(args):
  log.info('Starting program.')
  print(cksum(args.input_string))
  log.info('Stopping program.')
  pass

if __name__ == '__main__':
  args = parse_args()
  main(args)
  pass
