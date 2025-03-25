#####################################

# FlawedZephyr
# 03/19/2025
# Completed Reeborg's World
#  ⤷ steps: 1 - 20

#####################################
## basic code for all levels
from library import *
think(0)

## level 1
walk()

## level 2
walk(3, [(grab, [])]); walk(2, [(drop, [])])

## level 3
for _ in range(4): walk(); turn_left()

## level 4
walk(); turn_left(); walk(-1, [(grab, ["dandelion"])])
turn_right(); walk(); drop(); turn_right(); walk(); grab()
turn_right(); walk(); turn_left(); walk(3); drop(); move()

## level 5
for side in [turn_left, turn_right, turn_left, turn_right]:
    move(); lane(side)
walk(2)

## level 6
actions = [
(2, turn_left), (3, turn_left), (2, turn_around), (0, grab),
(2, turn_right), (3, turn_right), (2, drop)]

face_north()
for distance, action in actions: 
    walk(distance); action()

## level 7
move(); one(); walk(2); for _ in range(2): zero(); walk(4)
one(); walk(2); zero(); walk(4)

## level 8
move(); walk(11, [(grab, ["dandelion"])]); turn_around()
walk(11); drop(); move()

## level 9
move(); walk(11, [(grab, ["dandelion"])]); turn_around()
walk(11); drop(); move()

## level 10
while not at_goal(): walk(); jump() 

## level 11
for _ in range(4): walk(); grab(); turn_left() 

## level 12
walk(); turn_left(); walk(); turn_around(); grab()
actions = [
    (3, turn_left), (4, turn_left),(4, turn_around),
    (0, drop), (4, turn_right), (4, turn_left),
    (2, turn_right), (1, turn_left)
    ]
for distance, act in actions: walk(distance); act()

## level 13
while not at_goal(): 
    walk(-1, [(check_for_goal, [])]); jump()

## level 14
drop("banana"); move()
while not object_here("banana"): 
    move() if not wall_in_front() else turn_left()
    
## level 15
walk(1); turn_right(); move()
for _ in range(4): walk(-1, [(repair, [])]); turn_left()  
walk(2)

## level 16
turn_left()

while not wall_in_front() and not wall_on_right():
    walk(-1, [(grab, ["carrot"])]); turn_right(); walk(1); turn_right()
    walk(-1, [(grab, ["carrot"])]); turn_left(); walk(1); turn_left()

turn_left(); move(); drop()

## level 17
while not at_goal():
    if right_is_clear(): turn_right(); move()
    elif front_is_clear(): move()
    else: turn_left()
    
## level 18
face_north(); turn_around(); walk(); turn_right(); walk(); face_north()
turn_right(); count_x = count(1); turn_left()
for _ in range(count_x):
    grab(); walk(-1, [(grab, [])]); turn_around(); 
    walk(); turn_left(); walk(1); turn_left() 

walk(); drop(); for _ in range(2): turn_left(); walk()

## level 19
drop(); move()
while not object_here("banana"):
    if right_is_clear(): turn_right(); move()
    elif front_is_clear(): move()
    else: turn_left() 

## level 20
walk(3); turn_right(); move()
for _ in range(6): walk(-1, [(repair, [])]); turn_left()  
walk(2)
