class Snake:
    def __init__(self, pos_x, pos_y):
        initial_pos = (pos_x, pos_y)
        self.parts_pos = [initial_pos]

    def forward(self, next_pos, grow:bool):
        self.parts_pos.insert(0, next_pos)
        if not grow:
            self.parts_pos.pop()        
    
    def vetorial_subt(self, pos1, pos2):
        result1 = pos1[0] - pos2[0]
        result2 = pos1[1] - pos2[1]

        return result1, result2

    
