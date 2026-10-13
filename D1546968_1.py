x = int(input('請輸入數字'))
if 0 <= x <= 15:
    q = x//2
    w = q//2
    e = w//2
    a = x % 2
    s = q % 2
    d = w % 2
    print('二進制=',e,d,s,a)
    r=x//8
    t=x%8
    print('八進制=',r,t)
    if x<10:
        print('十六進制=',x)
    elif x<11:
        print('十六進制=','A')
    elif x<12:
        print('十六進制=','B')
    elif x<13:
        print('十六進制=','C')
    elif x<14:
        print('十六進制=','D')
    elif x<15:
        print('十六進制=','E')
    elif x<16:
        print('十六進制=','F')
else:
    print('輸入錯誤')