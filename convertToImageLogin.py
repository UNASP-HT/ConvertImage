from PIL import Image
import glob, os

size = 1920, 1280
cont = 0
for infile in glob.glob("Converter/*"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size, Image.ANTIALIAS)    
    cont+=1
    im.convert('RGB').save(str(cont)+".jpg","JPEG")
    #im.save(file + "_cv.jpg", "JPEG")