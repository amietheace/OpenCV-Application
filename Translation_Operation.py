# Translation Operation(Shifting an Image)
# Using cv2.warpAffine(img, T, (columns, rows))
# T is a matrix of pixels describing how much shift
# T = np.float32([[1,0, H-howmuch],[0,1,V-howmuch]])
# [0,1] means that img should be shifted along vertiaclly
# [1,0] means that img should be shifted along horizontally



import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path = "D:\\CV_and_NLP\\opencv\\dataset\\"
    imgpath1 =  path + "4.2.01.tiff"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    
    rows, columns, channels = img1.shape
    
    T = np.float32([[1, 0, 150], [0, 1, 50]])
    
    print(T)
    
    
    output = cv2.warpAffine(img1, T, (columns, rows))
    
    
    plt.imshow(output)
    plt.title('Shifted Image')
    plt.show()

if __name__ == "__main__":
    main()