


import math


angles = (0, 30, 45, 60, 90)
sin_cos = list(map(lambda a: (round(math.sin(math.radians(a)), 4),round(math.cos(math.radians(a)), 4)), angles))
print( sin_cos)