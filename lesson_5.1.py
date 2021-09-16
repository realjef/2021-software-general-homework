class Robot:
    position = 0
    arm_position = 0
    cube = False
    score = 0
    def __init__(self, position, arm_position, cube, score):
        self.position = position
        self.arm_position = arm_position
        self.cube = cube
        self.score = score
    def move(self, move_to):
        self.position = move_to
    def arm_movement(self, arm_move):
        self.arm_position = arm_move
    def cube_pickup(self, have_cube):
        if self.position == 3 and self.arm_position == 0 and have_cube == False:
            have_cube == True
    def cube_score(self):
        if self.position == 7 and self.arm_position == 10 and self.have_cube == True:
            self.score = 1
    

bot = Robot(0,0,False,0)
print(bot)