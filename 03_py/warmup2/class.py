def string_bits(str):
  final = ""
  for i in range (0,len(str),2):
    final+=str[i]
  return final

def string_splosion(str):
  counter = 0
  final = ""
  while counter < len(str):
    final+=str[0:counter+1]
    counter+=1
  return final

def last2(str):
  last = str[-2:]
  count = 0
  for i in range (len(str)-2):
    if str[i:i+2] == last:
      count+=1
  return count

def array_count9(nums):
  count = 0
  for num in nums:
    if num == 9:
      count+=1
  return count

def array_front9(nums):
  i = 0
  while i < 4 and i < len(nums):
    if nums[i] == 9:
      return True
    i+=1
  return False

def array123(nums):
    for i in range(len(nums)-2):
        if nums[i:i+3]==[1,2,3]:
            return True
    return False
def string_match(a, b):
  count = 0
  length = min(len(a), len(b))
  for i in range(length - 1):
    if a[i:i+2] == b[i:i+2]:
      count+=1
  return count

def first_last6(nums):
  return nums[0]==6 or nums[-1]==6

def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[-1]

 def make_pi():
  return [3,1,4]

def common_end(a, b):
  return a[0]==b[0] or a[-1]==b[-1]

def sum3(nums):
  count = 0
  for num in nums:
    count += num
  return count

def rotate_left3(nums):
  arr = []
  for i in range(len(nums)):
    if i != len(nums)-1:
      arr.append(nums[i+1])
  arr.append(nums[0])
  return arr

def reverse3(nums):
  arr = []
  for num in nums:
    arr.insert(0,num)
  return arr
# return arr[::-1] is a soln too

def max_end3(nums):
  m = max(nums[0], nums[-1])
  for i in range(len(nums)):
    nums[i] = m
  return nums

def sum2(nums):
  if len(nums) == 0:
    return 0
  count = 0
  length = min(len(nums), 2)
  for i in range(length):
    count += nums[i]
  return count

def middle_way(a, b):
  return [a[1], b[1]]

def make_ends(nums):
  return [nums[0], nums[-1]]

def has23(nums):
  return nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3
