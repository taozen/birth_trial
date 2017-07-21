import random

def simulate(max_num):
    # Stop when we get 1, and return number of 0 before that.
    cnt = 0
    while (random.randrange(0, 2) != 1):
        cnt += 1
        if (cnt == max_num):
            break;

    return cnt

def trial(n_repeat):
    # Run trial once
    girls = 0
    boys = 0
    max_num_children = 5

    for i in range(0, n_repeat):
        cnt = simulate(max_num_children)
        girls += cnt

        if cnt < max_num_children:
            boys += 1

    print "girls=", girls, ", boys=", boys, ", ratio=", float(girls)/boys


for i in range(0, 10):
    trial(1000000)

