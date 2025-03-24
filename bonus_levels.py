#####################################

# FlawedZephyr
# 03/19/2025
# Completed Reeborg's World
#  ⤷ bonus levels: 1 - 7

#####################################
from REEBORG import *

## basic code for all levels
from library import *
think(0)

## bonus level 1: Star tower 1
count_x = count(1); turn_around(); walk()
for i in range(1, count_x+1): 
    if i % 2 == 1: tower(); walk(1) 
    else: walk(1)

## bonus level 2: Star tower 2
count_x = count(1); turn_around(); walk()
for i in range(1, count_x+1): 
    if i % 2 == 1: tower(); walk(1) 
    else: walk(1)

## bonus level 3: target practice
face_north(); search()
for _ in range(4):        
    len_count = 0; while front_is_clear(): walk(1, [(drop, ["triangle",1])]); len_count += 1
    turn_around(); walk(len_count); turn_around(); turn_left()

## bonus level 4: line follower
while True:
    if object_here():
        take(); move()
    else:
        for turn in [turn_left, turn_around]:
            turn_around(); move(); turn_around(); turn(); move()
            if object_here():
                take(); move(); break
        else:
            turn_around(); move(); break

## bonus level 5: Double the pile
while not object_here("square"): move()
pile_count = 0; while object_here("square"): take(); pile_count += 1
move(); drop("square", pile_count*2)

## bonus level 6: find the center 1
count_x = count(1); walk(count_x // 2); drop("token", 1)

## bonus level 7: find the center 2
count_x = count(1); turn_left(); count_y = count(1); turn_right()
walk(count_x // 2); turn_left(); walk(count_y // 2); drop("token", 1)
