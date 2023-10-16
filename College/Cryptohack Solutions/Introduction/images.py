import sys
from PIL import Image

img1 = Image.open('lemur.png')
img2 = Image.open('flag.png')
newImage = Image.new('RGB', img1.size)

img1.convert('RGB')
img2.convert('RGB')
pixelmap = newImage.load()

width, height = img1.size#Both images are the same size

for x in range(width):
    for y in range(height):
        ransbin = ""
        gansbin = ""
        bansbin = ""
        r1,g1,b1 = img1.getpixel((x,y))
        r2,g2,b2 = img2.getpixel((x,y))
        r1bin = bin(r1)[2:]
        g1bin = bin(g1)[2:]
        b1bin = bin(b1)[2:]
        r2bin = bin(r2)[2:]
        g2bin = bin(g2)[2:]
        b2bin = bin(b2)[2:]

        while len(r1bin)>len(r2bin):
            r2bin = "0"+r2bin
        while len(r1bin)<len(r2bin):
            r1bin = "0"+r1bin
        for count2 in range(len(r1bin)):
            ransbin += str(int(not r1bin[count2]==r2bin[count2]))
        rans = int(ransbin, 2)

        while len(g1bin)>len(g2bin):
            g2bin = "0"+g2bin
        while len(g1bin)<len(g2bin):
            g1bin = "0"+g1bin
        for count2 in range(len(g1bin)):
            gansbin += str(int(not g1bin[count2]==g2bin[count2]))
        gans = int(gansbin, 2)

        while len(b1bin)>len(b2bin):
            b2bin = "0"+b2bin
        while len(b1bin)<len(b2bin):
            b1bin = "0"+b1bin
        for count2 in range(len(b1bin)):
            bansbin += str(int(not b1bin[count2]==b2bin[count2]))
        bans = int(bansbin, 2)

        pixelmap[x, y] = (rans, gans, bans)

newImage.show()