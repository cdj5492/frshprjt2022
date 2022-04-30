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
            print(x+y*displayWidth, end='')
            print(A.getPixel(x, y))
            pixels[x+y*displayWidth] = A.getPixel(x, y)
            #pixels[x+y*displayWidth] = (255,255,255)
    #pixels[0] = (255,255,255)
    

if __name__ == '__main__':
    main()