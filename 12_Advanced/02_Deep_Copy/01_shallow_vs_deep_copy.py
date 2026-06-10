m = [[1,2],[3,4]]

n = m.copy()     # same loc

n[0].append(9)       
print(n,m)

print("\n")

import copy

p = copy.deepcopy(m)  # loc changed
p[0].clear()
p[0].extend([0,9])
print(p,m)