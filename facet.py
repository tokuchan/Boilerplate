#!/usr/bin/env python

import boilerplate as bp
import cksum as ck

def facet(args):
  return 'P-{}-{}-{}-{}'.format(
    args.year, ck.cksum(args.publisher), 
    ck.cksum(args.authors_last_name),
    ck.cksum(args.title))

def main(plate, args):
  "Compute the facet classifier for a paper."
  print(facet(args))
  return 0

if __name__ == '__main__':
  plate = bp.Boilerplate(main, 'Compute the facet ID for a paper.')
  plate.parser.add_argument('year', type=int,
    help='The year in which the paper published.')
  plate.parser.add_argument('publisher',
    help='The short name of the publisher of the paper, eg.: OSDI.')
  plate.parser.add_argument('authors_last_name',
    help='The last name of the primary author.')
  plate.parser.add_argument('title',
    help='The full title, including punctuation and space, of the paper.')
  plate.main()
  pass
