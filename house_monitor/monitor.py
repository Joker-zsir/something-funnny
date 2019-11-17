import time
import body_monitor
import camera

def body_appear(channel):
    cam.capture()
    print 'body'

def body_disappear(channel):
    print 'no'

cam = camera.Camera()
bm = body_monitor.BodyMonitor(12)

bm.rasing_callback_register(body_appear)

time.sleep(10)
