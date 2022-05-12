import cv2
import numpy as np

video = cv2.VideoCapture(0) 
image = cv2.imread("image.jpeg")

while True:
    ret, frame = video.read() 

    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480))

    u_black = np.array([104, 153, 70]) 
    l_black = np.array([30, 30, 0])

    mask = cv2.inRange(frame, l_black, u_black)
    # Getting the area of the frame that is black
    res = cv2.bitwise_and(frame, frame, mask = mask)

    # Getting the area of the frame that is NOT black
    f = frame - res

    # Replacing all areas of f that is not not black (that is black) and replacing it with the image
    f = np.where(f == 0, image, f)

    cv2.imshow("video", frame) 
    cv2.imshow("mask", f) 
    
    # Breaking the program execution when the '1' key is pressed
        # cv2.waitkey(1) returns a 32-bit integer corresponding to the pressed key
        # ord('q') returns the Unicode code point of q
        # 0xFF is a bit mask which sets the left 24 bits to zero, because ord()
        # returns a value betwen 0 and 255, since your keyboard only has a limited
        # character set Therefore, once the mask is applied, it is then possible to
        # check if it is the corresponding key.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release() 
cv2.destroyAllWindows()