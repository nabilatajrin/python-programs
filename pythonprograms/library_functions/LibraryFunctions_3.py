from pip._vendor.distlib.compat import raw_input

print('please enter two numbers below:')
base = float(raw_input())
height = float(raw_input())
area = 0.5 * base * height

print (area)