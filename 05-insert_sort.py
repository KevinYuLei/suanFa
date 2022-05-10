# 插入排序
import random


def insert_sort(li):
    for i in range(1, len(li)):  # i表示摸到的下一个数的下标
        tmp = li[i]  # 记录新摸到的数的值
        j = i - 1  # 从有序区的最后一个值往前比较，j就是有序区的下标
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp  # while循环结束后，找到了准确位置，将新值插入即可
        print(li, i, '趟')  # 记录每一趟结果


li = [random.randint(0, 500) for i in range(5)]
print(li)
insert_sort(li)
print(li)

# 插入排序
# 时间复杂度o（n²），因为有两层循环
# 原地排序
# 插入排序思路：
#   1.将无序区的值记录，然后从有序区最后一个值向前比较
#   2.有序区的值依次向后移动，直到找到正确位置
#   3.插入新值即可
# 排序lowB三人组：冒泡排序、选择排序、插入排序
