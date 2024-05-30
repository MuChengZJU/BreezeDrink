class Animation:
    def __init__(self, start_position, end_position, image):
        self.start_position = start_position
        self.end_position = end_position
        self.image = image
        self.current_position = start_position
        self.finished = False

    def update(self):
        # 简单的线性插值更新动画位置
        if not self.finished:
            self.current_position = (
                self.current_position[0] + (self.end_position[0] - self.start_position[0]) / 10,
                self.current_position[1] + (self.end_position[1] - self.start_position[1]) / 10
            )
            if self.current_position == self.end_position:
                self.finished = True