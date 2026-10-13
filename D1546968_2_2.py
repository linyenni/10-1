x = int(input('請輸入1或0:'))
y = int(input('請輸入1或0:'))
s = int(input('請輸入1或0:'))

if x not in [0, 1] or y not in [0, 1] or s not in [0, 1]:
  print('輸入錯誤')
else:
  if x != y:
     middle = 1
  else: middle=0

  if middle == 1 and s==1:
     start=1
  else: start=0

  print('第一個閘輸出=',middle)
  print('允許啟動＝',start)