from  picamera2 import Picamera2, Preview
from PIL import Image
from pillow_lut import load_cube_file
import time
import subprocess
from datetime import datetime
from gpiozero import Button 
from signal import pause

b=Button(27, pull_up=True, active_state=None, bounce_time=0.2)
cam = Picamera2()
camera_config = cam.create_preview_confihub.com
guration(main={"size": (1920, 1080)}, lores={"size": (960, 540)}, display="lores")
cam.configure(camera_config)
cam.start()


def capture(): 
	print('img capture starting')
	img = cam.capture_image("main")

	im = img.convert("RGB")

	date = str(datetime.now())
	filename = date+".jpg"

	lut = load_cube_file("filter.cube")
	im.filter(lut).save(filename)

	subprocess.run([f"filmgrainer --type 1 --sat 0.5 --power 0.8,0.1,0.3 -o '{filename}' '{filename}'"], shell=True)

def released(): 
	print('Finished')

b.when_pressed=capture
b.when_released=released

pause()
