def check_subset(s):
    size = len(s)
    for i in range(size):
        for j in range(i+1, size+1):
            print(f's[i:j] = {s[i:j]}, s[i:j][::-1]={s[i:j][::-1]}')

s = 'aaa'
check_subset(s)
