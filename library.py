
def walk(distance=-1, actions=[]):
    while distance != 0 and front_is_clear():
        move(); distance -= 1
       
        for action in actions:
            act, params = action; act(*params)

turn_right = lambda: [turn_left() for _ in range(3)]
turn_around = lambda: [turn_left() for _ in range(2)]

def face_north(): 
    while not is_facing_north():
        turn_left()

def grab(item=None, amount=-1):
    while amount != 0 and object_here(item):
        if item: take(item)
        else: take()
        amount -=1
        
def jump():
    turn_left(); while wall_on_right(): move()
    for _ in range(2): turn_right(); move()
    walk(); turn_left()

def one():
    turn_left(); walk(5, [(drop, ["daisy", 1])])
    turn_around(); walk(); turn_left()

def zero():
    turn_left(); walk(5, [(drop, ["daisy", 1])])
    turn_right(); walk(2, [(drop, ["daisy", 1])]) 
    turn_right(); walk(4, [(drop, ["daisy", 1])])
    turn_right(); walk(1, [(drop, ["daisy", 1])]) 
    move(); turn_left(); move(); turn_left()    
    
def drop(item=None, amount=-1):
    while amount != 0 and carries_object(item):
        if item: put(item)
        else: put()
        amount -=1

def repair():
    if not wall_on_right(): 
        move()
        if wall_on_right(): 
            turn_around(); move(); turn_left() 
            build_wall(); turn_left()
        else:
            turn_around(); move()
            turn_around(); turn_right()

def lane(turn):
    turn(); walk(2, [(grab, ["strawberry"])]); turn_around()
    walk(2); drop(); face_north()            

def count(start=0):
    value = start
    while not wall_in_front(): 
        move(); value += 1
        
    turn_around(); walk(); turn_around()
    return value

def tower():
    face_north(); walk(); turn_around()
    walk(-1, [(drop, ["star", 1])]); turn_left() 

    
def search():
    while not object_here():
        if front_is_clear(): move()  
        else: 
            turn_around(); walk(); turn_left(); 
            move(); turn_left()
            
def check_for_goal():
    if at_goal(): 
        quit()


            
    
        
    
