'''
#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
# 求最大子数组和
# @param nums int整型 一维数组 int 数组
# @return int整型
#
class Solution:
    def maxSubArrSum(self, nums):
        # write code here
        start = 0
        cursum = 0
        maxnum = 0
        for num in nums:
            cursum += num
            maxnum = max(maxnum,cursum)
            if cursum < 0:
                cursum = 0
        return int(maxnum)


# nums = eval(input())
nums =  [int(num) for num in input().strip('[]').split(',')]
# print(nums)
# print(type(nums))
s = Solution()
result = s.maxSubArrSum(nums)
print(result)
'''
class node:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def levelPrintTree(self, pre, mid) :
        def dfs(result,precur,midcur):
            # if len(precur) <= 1:
            #     return precur[0]
            n = len(precur) # 当前总节点个数
            root = precur[0]
            # root在右边的位置
            for i,num in enumerate(midcur):
                if num == root:
                    root_index = i
                    break
            result.append(root)
            # pre当中左子树起点
            leftstart = 1 # 
            leftnum = root_index
            if leftstart > root_index:
                return root
            rightstart = 1 + root_index
            rightnum = n - 1 - root_index

            leftree = dfs(result,precur[leftstart:leftstart+leftnum],midcur[:root_index])
            rightree = dfs(result,precur[leftstart+leftnum:],midcur[root_index+1:])
            rootnode = node(root)
            rootnode.left = leftree
            rootnode.right = rightree
            return root

        result = []
        dfs(result,pre,mid)
        return result

input_list = input().strip('')
# print(input_list)
pre,mid = eval(input_list)[0],eval(input_list)[1]
print(pre,mid)
# pre = [1,2,3,4,5]
# mid = [2,1,4,3,5]
s = Solution()
result = s.levelPrintTree(pre,mid)
print(result)