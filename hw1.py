#1
def get_radius(prompt):
    r = int(input(prompt))
    return r

#2
def get_circle_area(radius):
    result = radius*radius*3.14
    return result
#3


radius=get_radius('넓이를 구하고자 하는 원의 반지름은?')
area=get_circle_area(radius)
print('반지름', str(radius), '인 원의 넓이 = 3.14 *', radius, '*', radius, '=', area)
