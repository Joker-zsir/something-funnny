import picamera
import os
import time

IMAGE_PATH_DEFAULT = './images/'
IMAGE_NAME_DEFAULT = 'IM'
LIVE_VIEW_SHOW_TIME_DEFAULT = 10

class Camera(object):
    def __init__(self, image_path = IMAGE_PATH_DEFAULT, image_name = IMAGE_NAME_DEFAULT):
        self.camera_obj = picamera.PiCamera()
        self.image_path = image_path
        self.image_name = image_name

        if not os.path.exists(self.image_path)
            os.makedirs(self.image_path)

    def capture(self):
        cur_time = time.localtime(time.time())
        self.camera_obj.capture(self.image_path + self.image_name + '%4d%2d%2d%2d%2d%2d.jpg'%(cur_time.tm_year, cur_time.tm_mon, cur_time.tm_mday, cur_time.tm_hour, cur_time.tm_min, cur_time.tm_sec))
        time.sleep(1)

    def live_view(self, show_time = LIVE_VIEW_SHOW_TIME_DEFAULT):
        self.camera_obj.start_preview()
        time.sleep(show_time)
        self.camera_obj.stop_preview()

def test():
    camera = Camera()
    camera.capture()
    camera.live_view()

if __name__ == '__main__':
    test()
