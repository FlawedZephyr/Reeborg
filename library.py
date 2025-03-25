## basic all any level use functions
def walk(distance=-1, actions=[]):
    while distance != 0 and front_is_clear():
        move(); distance -= 1

        # actions are just extra things you want the reeborg
        # to do every time it walks
        for action in actions:
            act, params = action; act(*params)

def grab(item=None, amount=-1):
    while amount != 0 and object_here(item):
        if item: take(item)
        else: take()
        amount -=1

def drop(item=None, amount=-1, do_throw=False):
    while amount and carries_object(item):
        (toss if do_throw else put)(item)
        amount -= 1

def count(start=0):
    # sets the value, then runs a while loop: that moves reeborg and adds 1 ot value
    value = start; while not wall_in_front(): move(); value += 1
    
    # returns to the start where counting began
    turn_around(); walk(); turn_around()

    # returns value
    return value


## lambda functions
turn_right = lambda: [turn_left() for _ in range(3)]
turn_around = lambda: [turn_left() for _ in range(2)]

face_north = lambda: (turn_left(), face_north()) if not is_facing_north() else None

check_for_goal = lambda: quit() if at_goal() else None


## level specific functions  
# level: 5
def lane(turn):
    turn(); walk(2, [(grab, ["strawberry"])]); turn_around()
    walk(2); drop(); face_north()            

# level: 7
def one():
    turn_left(); walk(5, [(drop, ["daisy", 1])])
    turn_around(); walk(); turn_left()

# level: 7
def zero():
    turn_left(); walk(5, [(drop, ["daisy", 1])])
    turn_right(); walk(2, [(drop, ["daisy", 1])]) 
    turn_right(); walk(4, [(drop, ["daisy", 1])])
    turn_right(); walk(1, [(drop, ["daisy", 1])]) 
    move(); turn_left(); move(); turn_left()   

# levels: 10, 13
def jump():
    turn_left(); while wall_on_right(): move()
    for _ in range(2): turn_right(); move()
    walk(); turn_left()

# levels: 15, 20
def repair():
    if not wall_on_right(): 
        move()
        if wall_on_right(): 
            turn_around(); move(); turn_left() 
            build_wall(); turn_left()
        else:
            turn_around(); move()
            turn_around(); turn_right()


## bonuses: star tower 1 & 2
def tower():
    face_north(); walk(); turn_around()
    walk(-1, [(drop, ["star", 1])]); turn_left() 

## bonus: target practice
def search():
    while not object_here():
        if front_is_clear(): move()  
        else: 
            turn_around(); walk(); turn_left(); 
            move(); turn_left()
            



            
    
        
    
