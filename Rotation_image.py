# Rotation of image
# using cv2.getRotationMatrix2D()
# use this matrix in warpAffine() in place of T
# getRotationMatrix2D((columns/2, rows/2), rotation in degree, scalingfactor)
# this scaling factor will scale along both axes

import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "D:\\CV_and_NLP\\opencv\\dataset\\"
    imgpath1 =  path + "4.2.01.tiff"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    
    rows, columns, channels = img1.shape
    
    R = cv2.getRotationMatrix2D((columns/2, rows/2), 370, 1)
    
    print(R)
    
    
    output = cv2.warpAffine(img1, R, (columns, rows))
    
    
    plt.imshow(output)
    plt.title('Ratated Image')
    plt.show()

if __name__ == "__main__":
    main()