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
