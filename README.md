# Raspberry Pi 4 Film Simulation Camera Code

This repository holds the Python code that runs on my Raspberry Pi 4 camera. This project is in progress, but the end goal is to transform a broken film camera into a working digital film simulation camera.

I will update the README as things progress with my build!

- [x] Set up Raspberry Pi 4 once all components come in
- [x] Set up Raspberry Pi Camera module & test it works
- [x] Learn about LUTs and HALDCluts
- [x] Programatically apply .cube files and/or HaldCLUTs .png files to an image with Python
- [ ] Programatically apply realistic film grain
- [x] Set up film simulation code to run on Raspberry Pi
- [ ] Set up button & code that will take a photo on button press
- [ ] Figure out portable power source
- [ ] Somehow get the Raspberry Pi inside of a film camera (aka learn how to cut metal 😳)

## Resources

Here is a list of resources I've been using and learning from:

- https://kevinmartinjose.com/2021/04/27/film-simulations-from-scratch-using-python/ : Guide to creating your own CLUTs. Helped me understand what LUTs are from a code perspective.

- https://rawpedia.rawtherapee.com/Film_Simulation : Instrumental in understanding what HaldCLUTs are.

- https://github.com/homm/pillow-lut-tools : Repo for Pillow LUT tools. Looking at the source code and tests helped me figure out why my LUT files were erroring out when using PIL functions.
