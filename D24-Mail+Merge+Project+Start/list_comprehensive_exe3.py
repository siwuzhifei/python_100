with open("file1.txt") as f1:
  contents1 = [x.strip() for x in f1.readlines()]
  # list1 = [int(contents1[i]) for i in range(len(contents1))]


with open("file2.txt") as f2:
  contents2 = [x.strip() for x in f2.readlines()]
# list2 = [int(contents2[i]) for i in range(len(contents2))]


compare = [int(num) for num in contents1 if num in contents2]
# result1 = [num for num in list1 if num in list2]


print(compare)