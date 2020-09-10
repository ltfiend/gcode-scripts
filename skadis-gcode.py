#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-H", "--height", dest='height', action='store', type=int, help="Height of Board")
parser.add_argument("-w", "--width", dest='width', action='store',  type=int, help="Width of Board")
parser.add_argument("-b", "--border", dest='border', action='store',  type=int, help="Top/Bottom Border, adds 5 for sides")
parser.add_argument("-s", "--skip", dest='skip', action='store_true', help="Skip every other line")
parser.add_argument("-i", "--inline", dest='inline', action='store_true', help="Inline cuts")
args = parser.parse_args()
border=args.border if args.border else 10

def header():
    print("""G17 G90
G21
M3 S5.000
G0 Z2""")

def plunge():
    print("G0 Z-3 F150")

def raise2():
    print("G0 Z3 F150")

def cutslot(x, y):
    yend = y+10
    print("G0 X" + str(x), "Y" +str(yend), "F150")

def move(x, y):
    print ("G0 X" + str(x), "Y" +str(y), "F150")

wwidth = int((args.width-(border*2+10))/2)
wheight = int((args.height-(border *2))/2)

# Row Height, defined by Y location
global a
a = bool(1)
header()
for y in range(-wheight, wheight, 20):
    if a:
      if not args.inline: a = bool(0)
      for x in range(-wwidth+20, wwidth-20, 40):
          # plunge, travel down y+10
          move(x, y)
          plunge()
          cutslot(x, y)
          raise2()
    else:
      a = bool(1)
      if not args.skip:
          for x in range(-wwidth, wwidth, 40):
          # plunge, travel down y+10
              move(x, y)
              plunge()
              cutslot(x, y)
              raise2()
