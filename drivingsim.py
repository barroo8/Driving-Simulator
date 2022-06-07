import random

import pygame
from pygame.locals import *
from pyvidplayer import Video
from random import randint
from random import seed

#ipad sizes
# w - 1194 //1188
# h - 1709 //1703

# screen_width = 1920
# screen_height = 1080
# screen = pygame.display.set_mode((screen_width, screen_height))

def main():
    pygame.init()

    savta_flag = False
    check = 0
    hz10_flag = False
    funnyFlag = False
    funnyFlag2 = False

    # screen
    screen_width = 1920
    scree_height = 1080
    screen = pygame.display.set_mode((screen_width, scree_height))
    pygame.display.set_caption('Driving Simulator')

    # time components
    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()

    # car interior image
    driver_image = pygame.image.load("venv\driverseat.jpg")
    driver_image = pygame.transform.scale(driver_image, (1620, 895))
    # ipad image
    ipad_image = pygame.image.load("venv\ipad2.png")
    ipad_image = pygame.transform.scale(ipad_image, (300, 375))
    # ipad no background image
    ipad_nobackground_image = pygame.image.load("venv\ipad.png")
    ipad_nobackground_image = pygame.transform.scale(ipad_nobackground_image, (300, 375))

    # driving video
    vid = Video("venv\drive.mp4")
    vid.set_size((1620, 660))
    vid.set_volume(0.7)


    # funny video 10hz
    funnyvid10hz = Video("venv\dogscats2.mp4")
    funnyvid10hz.set_size((237, 325))
    funnyvid10hz.set_volume(0.4)
    # funny video 15hz
    funnyvid15hz = Video("venv\dogscats2.mp4")
    funnyvid15hz.set_size((237, 325))
    #funnyvid10hz.seek(randint(0, 280))
    funnyvid15hz.toggle_pause()
    # savta video
    savtavid = Video("venv\savta (1).mp4")
    savtavid.set_size((1620, 660))
    savtavid.set_volume(0.3)
    savtavid.toggle_pause()

    run = True

    # gameloop function
    while run:
        #seed(1)
        randomNumber = random.randrange(0, 280)
        # count seconds since start
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000

        # display car interior
        screen.blit(driver_image, (0, 0))

        # player lost - hit the savta
        if savta_flag == True:
            savtavid.draw(screen, (0, 0), force_draw=True)
            if savtavid.active == False:
                savtavid.close()
                run = False
        # display driving video
        else:
            vid.draw(screen, (0, 0), force_draw = True)

        # display ipad
        screen.blit(ipad_image, (1256, 490))

        # 10hz and 15hz funny videos loop
        if check == 0:

            if funnyvid10hz.active == False:
                funnyvid10hz = Video("venv\dogscats2.mp4")
                funnyvid10hz.set_size((237, 325))
                funnyvid10hz.seek(randomNumber)

            if funnyvid10hz.get_playback_data()["paused"] == True:
                funnyvid10hz.toggle_pause()
                funnyvid10hz.draw(screen, (1287, 515), force_draw=True)

            elif funnyvid10hz.active == True:
                funnyvid10hz.draw(screen, (1287, 515), force_draw=True)

        if check == 1:
            funnyvid10hz.close()

        if check == 2:
            if funnyvid15hz.active == False:
                funnyvid15hz = Video("venv\dogscats2.mp4")
                funnyvid15hz.set_size((237, 325))
                funnyvid15hz.seek(randomNumber)

            if funnyvid15hz.get_playback_data()["paused"] == True:
                funnyvid15hz.seek(randomNumber)
                funnyvid15hz.toggle_pause()
                funnyvid15hz.draw(screen, (1287, 515), force_draw=True)

            elif funnyvid15hz.active == True:
                funnyvid15hz.draw(screen, (1287, 515), force_draw=True)

        if check == 3:
            funnyvid15hz.close()

            # display no background ipad
            screen.blit(ipad_nobackground_image, (1256, 490))

        # update game display
        pygame.display.update()

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vid.close()
                funnyvid10hz.close()
                savtavid.close()
                run = False
            # ESC to quit game
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    vid.close()
                    if funnyvid10hz.active == True:
                        funnyvid10hz.close()
                    if funnyvid15hz.active == True:
                        funnyvid15hz.close()
                    savtavid.close()
                    run = False
                elif event.key == K_SPACE:
                    if check == 0:
                        check = 1
                    elif check == 1:
                        check = 2
                    elif check == 2:
                        check = 3
                    elif check == 3:
                        check = 0

            elif event.type == MOUSEBUTTONDOWN:
                check = 4
                if funnyFlag == False:
                    funnyFlag = True
                    vid.close()
                    if funnyvid10hz.active == True:
                        funnyvid10hz.close()
                    if funnyvid15hz.active == True:
                        funnyvid15hz.close()
                    savta_flag = True
                    savtavid.toggle_pause()


        #clock.tick(60)
    pygame.quit()

# call game func
main()

# if check == 0:
#     if vid10hz.active == False:
#         vid10hz = Video("venv\hz10.mp4")
#         vid10hz.set_size((237, 325))
#
#     if vid10hz.get_playback_data()["paused"] == True:
#         vid10hz.toggle_pause()
#         vid10hz.draw(screen, (1282, 512), force_draw=True)
#
#     elif vid10hz.active == True:
#         vid10hz.draw(screen, (1282, 512), force_draw=True)
#
# if check == 1:
#     vid10hz.close()
#
# if check == 2:
#     if vid15hz.active == False:
#         vid15hz = Video("venv\hz10.mp4")
#         vid15hz.set_size((237, 325))
#
#     if vid15hz.get_playback_data()["paused"] == True:
#         vid15hz.toggle_pause()
#         vid15hz.draw(screen, (1282, 512), force_draw=True)
#
#     elif vid15hz.active == True:
#         vid15hz.draw(screen, (1282, 512), force_draw=True)
#
# if check == 3:
#     vid15hz.close()


