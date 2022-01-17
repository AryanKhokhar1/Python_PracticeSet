from types import MappingProxyType


Maths = float(input('Enter the marks of Maths :'))
Physics = float(input('Enter the marks of Physics :'))
Chemistry = float(input('Enter the marks of Chemistry :'))
Hindi = float(input('Enter the marks of Hindi :'))
English = float(input('Enter the marks of English :'))
print(f'Percentage = {(Maths + Physics + Chemistry + Hindi + English)/5}')