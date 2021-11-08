from random import randint

m = int(input())
n = int(input())
nums1 = [randint(0, m) for i in range(m)]
nums2 = [randint(0, n) for j in range(n)]

def medians(nums1, nums2):
  new_list = nums1 + nums2
  new_list.sort()
  if len(new_list) % 2 == 0:
    result = (new_list[len(new_list)//2] + new_list[len(new_list)//2 - 1]) / 2
  else:
    result = new_list[len(new_list) // 2]
  return result

print(medians(nums1, nums2))
