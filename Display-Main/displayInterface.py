import board
import neopixel
import dictionaryBuild




displayWidth = 32
displayHeight = 8

pixels = neopixel.NeoPixel(board.D18, displayWidth * displayHeight)

def main():
    dictionaryBuild.fullDictBuild()
    A = dictionaryBuild.cDict['A']
    for x in range(7):
        for y in range(7):
            pixels[x+y*displayWidth] = A.getPixel(x, y)

if __name__ == '__main__':
    main()