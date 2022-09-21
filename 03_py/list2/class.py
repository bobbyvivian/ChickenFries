def count_evens(nums):
  count = 0
  for num in nums:
    if num%2==0: #checks if num is divisble by 2, if is, then it's even
      count+=1
  return count

 def big_diff(nums):
  small = nums[0]
  big = nums[0]
  for num in nums: #loop through array to look for min/max
    small = min(small, num) #find the smallest val
    big = max(big, num) #find the biggest val
  return big - small

def centered_average(nums):
  small = nums[0]
  big = nums[0]
  count = 0
  for num in nums:
    small = min(small, num) #find min
    big = max(big, num) # find max
    count += num #add all the vals together
  count -= small+big #get rid of min and max from total count
  return count / (len(nums) - 2)

def sum13(nums):
  count = 0
  i = 0
  while i < len(nums):
    if nums[i] != 13:
      count += nums[i]
    else:
      i+=1
    i+=1
  return count

def sum67(nums):
  count = 0
  i = 0
  add = True
  while i < len(nums):
    if nums[i]==6: #check if its a 6, if is, dont add and make it so that you cant add for all vals after
      add = False
    if add: #only add if you have permission from this boolean
      count+=nums[i]
    if nums[i] == 7 and add==False: # if 7 and previously couldnt add, then make it so that now you can add
      add = True

    i+=1
  return count
