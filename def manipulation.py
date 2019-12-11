def manipulation(x,y,choice):

  def add(x,y):
    z = x+y
    return z,'addition'

  def sub(x,y):
    z = x-y
    return z,'subtraction'

  def multi(x,y):
    z = x*y
    return z,'manipulation'

  def div(x,y):
    z = x/y
    return z,'division'

  def default():
    return 'invalid','Enter a valid choice'

  if choice == 1:
    return add(x,y)
  elif choice == 2:
    return sub(x,y)
  elif choice == 3:
    return multi(x,y)
  elif choice == 4:
    return div(x,y)
  else:
    return default()

x = int(input('Enter x value:'))
y = int(input('Enter y value:'))

print('Enter ur choice')
choice = int(input('1.sum\n2.sub\n3.multi\n4.div\n:'))
r,s = manipulation(x,y,choice)

if r == 'invalid':
  print(s)
else:
  print('{0} of {1} and {2} is {3}'.format(s,x,y,r))


  