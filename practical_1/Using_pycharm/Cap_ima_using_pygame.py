import pygame

import pygame.camera

pygame.camera.init()

camlist = pygame.camera.list_cameras()

if camlist:
    cam = pygame.camera.Camera(camlist[0],(640, 480))
    cam.start()
    image = cam.get_image()
    pygame.image.save(image, "filename.png")

else:
    print("Some error occurs here")
