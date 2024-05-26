import cv2
from mjpeg_streamer import MjpegServer, Stream

cap = cv2.VideoCapture(4)
cap2 = cv2.VideoCapture(1)

stream = Stream("my_camera", size=(1920, 1080), quality=100, fps=30)
stream2 = Stream("my_camera2", size=(1920, 1080), quality=100, fps=30)

server = MjpegServer("0.0.0.0", 8080)
server.add_stream(stream)
server.add_stream(stream2)
server.start()

while True:
		_, frame = cap.read()
		stream.set_frame(frame)
		
		_, frame2 = cap2.read()
		stream2.set_frame(frame2)