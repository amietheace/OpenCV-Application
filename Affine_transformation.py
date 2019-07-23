# Affine Transformation
# it preserves the parrelism of image
# cv2.getAffineTransform
# cv2.warpAffine

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    path = "D:\\CV_and_NLP\\opencv\\dataset\\"
    imgpath1 = path + "4.2.01.tiff"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
		
    rows, columns, channels = img1.shape
		
    point1 = np.float32([[100,100], [300,100], [100,300]])
    point2 = np.float32([[200,150], [400,150], [400,300]])
		
		
    A = cv2.getAffineTransform(point1, point2)
		
    print(A)
		
    output = cv2.warpAffine(img1, A, (columns, rows))
		
    plt.imshow(output)
    plt.title('Transformed Image')
    plt.show
	
if __name__ == "__main__":
    main()