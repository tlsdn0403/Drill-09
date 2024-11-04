# game_world.py
world = [[], []]  # 깊이별로 나누어진 객체 리스트

def add_object(o, depth=0):
    if depth < len(world):
        world[depth].append(o)
        print(f'Added {o} at depth {depth}')  # 디버깅용 출력

def add_objects(ol, depth=0):
    if depth < len(world):
        world[depth] += ol
        print(f'Added list of objects at depth {depth}')  # 디버깅용 출력

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            print(f'Removed {o}')  # 디버깅용 출력
            return
    print(f'Error: {o} 객체가 존재하지 않습니다.')

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()
