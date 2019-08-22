"""
Generate percentage frames for load indicator
"""
import sys
from random import randint
import numpy as np
import cv2 as cv
def main(argv):
    
    borderType = cv.BORDER_CONSTANT
    window_name = "Percentage frame maker"
    
    imageName = argv[0] if len(argv) > 0 else 'nvidia256.png'
    imageName = 'nvidia256.jpg'
    nvidia = cv.imread(imageName)
    print(nvidia)
    print(nvidia.shape[1])
    
    width = 256
    height = 256
    bpp = 3
    color  = [0, 255, 0]
    black  = [0, 0, 0]
    white  = [255, 255, 255]
    
    #src = np.ones((width, height, bpp), dtype = "uint8")*255 #white
    src = nvidia
    overlay = src.copy()
        
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
    
    top = int(0.00 * src.shape[0])  # shape[0] = rows
    bottom = int(0.05 * src.shape[0])  # shape[0] = rows
    left = int(0.00 * src.shape[1])  # shape[1] = cols
    right = int(0.00 * src.shape[1])  # shape[1] = cols
    
    percent = 0
    while percent <= 100:
        print(percent/100.0)
        
        cv.rectangle(overlay,(0,                        height),    (width,             int((1.0-percent/100.0)*height)),   color, cv.FILLED)
        
        
        alpha = 0.7  # Transparency factor.
        dst = cv.addWeighted(overlay, alpha, src, 1 - alpha, 0)
        
        cv.rectangle(dst, (0,                       height),    (width,             int(height-height*0.05)),           white, cv.FILLED) #bot border
        cv.rectangle(dst, (0,                       height),    (int(width*0.05),   0),                                 black, cv.FILLED) #left border
        cv.rectangle(dst, (int(width-0.05*width),   height),    (width,             0),                                 white, cv.FILLED) #right border
        cv.rectangle(dst, (0,                       0),         (width,             int(height*0.05)),                  black, cv.FILLED) #top border
        cv.imshow(window_name, dst)
        
        c = cv.waitKey(50)
        if c == 27:
            break

        cv.imwrite('../images/' + str(percent) + '.jpg', dst)         
        
        percent = percent + 1
            
    
        
    return 0
if __name__ == "__main__":
    main(sys.argv[1:])