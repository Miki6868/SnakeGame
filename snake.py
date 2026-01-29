from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
     
    def add_segment(self, position):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()        
        new_snake.goto(position)
        self.segments.append(new_snake)
    
    def extend(self):
        self.add_segment(self.segments[-1].position()) #add new segment to the end of the snake 
        #(lists are 0 indexed)
        
    def move(self):
        # range (start, stop, step), start length(segments)-1 to 0, step -1, use length so when 
        # snake grows , it still works 
        for seg_num in range(len(self.segments) - 1, 0, -1):
            #move segment by grabbing x and y of second last segment, and moving it to that position
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  
    
        self.segments[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)    
    
    def down(self):        
        if self.head.heading() != 90:
            self.head.setheading(270)
            
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)                