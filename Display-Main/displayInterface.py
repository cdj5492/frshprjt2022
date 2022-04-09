import board
import neopixel
import dictionaryBuild




displayWidth = 32
displayHeight = 8

pixels = neopixel.NeoPixel(board.D18, displayWidth * displayHeight)

def main():
    fullDictBuild()
    A = cDict['A']
    for x in range(8):
        for y in range(8):
            pixels[x+y*8] = A.getPixel(x, y)

if __name__ == '__main__':
    main()