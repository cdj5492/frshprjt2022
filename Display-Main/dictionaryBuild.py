from PIL import Image
from PIL import GifImagePlugin
import os
cDict = dict()
dirname = os.path.dirname(__file__)

class Glyph:
    def __init__(glyph, path):
        img = Image.open(path)
        glyph.isAnimated = path[len(path)-4:len(path)] == '.gif'
        glyph.width = img.size[0]
        if(glyph.isAnimated == False):
            glyph.pixel = img.load()
        else:
            glyph.pixel = []
            glyph.length = img.n_frames
            for frame in range(0,img.n_frames):
                glyph.pixel.append([])
                img.seek(frame)
                glyph.pixel[frame] = img.load()
    
    def getWidth(glyph):
        return(glyph.width)
    
    def getPixel(glyph, row, col, textColor=(255,255,255), backgroundColor=(0,0,0)):
        if(glyph.pixel[row,col] == (255,255,255)): return(textColor) 
        elif(glyph.pixel[row,col] == (0,0,0)): return(backgroundColor) 
        else: return(glyph.pixel[row,col])

    ''' getPixel functionality for gif frames, not working
    def getAnimatedPixel(glyph, row, col, frame=0, backgroundColor=(0,0,0)):
        if(glyph.pixel[row,col] == (0,0,0)): return(backgroundColor)
        return(glyph.pixel[frame][row,col])
    '''

    def debugPrint(glyph, row):
        if(glyph.isAnimated == False):
                for j in range(glyph.width):
                    if(sum(glyph.pixel[j,row]) >= 672): print('██', end = '')
                    elif(sum(glyph.pixel[j,row]) >= 480): print('▓▓', end = '')
                    elif(sum(glyph.pixel[j,row]) >= 288): print('▒▒', end = '')
                    elif(sum(glyph.pixel[j,row]) >= 96): print('░░', end = '')
                    else: print('  ', end = '')
        ''' Debug print for gif frames, not working
        else:
            print(glyph.pixel)
            for frame in range(glyph.length):
                for i in range(8):
                    for j in range(glyph.width):
                        if(sum(glyph.pixel[frame][j,i]) >= 672): print('██', end = '')
                        elif(sum(glyph.pixel[frame][j,i]) >= 480): print('▓▓', end = '')
                        elif(sum(glyph.pixel[frame][j,i]) >= 288): print('▒▒', end = '')
                        elif(sum(glyph.pixel[frame][j,i]) >= 96): print('░░', end = '')
                        else: print('  ', end = '')
        '''
def dictBuild(relativeDirectory):
    directory = os.path.join(dirname, relativeDirectory)
    for file in os.listdir(directory):
        filename = str(os.fsdecode(file))[0:len(os.fsdecode(file))-4]
        cDict[filename] = Glyph(os.path.join(directory, file))
        continue

def fullDictBuild():
    dictBuild('glyphs/characters/letters')
    dictBuild('glyphs/characters/numbers_big')
    dictBuild('glyphs/characters/numbers_small')
    dictBuild('glyphs/characters/symbols')
    dictBuild('glyphs/characters/arrows')
    dictBuild('glyphs/icons')

if __name__ == '__main__':
    fullDictBuild()
    #for item in cDict:
    #    cDict[item].debugPrint(1)
    statement = ['H','E','L','L','O','U+0020','W','O','R','L','D','cloudy']
    for row in range(8):
        for char in statement:
            cDict[char].debugPrint(row)
        print()