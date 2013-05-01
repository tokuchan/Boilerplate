#!/usr/bin/env python

import boilerplate
import logging
import re

def cksum(input_string):
  log = logging.getLogger(__name__)
  log.debug('Input string: {}'.format(input_string))
  cap_string = ''.join([str.capitalize(x) for x in input_string])
  log.debug('Capitalized string: {}'.format(cap_string))
  space_free_string = re.sub('\s+', '', cap_string)
  log.debug('Space free string: {}'.format(space_free_string))
  prefix = space_free_string[:2]
  log.debug('Prefix string: {}'.format(prefix))
  suffix_string = cap_string[2:]
  log.debug('Suffix string: {}'.format(suffix_string))
  suffix_sum = sum([ord(x)-ord('A') for x in suffix_string])
  log.debug('Suffix sum: {}'.format(suffix_sum))
  return('{}{}'.format(prefix, suffix_sum % 999))

def main(self, args):
  plate.log.info('Starting program.')
  print(cksum(plate.args.input_string))
  plate.log.info('Stopping program.')
  pass

if __name__ == '__main__':
  plate = boilerplate.Boilerplate(main, 'Compute simple checksum')
  plate.parser.add_argument('input_string', type=str,
    help='The string to compute the checksum for')
  plate.main()
  pass
