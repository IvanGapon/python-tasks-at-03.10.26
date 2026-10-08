class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums :
            return 0
        set_nums = set(nums)

        max_length = 1
        for num in set_nums :
            if ( num - 1) not in set_nums :
                cur = num
                cur_length = 1
                while ( cur + 1 in set_nums):
                    cur_length += 1
                    cur += 1
                max_length = max( max_length , cur_length)

        return max_length
