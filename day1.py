
#return sum of differences between pairwise elts of sorted lists
def main(list1, list2):
  #sort lists
  list1.sort()
  list2.sort()

  #find difference between pairwise elts of lists and sum
  diff = 0
  for i in range(len(list1)):
    diff += abs(int(list1[i]) - int(list2[i]))

  return diff

# parse list.txt and create two lists
file = open("lists.txt", "r")
list1 = []
list2 = []
for lines in file:
  #print(lines)
  line = lines.split()
  #print(line)
  list1.append(line[0])
  list2.append(line[1])

#print(list1)
#print(list2)

print(main(list1, list2))
