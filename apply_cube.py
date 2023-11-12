from PIL import Image
from pillow_lut import load_cube_file

def apply(filename):
  original_file_path = 'assets/' + filename
  img = Image.open(original_file_path)

  # lut = load_cube_file('assets/Lutify.me-Claire-ACEScct-to-ACEScct.cube')
  # lut = load_cube_file('assets/Lutify.me-Claire-RWG-to-RWG.cube')
  # lut = load_cube_file('assets/Lutify.me-FilmTone3-ACEScct-to-ACEScct.cube')
  # lut = load_cube_file('assets/Lutify.me-PrintFilm2-RWG-to-RWG.cube')
  cubefile = 'Presetpro - Kodak Color'
  lut = load_cube_file('assets/'+cubefile+'.cube')
  
  filename = cubefile+'.jpg'
  img.filter(lut).save(filename)

apply('outside.jpg')