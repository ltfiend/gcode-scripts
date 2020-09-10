#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-H", "--height", required='true', dest='height', action='store', type=int, help="Height of Board")
parser.add_argument("-w", "--width", required='true', dest='width', action='store',  type=int, help="Width of Board")
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

def process(b, y):
    shift=0
    if b and not args.inline: shift=20
    # track alternating lines
    global a
    a = not b
    for x in range(-w_width+shift, w_width-shift, 40):
        # plunge, travel down y+10
        move(x, y)
        plunge()
        cutslot(x, y)
        raise2()


# These center the workspace and calculate the +/- range that the cuts will be made in
w_width = int((args.width-(border*2+10))/2)
w_height = int((args.height-(border *2))/2)
a = bool(1)

header()

y=-w_height
while y+20 < w_height:
    process(a, y)
    if args.skip: y += 40
    else: y += 20
