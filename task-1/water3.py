def initial_state():
    return (8, 0, 0)

def is_goal(s):
    x, y, z = s
    return x == 4 and y == 4

def successors(s):
    x, y, z = s
    # 8 to 5
    if x > 0 and y < 5:
        pour_amount = min(x, 5 - y)
        
        print(pour_amount,end='')
        new_state = ((x - pour_amount, y + pour_amount, z),x)
        yield new_state

    # 8 to 3
    if x > 0 and z < 3:
        pour_amount = min(x, 3 - z)
        new_state = ((x - pour_amount, y, z + pour_amount),x)
        yield new_state

    # 5 to 8
    if y > 0 and x < 8:
        pour_amount = min(y, 8 - x)
        new_state = ((x + pour_amount, y - pour_amount, z),y)
        yield new_state

    # 5 to 3
    if y > 0 and z < 3:
        pour_amount = min(y, 3 - z)
        new_state = ((x, y - pour_amount, z + pour_amount),y)
        yield new_state

    # 3 to 8
    if z > 0 and x < 8:
        pour_amount = min(z, 8 - x)
        new_state = ((x + pour_amount, y, z - pour_amount),z)
        yield new_state

    # 3 to 5
    if z > 0 and y < 5:
        pour_amount = min(z, 5 - y)
        new_state = ((x, y + pour_amount, z - pour_amount),z)
        yield new_state
