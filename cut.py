__author__ = 'zhanxianbo'
from PIL import Image
import os

def cut_image(imagePath,cellSize,quality):
    print imagePath
    path,baseName = os.path.split(imagePath)
    fileName,ext = os.path.splitext(baseName)
    if not os.path.exists(fileName):
        os.mkdir(fileName)
    else:
        for root, dirs, files in os.walk(fileName, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))

    img = Image.open(imagePath)
    w, h = img.size
    print img.tile
    row = h / cellSize
    col = w/ cellSize

    for r in range(0,row):
        for c in range(0,col):
            index = r * col + c + 1
            rect = (c*cellSize,r*cellSize,(c+1)*cellSize,(r+1)*cellSize)
            cropImg = img.crop(rect)
            saveName = fileName+"/"+'{:0>5}'.format(str(index))+ext
            cropImg.save(saveName,quality=quality)
