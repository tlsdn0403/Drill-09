from pico2d import load_image
from game_world import*
class Ball:
    image = None
    def __init__(self, x = 400, y = 300, velocity = 1):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity
    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        self.x += self.velocity
    def fire_ball(self):
        ball = Ball(self.x, self.y, self.face_dir*10)
        add_object(ball, 1)