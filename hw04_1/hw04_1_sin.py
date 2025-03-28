import math
print("각 / 라디안 / sin / cos / tan ")
print("-"*30)
for angle in range(0,91):
    radian = round(math.radians(angle),4)
    sin = round(math.sin(radian),4)
    cos = round(math.cos(radian),4)
    tan = round(math.tan(radian),4)
    if angle == 90 :
        tan = "x"
    print (f"{angle} / {radian} / {sin} / {cos} / {tan}")