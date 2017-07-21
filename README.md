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
girls= 967519 , boys= 968807 , ratio= 0.998670529837
girls= 966922 , boys= 968838 , ratio= 0.998022373193
girls= 969174 , boys= 968842 , ratio= 1.00034267713
girls= 965454 , boys= 968885 , ratio= 0.996458816062
girls= 972365 , boys= 968451 , ratio= 1.00404150546
girls= 970183 , boys= 968681 , ratio= 1.00155056205
girls= 969131 , boys= 968731 , ratio= 1.00041291132
girls= 969986 , boys= 968690 , ratio= 1.00133788931
girls= 969365 , boys= 968914 , ratio= 1.00046546959
girls= 969086 , boys= 968719 , ratio= 1.00037885083

```

## Conclusion

The number of female and that of male are even. 
