import cv2
import numpy as np
import os

from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
print(sys.path)





image_folder = 'screen_shot'
video_file = 'result.mp4'
image_size = (3840, 2880) #normale = (640, 480) dpi=600 (3840,2880)
fps = 30    


images=[]
for i in range(0,500):
    images.append('screen_'+str(i)+'.png')

#images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
#images.sort()




out = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, image_size)

img_array = []
i=0
for filename in images:
    print(i)
    i+=1
    img = cv2.imread(os.path.join(image_folder, filename))
    img_array.append(img)
    out.write(img)

out.release()