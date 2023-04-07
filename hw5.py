def read_number(n):
    _hund = n // 100
    _ten = (n % 100) // 10
    _one = ((n % 100) % 10) // 1
    
    x = read_single_number(_hund) + read_single_number(_ten) + read_single_number(_one)
    return x

def read_single_number(n):
    if n == 9:
        return '구'
    elif n == 8:
        return '팔'
    elif n == 7:
        return '칠'
    elif n == 6:
        return '육'
    elif n == 5:
        return '오'
    elif n == 4:
        return '사'
    elif n == 3:
        return '삼'
    elif n == 2:
        return '이'
    elif n == 1:
        return '일'
    else:
        return '영'

x = int(input("세 자리 정수 입력: "))
str = read_number(x)
print(str[0], str[1], str[2])