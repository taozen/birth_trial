## Problem description

There's an evil country where every couple prefer boys to girls. 
They keep producing babies until they get a boy. 
What's the gender ratio of this country?

## Code
```python
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

```

## Simulation
```
$ python trial.py
girls= 1001492 , boys= 1000000 , ratio= 1.001492
girls= 998178 , boys= 1000000 , ratio= 0.998178
girls= 1001550 , boys= 1000000 , ratio= 1.00155
girls= 1001266 , boys= 1000000 , ratio= 1.001266
girls= 996568 , boys= 1000000 , ratio= 0.996568
girls= 999342 , boys= 1000000 , ratio= 0.999342
girls= 1000515 , boys= 1000000 , ratio= 1.000515
girls= 1000379 , boys= 1000000 , ratio= 1.000379
girls= 1001829 , boys= 1000000 , ratio= 1.001829
girls= 1002272 , boys= 1000000 , ratio= 1.002272

```

## Conclusion

The number of female and that of male are even. 
