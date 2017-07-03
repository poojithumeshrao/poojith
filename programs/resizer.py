from os import listdir
import PIL.Image as image


c = 0
for f in listdir('/home/poojith/Downloads/test1/'):
    print c
    c+=1
    im=image.open('/home/poojith/Downloads/test1/'+f)
    img = im.resize((256,256),image.BILINEAR)
    img = img.convert('L')
    img.save('/home/poojith/test/'+f)
    
