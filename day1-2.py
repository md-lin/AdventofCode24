#return similarity score (for each value in list1 i, sum i*(number of occurrences of i in list2))
def main(list1, list2):

  #find simscore between list1[i] and list2 
  simscore = 0
  for i in range(len(list1)):
    simscore += list1[i] * list2.count(list1[i])
    
  return simscore

# parse list.txt and create two lists
file = open("lists.txt", "r")
list1 = []
list2 = []
for lines in file:
  #print(lines)
  line = lines.split()
  #print(line)
  list1.append(int(line[0]))
  list2.append(int(line[1]))

#print(list1)
#print(list2)

print(main(list1, list2))
