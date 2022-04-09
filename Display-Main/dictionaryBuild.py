from PIL import Image
import os
cDict = dict()
dirname = os.path.dirname(__file__)

class Glyph:
    def __init__(glyph, path):
        img = Image.open(path)
        glyph.width = img.size[0]
        glyph.pixel = img.load()
    
    def getWidth(glyph):
        return(glyph.width)
    
    def getPixel(glyph, row, col, rgb=(255,255,255)):
        if(glyph.pixel[row,col] == (255,255,255)): return(rgb) 
        else: return(glyph.pixel[row,col])

    def debugPrint(glyph):
        for i in range(8):
            for j in range(glyph.width):
                if(glyph.pixel[j,i] == (0, 0, 0)): print(' ', end = ' ')
                else: print('█', end = ' ')
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

def fullDictBuild():
    dictBuild('glyphs/letters')
    dictBuild('glyphs/numbers_big')
    dictBuild('glyphs/numbers_small')
    dictBuild('glyphs/symbols')
    dictBuild('glyphs/arrows')
    dictBuild('glyphs/images')
#for item in cDict:
    #print(item + ': ' + cDict[item])
if __name__ == '__main__':
    fullDictBuild()
    cDict['A'].debugPrint()
    print(cDict['A'].getPixel(4,7))