height_1 = int(input('Enter The Height For Rectangle 1: '))
width_1 = int(input('Enter The Width For Rectangle 1: '))
height_2 = int(input('Enter The Height For Rectangle 2: '))
width_2 = int(input('Enter The Width For Rectangle 2: '))
rectangle_1 = height_1 * width_1
rectangle_2 = height_2 * width_2
print('Rectangle 1:', rectangle_1) 
print('Rectangle 2:', rectangle_2) 
if rectangle_1 > rectangle_2 : 
    print('Rectangle 1 has more Area than Rectangle 2.')
elif rectangle_1 < rectangle_2 : 
    print('Rectangle 2 has more Area than Rectangle 1.')
elif rectangle_1 == rectangle_2 : 
    print('Rectangle 1 and Rectangle 2 have the same Area!')