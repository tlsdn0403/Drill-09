from pico2d import *
from grass import Grass
from boy import Boy
from game_world import *

def handle_events():
    global running, boy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)

def reset_world():
    global running, boy
    running = True
    grass = Grass()
    add_object(grass, 1)

    boy = Boy()
    add_object(boy, 0)

def update_world():
    update()  # game_world의 update 함수를 호출하여 world 업데이트

def render_world():
    clear_canvas()
    render()  # game_world의 render 함수를 호출하여 world 렌더링
    update_canvas()

# main game loop
open_canvas()
reset_world()
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
close_canvas()
