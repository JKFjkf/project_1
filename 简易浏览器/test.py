


def Find_list():
    list = [1]
    i = 1
    num = int(input('数组范围:'))
    for m in range(0,num):
        if m <= num:
            i = i*2
            list.append(i)
    print(list)
    while(1):
        k = len(list) - 1
        count = int(input("输入序号："))
        while(1):
            if count <= k:
                print(list[count])
                break
            else:
                print("宁输入的数字不在数列范围")
                break

if __name__ == '__main__':
    Find_list()