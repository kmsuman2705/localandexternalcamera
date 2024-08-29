import cv2

class Camera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)  # 0 for default camera

    def __del__(self):
        self.video.release()

    def video_stream(self):
        while True:
            success, frame = self.video.read()
            if not success:
                break
            ret, jpeg = cv2.imencode('.jpg', frame)
            if not ret:
                break
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
