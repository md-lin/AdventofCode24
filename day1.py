#return sum of differences between pairwise elts of sorted lists
def main(list1, list2):
  #sort lists
  list1.sort()
  list2.sort()

  #find difference between pairwise elts of lists and sum
  diff = 0
  for i in range(len(list1)):
    diff += abs(list1[i] - list2[i])

  return diff

list1 = [3, 4, 2, 1, 3, 3]
list2 = [4, 3, 5, 3, 9 ,3]
print(main(list1, list2))
