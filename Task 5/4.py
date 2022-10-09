# Exercise 12: Distance Between Two Points on Earth

import math

t1, g1, t2, g2 = map(int, input("Enter t1, g1, t2, g2: ").split())

t1, g1, t2, g2 = (
    t1 * 180 / math.pi,
    g1 * 180 / math.pi,
    t2 * 180 / math.pi,
    g2 * 180 / math.pi,
)

distance = 6371.01 * (
    math.acos(
        math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2)
    )
)

print("Distance = ", int(distance), sep=" ")
