# -*- coding: utf-8 -*- 
# 문제1 : 리스트의 삭제
# 다음 리스트에서 400, 500 을 삭제하는 code를 입력하세요.
# nums = [100, 200, 300, 400, 500]

# 해결1
nums = [100,200,300,400,500]
del nums[3]
del nums[3]
print(nums)

# 해결2
nums = [100, 200, 300, 400, 500]
nums = nums[:3]
print(nums)

# 해결3
nums = [100, 200, 300, 400, 500]
nums.pop()
nums.pop()
print(nums)