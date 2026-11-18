import numpy as np
import matplotlib.pyplot as plt
p1 = np.array([
    1, 1, 1, 1, 1,
    -1,-1,1,-1,-1,
    -1,-1,1,-1,-1,
    -1,-1,1,-1,-1,
    1, 1, 1, 1, 1
    ])

p2 = np.array([
    1, 1, 1, 1,1,
    1,-1,-1,-1,1,
    1,-1, 1,-1,1,
    1,-1,-1,-1,1,
    1, 1, 1, 1,1
    ])

w = np.zeros((25, 25))
patterns = [p1 , p2]
for p in patterns:
    w += np.outer(p, p)

np.fill_diagonal(w , 0)
w /= 25

noisy = np.array([
    1, 1, 1, 1,1,
    1,-1,-1,-1,1,
    1,-1,-1,-1,1,
    -1,-1,-1,-1,1,
    -1, 1, 1, -1,1
    ])

output = noisy.copy()

for _ in range(200):
    out = output.copy()

    for i in np.random.permutation(25):
        h = w[i] @ out
        output[i] = 1 if h >= 0 else -1

    if np.array_equal(output , out):
        break;
    
    
#Not needed you can show that it can be is equal to one the pattern
flt , ax = plt.subplots(1,4)
patterns.append(noisy)
patterns.append(output)

title = ["p1", "p2", "noisy", "output"]

for a , p, t in zip(ax , patterns, title):
    a.imshow(p.reshape(5,5))
    a.set_title(t)
    a.axis(False)
plt.show()
