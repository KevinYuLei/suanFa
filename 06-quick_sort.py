# 快速排序
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 从右边找比tmp小的数
            right -= 1  # 往左走一步
        li[left] = li[right]  # 把右边的值写到左边的空位上
        # print(li, 'right')
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]  # 把左边的值写到右边的空位上
        # print(li, 'left')
    li[left] = tmp  # 把tmp归位
    return left


def quick_sort(li, left, right):
    if left < right:  # 至少两个元素
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
print(li)
quick_sort(li, 0, len(li) - 1)
print(li)

# 快速排序
# 时间复杂度；o（nlogn）
# 原地排序
# 排序牛逼三人组：快速排序
# 快速排序思路：
#   1.取一个元素p（第一个元素），使元素p归为
#   2.列表被p分成两部分，左边都比p小，右边都比p大
#   3.递归完成排序
# 问题：
#   最坏情况，时间复杂度达到o（n²），通过随机化初始值解决
#   递归