def converter(feet):
    inc = feet * 12
    cm = feet * 30.48
    print('Inches =',inc)
    print('Cm =',cm)

feet = float(input('Enter the length in feet :'))
converter(feet)