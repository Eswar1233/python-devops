sample_list = ["Ansible", "Terrraform", "Docker", "Jenkins", "Argocd"]

for i in sample_list:
    print(i, len(i))

# print element and corresponding index
for i in enumerate(sample_list):
  print(i)

# print element and corresponding index
for idx, i in enumerate(sample_list):
  print(idx, i)


# Range based for loop
#  1:10 --> 1,2,............,9 --> slicing
sample_range = range(0, len(sample_list))
print(sample_range, type(sample_range))

# Range object values ni el consume cheyyali ante we iterate it to get values
for i in sample_range:
  print(i)


for i in range(0, len(sample_list)):
  print(i, sample_list[i])


for i in range(0, len(sample_list)):
  if sample_list[i] == "Docker":
    continue
  print(i, sample_list[i])


for i in range(0, len(sample_list)):
  if sample_list[i] == "Docker":
    break
  print(i, sample_list[i])


for i in range(0, len(sample_list)):
  if sample_list[i] == "Docker":
    pass
  print(i, sample_list[i])


for i in range(0, len(sample_list)):
  if sample_list[i] == "Docker":
    exit(1)
  print(i, sample_list[i])

print(sample_list)


# While loop

sample_list = ["Promethues", "grafana", "Elk", "Sonarqube"]

i = 2

while i < len(sample_list):
  if sample_list[i] == "grafana":
    break
  print(i, sample_list[i])
  i += 1



sample_dict = {1: 1, 2: 4, 3: 9}

for k, v in sample_dict.items():
  print(k, v)