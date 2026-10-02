# Create a list

sample_list = ["Ansible", "Terraform", "Docker", "Jenkins", "Docker", "K8s"]


sample_ele = sample_list[1]
print(sample_ele)


sample_ele = sample_list[-1]
print(sample_ele)


# Slicing  --> start is included, stop is excluded.
# Start at index 1 and stop before index 3.
sliced_list = sample_list[1:3]
print(sliced_list)


sliced_list_len = len(sliced_list)
print(sliced_list_len)

# sample_list[1] = "Shell"
# print(sample_list)

# appending to original list --> inplace operation
sample_list = ["Ansible", "Terraform", "Docker", "Jenkins", "Docker", "K8s"]
sample_list.append("Shell")
print(sample_list)


sample_list.append("Promethues")
print(sample_list)

# Append list to list
# more than 1 element add chesthey append ki adhi single lement ga consider chesthundhi
sample_list.append(sample_list)
print(sample_list)


# Extend   -->
sample_list = [1, 2, 3, 'hello', True]
sample_list.extend(sample_list)
#  elements added as individual elements to the existing list as showin in example
print(sample_list)


#  membership operator: in , not in
is_elem = 2 in sample_list
print(is_elem)

is_elem = 2 not in sample_list
print(is_elem)

