import board
import neopixel

displayWidth = 32
displayHeight = 8

pixels = neopixel.NeoPixel(board.D18, displayWidth * displayHeight)

def main():
    pixels[0] = (255,255,255)

if __name__ == '__main__':
    main()