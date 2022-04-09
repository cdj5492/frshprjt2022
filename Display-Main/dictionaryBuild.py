from PIL import Image
import os
cDict = dict()
dirname = os.path.dirname(__file__)

class Glyph:
    def __init__(glyph, path):
        img = Image.open(path)
        glyph.width = img.size[0]
        glyph.pixel = []
        for i in range(img.size[1]):
            glyph.pixel.append([])
            for j in range(img.size[0]):
                glyph.pixel[i].append([])
                glyph.pixel[i][j] = img.getpixel((j,i))
                print(img.getpixel((j,i)))

    def getPixel(glyph, row, col, rgb=(255,255,255)):
        if(glyph.pixel[col, row] == (255,255,255)): return(rgb) 
        else: return(glyph.pixel[col, row])

    def debugPrint(glyph):
        for i in range(8):
            for j in range(glyph.width):
                if(glyph.pixel[i][j] == (0, 0, 0)): print('▯', end = '')
                else: print('█', end = '')
            print('')


def dictBuild(relativeDirectory):
    directory = os.path.join(dirname, relativeDirectory)
    for file in os.listdir(directory):
        filename = str(os.fsdecode(file))[0:len(os.fsdecode(file))-4]
        #if filename.startswith("U+") or filename.endswith(".py"): 
        #    print(chr(int(filename[2:len(filename)-4])))
        #    continue
        #else:
        #print(filename)
        cDict[filename] = Glyph(os.path.join(directory, file))
        #print(cDict[filename])
        continue

dictBuild('glyphs/letters')
dictBuild('glyphs/numbers_big')
dictBuild('glyphs/numbers_small')
dictBuild('glyphs/symbols')
dictBuild('glyphs/arrows')
dictBuild('glyphs/images')
#for item in cDict:
    #print(item + ': ' + cDict[item])
cDict['A'].debugPrint()