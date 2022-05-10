# 选择排序
import random


def select_sort_simple(li):  # 简单的选择排序版本，不推荐使用
    li_new = []  # 创建了新的列表，不属于原地排序，不建议使用
    for i in range(len(li)):
        min_val = min(li)  # 该操作的时间复杂度o（n）
        li_new.append(min_val)
        li.remove(min_val)  # 该操作的时间复杂度o（n）
    return li_new


def select_sort(li):
    for i in range(len(li) - 1):  # i是第几趟，共需要n-1趟
        min_loc = i  # 记录最小值的位置，默认取无序区的第一个数的下标
        for j in range(i + 1, len(li)): # 从无序区的第二个数（i+1）开始比较
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
        print(li, i + 1, '趟')  # 打印每一趟后的结果


li = [random.randint(0, 500) for i in range(5)]
print(li)
# select_sort_simple(li)
select_sort(li)
print(li)

# 选择排序
# 时间复杂度：o（n²），两层循环
# 原地排序
# 选择排序思路：
#   1.一趟排序记录最小的数，放到第一个位置
#   2.再一趟排序记录列表无序区最小的数，放到第二个位置
#   3.……以此类推
# 算法关键点：有序区、无序区、无序区最小数的位置
