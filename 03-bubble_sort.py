# 冒泡排序

import random


def bubble_sort(li):
    for i in range(len(li) - 1):  # 第i趟
        exchange = False    # 优化算法，降低时间复杂度
        for j in range(len(li) - i - 1):  # 箭头
            if li[j] > li[j + 1]:  # 升序排列，将大的数放在后方
                li[j], li[j + 1] = li[j + 1], li[j]  # python实现交换语句
                exchange = True
        print(li)  # 展示每一趟的结果
        if not exchange:
            return


li = [random.randint(0, 10000) for i in range(5)]
print(li)
bubble_sort(li)
print(li)

# 冒泡排序
# 时间复杂度：o（n²），未优化的话，无论是否有序，均进行n-1趟排序
#   n-1趟的原因：每一趟均将较大值排好，最后剩下的一定是最小值，故不需要移动第n趟
# 原地排序
# 冒泡排序思路：
#   1.每次一趟遍历无序区，将其中的最大值放在有序区的前面，无序区逐渐变小
#   2.每次遍历比较相邻两值，根据条件两两交换
#   3.每一趟遍历出的最大值均比有序区的最小值还要小，放在有序区最前面即可
# 优化：如果冒泡排序中的一趟排序没有发生交换，则说明列表已经有序，可以直接结束算法

