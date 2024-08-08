import random

def cr_check(low, high, cr, crit_fail, crit_success):
    roll = random.randint(low, high)
    if roll >= crit_success:
        return 0
    elif roll >= cr:
        return 1
    elif roll > crit_fail:
        return 2
    else:
        return 3
    
