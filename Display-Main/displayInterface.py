import board
import neopixel
import dictionaryBuild




displayWidth = 32
displayHeight = 8

pixels = neopixel.NeoPixel(board.D18, displayWidth * displayHeight)

def main():
    dictionaryBuild.fullDictBuild()
    A = dictionaryBuild.cDict['A']
    for x in range(A.getWidth()):
        for y in range(8):
            print(A.getPixel(y, x))
            pixels[x+y*displayWidth] = A.getPixel(y, x)
    pixels[0] = (255,255,255)

if __name__ == '__main__':
    main()