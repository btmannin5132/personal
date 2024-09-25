#CreepyPeteMotionDetection.

import sensor, image, pyb, os, time
from pyb import Pin

TRIGGER_THRESHOLD = 25

sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.RGB565) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.QVGA) # or sensor.QQVGA (or others)
sensor.skip_frames(time = 2000) # Let new settings take affect.
sensor.set_auto_whitebal(False) # Turn off white balance.
clock = time.clock() # Tracks FPS.

pin1 = Pin('P1', Pin.OUT_PP, Pin.PULL_NONE)


extra_fb = sensor.alloc_extra_fb(sensor.width(), sensor.height(), sensor.RGB565)


now = time.time()

while(True):

    pin1.value(0)
    print("About to save background image...")
    sensor.skip_frames(time = 2000) # Give the user time to get ready.
    extra_fb.replace(sensor.snapshot())
    print("Saved background image - Now frame differencing!")

    while(True):
        clock.tick() # Track elapsed milliseconds between snapshots().
        img = sensor.snapshot() # Take a picture and return the image.

        # Replace the image with the "abs(NEW-OLD)" frame difference.
        img.difference(extra_fb)

        hist = img.get_histogram()

        diff = hist.get_percentile(0.99).l_value() - hist.get_percentile(0.90).l_value()
       # print(diff)
        triggered = diff > TRIGGER_THRESHOLD
        print(time.time(), diff, triggered)
        if triggered == True:
            pin1.value(1)
            time.sleep(5)
            pin1.value(0)


        if time.time() > now + 5:
            now = time.time()
            break
