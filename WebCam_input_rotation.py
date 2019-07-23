# Rotating Image Effect
# Rotating Webcam Input


import cv2
import time

def main():
    
	windowName = "Live Video Feed"
	cv2.namedWindow(windowName)
	cap = cv2.VideoCapture(0)
		
	if cap.isOpened():
		ret, frame = cap.read()
	else:
		ret = False
		
	rows, columns, channels = frame.shape
	angle = 0
	scale = 1
		
	while True:
		ret, frame = cap.read()
				
		if angle == 360:
			angle = 0
					
				
				
				
		R = cv2.getRotationMatrix2D((columns/2, rows/2), angle, scale)
				
				
			
		output = cv2.warpAffine(frame, R, (columns, rows))
			
			
		cv2.imshow(windowName, output)
		angle = angle + 1
		time.sleep(0.5)
				
		if cv2.waitKey(1) == 27:
			break
			
	cv2.destroyWindow(windowName)
	cap.release()

if __name__ == "__main__":
    main()