from pico2d import *

import GameWorld
from grass import Grass
from boy import Boy


# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def reset_world():
    global running
    global grass
    global team
    global boy

    running = True

    grass = Grass()
    GameWorld.add_object(grass,0)

    boy = Boy()
    GameWorld.add_object(boy)




def update_world():

    GameWorld.update()




def render_world():
    clear_canvas()
    GameWorld.render()
    update_canvas()


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
