# 定义一个函数，用于计算满足条件的数字对数量
def count_pairs(arr):
    # 初始化计数器
    count = 0
    # 获取数组的长度
    n = len(arr)
    # 遍历数组中的所有可能的数字对
    for i in range(n):
        for j in range(i+1, n):
            # 计算数字对的差的绝对值
            diff = abs(arr[i] - arr[j])
            # 计算数字对的乘积的5倍
            product_5x = 5 * arr[i] * arr[j]
            # 如果差的绝对值等于乘积的5倍，则增加计数器
            if diff == product_5x:
                count += 1
    # 返回满足条件的数字对数量
    return count

# 假设有一个数组
arr = [1, 3, 4, 8, 9]  # 例子数组，你可以用实际的数组替换它
# 调用函数并打印结果
print(count_pairs(arr))
