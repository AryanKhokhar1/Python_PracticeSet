x = float(input('Enter the value of x :'))
y = float(input('Enter the value of y :'))
if(x ==0 and y == 0):
    print('Point lies on the origin')
elif(y>=0 and x >=0):
    print('Points lies in 1st Quardant')
elif(y>=0 and x<=0):
    print('Points lies in 2nd Quardant')
elif(y<=0 and x<=0):
    print('Points lies in 3d Quardent')
elif(y<=0 and x>=0):
    print('Point lies in 4th Quardant')