import cv2
class Detect_Shape:
    def __init__(self,video_path):
        self.video_path=video_path
        self.cap=cv2.VideoCapture(self.video_path) #read the video
        print(self.cap is not None) #check if the video is opened successfully
        self.frame_width=int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #get the width of the video
        self.frame_height=int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #get the height of the video
        self.fps=self.cap.get(cv2.CAP_PROP_FPS) #get the fps (frames per second) of the video
        self.delay=int(1000/self.fps) #calculate the delay between frames
      

    def process_video(self):
        while True: 
            ret,frame=self.cap.read() #read the video frame by frame
            if not ret: #if the video is not read properly
                break
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #convert each frame to grayscale   
            blur=cv2.GaussianBlur(gray,(5,5),0) #apply gaussian blur to each grayscale frame to reduce
            hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #convert each frame to HSV (hue,saturation,value) color space
            blue_mask=cv2.inRange(hsv,(90,50,50),(130,255,255)) #create a mask for blue color in each frame
            blue_contours,_=cv2.findContours(blue_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #find contours of blue color in each frame
            cv2.drawContours(frame,blue_contours,-1,(0,255,0),2) #draw contours of blue color on each frame
            edges=cv2.Canny(blur,50,150) #apply canny edge detection to each blurred frame
            contours,_=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #find contours in each frame
            cv2.drawContours(frame,contours,-1,(0,255,0),2) #draw contours on each frame
            cv2.imshow('Shape Detection',frame) #display each frame with contour
            if cv2.waitKey(self.delay) & 0xFF == ord('q'):
                break
            
        self.cap.release() #close the video file
        cv2.destroyAllWindows() #close all OpenCV windows


video_path='thrown_shapes_noisy_30s.mp4' #path to the video file
shape_detector=Detect_Shape(video_path) #create an object of the Detect_Shape class
shape_detector.process_video() #call the process_video method
