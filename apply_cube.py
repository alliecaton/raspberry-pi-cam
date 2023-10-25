from PIL import Image
from pillow_lut import load_cube_file
import cv2
import numpy as np

def apply(filename):
  original_file_path = 'assets/' + filename
  img = Image.open(original_file_path)

  lut = load_cube_file('assets/Presetpro - Emulation.cube')
  img.filter(lut).save(original_file_path)

  # Add noise to image
  image = cv2.imread(original_file_path)

  mean = 0
  stddev = 180
  noise = np.zeros(image.shape, np.uint8)
  cv2.randn(noise, mean, stddev)

  noisy_img = cv2.add(image, noise)

  # Save noisy image
  cv2.imwrite(original_file_path, noisy_img)

apply('ca.png')