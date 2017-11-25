##image loading and grayscale version of it
# import cv2
#
# image = cv2.imread("clouds.jpg")
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Over the Clouds", image)
# cv2.imshow("Over the Clouds - gray", gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

##normal capture
# import cv2
#
# cv2.namedWindow("preview")
# vc = cv2.VideoCapture(0)
# if vc.isOpened(): # try to get the first frame
#     rval, frame = vc.read()
# else:
#     rval = False
# while rval:
#     cv2.imshow("preview", frame)
#     rval, frame = vc.read()
#     key = cv2.waitKey(20)
#     if key == 27: # exit on ESC
#         break
# cv2.destroyWindow("preview")
# vc.release()

##grayscale capture
# import numpy as np
# import cv2
# cap = cv2.VideoCapture(0)
#
# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Display the resulting frame
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()

##Save video to folder
# import numpy as np
# import cv2
#
# cap = cv2.VideoCapture(0)
#
# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
#
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret==True:
#
#         # write the flipped frame
#         out.write(frame)
#
#         cv2.imshow('frame',frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
#
# # Release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()

##Load video from folder
# import numpy as np
# import cv2
#
# cap = cv2.VideoCapture('output.avi')
#
# while(cap.isOpened()):
#     ret, frame = cap.read()
#
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

##Saving couple of images
# from cv2 import *
# import time
# # initialize the camera
# cam = VideoCapture(0)   # 0 -> index of camera
# for i in range(20):
#     s, img = cam.read()
#     if s:           # frame captured without any errors
#         time.sleep(0.2)
#         imwrite("image"+str(i)+".jpg",img) #save image
# destroyWindow("cam-test")

##Binarizing Image according to threshold
# from cv2 import *
# import time
# # initialize the camera
# cam = VideoCapture(0)   # 0 -> index of camera
# for i in range(20):
#     s, frame = cam.read()
#     frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     (thresh, frame_bw) = cv2.threshold(frame_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#     thresh = 127
#     frame_bw = cv2.threshold(frame_gray, thresh, 255, cv2.THRESH_BINARY)[1]
#     if s:           # frame captured without any errors
#         imwrite("image"+str(i)+".jpg",frame_bw) #save image
#         time.sleep(0.2)
# destroyWindow("cam-test")