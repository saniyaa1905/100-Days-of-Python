# ==========================================
# REEBORG'S WORLD CHALLENGES
# These challenges were performed in the Reeborg's World environment.
# ==========================================


# ==========================================
# 1. HURDLE 3
# ==========================================

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


# ==========================================
# 2. HURDLE 4
# ==========================================

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


# ==========================================
# 3. LOST IN A MAZE
# ==========================================

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
