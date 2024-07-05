# 给定数字范围
n = 10 # 

nums_list = [3,'A',2,2,2,'A','A','7','7','7']# 
n = 8
nums_list = ['A',2,2,2,3,3,2] # [A 3 3 2 A]
#[input().split('')]#[3,'A',2,2,2,'A','A','7','7','7']

# 测试用例
# nums_list = ['A', 2, 2, 2, 3, 3, 2,'A']


def find_last_remaining(nums_list):
    # 连续计数器
    count = 1
    # 当前字符/数字记录器
    current = nums_list[0]
    for i in range(1, len(nums_list)):
        # 如果当前字符/数字与前一个相同，则连续计数器加1
        if nums_list[i] == current:
            count += 1
            # 如果连续出现了3次，则删除这3个元素
            if count == 3:
                # 从列表中删除出现3次的数字/字符
                del nums_list[i-2:i+1]
                break
        else:
            # 否则，重置连续计数器和当前字符/数字记录器
            count = 1
            current = nums_list[i]      
    # 如果列表中所有的元素都没有连续出现3次以上，则返回原列表
    return nums_list
n = int(input())
nums_list = input().split(',')#[item.strip() for item in input().split(',')]
print(nums_list)
# if n <= 2:
#     return ','.join(nums_list)
while True:
    original_length = len(nums_list)
    nums_list = find_last_remaining(nums_list)
    # 如果函数返回的列表长度未变，说明没有连续的3个相同字符/数字被找到
    if len(nums_list) == original_length:
        break
# return ','.join(result)
print(','.join(result))
# print(f"处理结束后剩下的列表是: {result}")

