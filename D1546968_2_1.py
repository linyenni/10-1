x = int(input('請輸入1或0:'))
y = int(input('請輸入1或0:'))

if x not in [0, 1] or y not in [0, 1]:
  print('輸入錯誤')
else:
  if x == 1 or y == 1:
     OR = 1
  else:
     OR = 0
  if x == 1 and y == 1:
     AND = 1
  else:
     AND = 0
  if x != y:
     XOR = 1
  else:
     XOR = 0

  print('OR =', OR)
  print('AND =', AND)
  print('XOR =', XOR)