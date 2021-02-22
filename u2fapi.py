import requests
import base64
from PIL import Image
from io import BytesIO
import sys
arghlen=len(sys.argv)
if(arghlen==3):
#import aiofiles
    url=sys.argv[1]
    url=url+"files"
    impath=sys.argv[2]
    savepath="./returnimagg.png"
    image=open(impath,'rb')
    files={"file":image}
    r=requests.post(url,files=files)
    im=base64.b64decode(str(r.text[10:-2]))
    img=Image.open(BytesIO(im))
    img.save(savepath,'png')
    print("Image saved at"+savepath)
else:
    print("arg1 is server address arg2 is imagepath")
#encoded_str="b'"r.text[10:-1]
#print(r.content)
#im=Image.open(BytesIO(base64.b64decode(encoded_str)))
#im.save(savepath,'PNG')

#async with aiofiles.open(r.path, mode="rb") as file:
