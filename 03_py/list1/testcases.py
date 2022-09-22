print(first_last6([1, 2, 6]) == True)
print(first_last6([6, 1, 2, 3]) == True)
print(first_last6([13, 6, 1, 2, 3]) == False)
print(first_last6([13, 6, 1, 2, 6]) == True)
print(first_last6([3, 2, 1]) == False)
print(first_last6([3, 6, 1]) == False)
print(first_last6([3, 6]) == True)
print(first_last6([6]) == True)
print(first_last6([3]) == False)
print(first_last6([5, 6]) == True)
print(first_last6([5, 5]) == False)
print(first_last6([1, 2, 3, 4, 6]) == True)
print(first_last6([1, 2, 3, 4]) == False)

print(same_first_last([1, 2, 3]) == False)
print(same_first_last([1, 2, 3, 1]) == True)
print(same_first_last([1, 2, 1]) == True)
print(same_first_last([7]) == True)
print(same_first_last([]) == False)
print(same_first_last([1, 2, 3, 4, 5, 1]) == True)
print(same_first_last([1, 2, 3, 4, 5, 13]) == False)
print(same_first_last([13, 2, 3, 4, 5, 13]) == True)
print(same_first_last([7, 7]) == True)

print(make_pi() == [3, 1, 4])

print(common_end([1, 2, 3], [7, 3]) == True)
print(common_end([1, 2, 3], [7, 3, 2]) == False)
print(common_end([1, 2, 3], [1, 3]) == True)
print(common_end([1, 2, 3], [1]) == True)
print(common_end([1, 2, 3], [2]) == False)

print(sum3([1, 2, 3]) == 6)
print(sum3([5, 11, 2]) == 18)
print(sum3([7, 0, 0]) == 7)
print(sum3([1, 2, 1]) == 4)
print(sum3([1, 1, 1]) == 3)
print(sum3([2, 7, 2]) == 11)

print(rotate_left3([1, 2, 3]) == [2, 3, 1])
print(rotate_left3([5, 11, 9]) == [11, 9, 5])
print(rotate_left3([7, 0, 0]) == [0, 0, 7])
print(rotate_left3([1, 2, 1]) == [2, 1, 1])
print(rotate_left3([0, 0, 1]) == [0, 1, 0])

print(reverse3([1, 2, 3]) == [3, 2, 1])
print(reverse3([5, 11, 9]) == [9, 11, 5])
print(reverse3([7, 0, 0]) == [0, 0, 7])
print(reverse3([2, 1, 2]) == [2, 1, 2])
print(reverse3([1, 2, 1]) == [1, 2, 1])
print(reverse3([2, 11, 3]) == [3, 11, 2])
print(reverse3([0, 6, 5]) == [5, 6, 0])
print(reverse3([7, 2, 3]) == [3, 2, 7])

print(max_end3([1, 2, 3]) == [3, 3, 3])
print(max_end3([11, 5, 9]) == [11, 11, 11])
print(max_end3([2, 11, 3]) == [3, 3, 3])
print(max_end3([11, 3, 3]) == [11, 11, 11])
print(max_end3([3, 11, 11]) == [11, 11, 11])
print(max_end3([2, 2, 2]) == [2, 2, 2])
print(max_end3([2, 11, 2]) == [2, 2, 2])
print(max_end3([0, 0, 1]) == [1, 1, 1])

print(sum2([1, 2, 3]) == 3)
print(sum2([1, 1]) == 2)
print(sum2([1, 1, 1, 1]) == 2)
print(sum2([1, 2]) == 3)
print(sum2([1]) == 1)
print(sum2([]) == 0)
print(sum2([4, 5, 6]) == 9)
print(sum2([4]) == 4)

print(middle_way([1, 2, 3], [4, 5, 6]) == [2, 5])
print(middle_way([7, 7, 7], [3, 8, 0]) == [7, 8])
print(middle_way([5, 2, 9], [1, 4, 5]) == [2, 4])
print(middle_way([1, 9, 7], [4, 8, 8]) == [9, 8])
print(middle_way([1, 2, 3], [3, 1, 4]) == [2, 1])
print(middle_way([1, 2, 3], [4, 1, 1]) == [2, 1])

print(make_ends([1, 2, 3]) == [1, 3])
print(make_ends([1, 2, 3, 4]) == [1, 4])
print(make_ends([7, 4, 6, 2]) == [7, 2])
print(make_ends([1, 2, 2, 2, 2, 2, 2, 3]) == [1, 3])
print(make_ends([7, 4]) == [7, 4])
print(make_ends([7]) == [7, 7])
print(make_ends([5, 2, 9]) == [5, 9])
print(make_ends([2, 3, 4, 1]) == [2, 1])

print(has23([2, 5]) == True)
print(has23([4, 3]) == True)
print(has23([4, 5]) == False)
print(has23([2, 2]) == True)
print(has23([3, 2]) == True)
print(has23([3, 3]) == True)
print(has23([7, 7]) == False)
print(has23([3, 9]) == True)
print(has23([9, 5]) == False)
