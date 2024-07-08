# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
# 示例 1:
# 输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
# 示例 2:
#
# 输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1

# 对于二分查找，我们常见的两种区间定义分别为:
# [left,right]   左闭右闭
# [left,right)   左闭右开
# 1.对于第一种左闭右闭的区间定义：
# [left,right]
#实例代码如下：
#需要注意的点：
#1.middle必须是整形，我们每次将(left+right)/2会得到一个中间下标，无论middle是取整数部分还是四舍五入，它只是去划定边界，假如值不相等，那就去除一边加上它自己的值。
#2.数组都是从0开始的。
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = int((left+right)/2)
            if nums[middle] > target:
                right = middle-1
            elif nums[middle] < target:
                left = middle+1
            else :
                return middle
        return -1
#2.对于左闭右开的区间：
