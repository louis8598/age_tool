#年齡判斷小工具
country = input('請輸入您的國籍:')
age = input('請輸入您的年齡:')
age = int(age)
if country == '台灣':
    if age >= 18:
        print('恭喜!你可以考駕照~')
    else:
        print('請到18歲再來考駕照~')
elif country == '臺灣':
    if age >= 18:
        print('恭喜!你可以考駕照~')
    else:
        print('請到18歲再來考駕照~')
elif country == 'taiwan':
    if age >= 18:
        print('恭喜!你可以考駕照~')
    else:
        print('請到18歲再來考駕照~')
else:
    print('你在台灣不允許考駕照')
