# There are 2 methods to create a tuple
#  1. ()
#  2. tuple()
# Behaviour --> they are immutable --> variables defined cannot be changed.


sample_tuple = ("Ansible", "Terraform", "Docker", "Jenkins", "Docker", "K8s")


sample_ele = sample_tuple[4]
print(sample_ele)


sample_ele = sample_tuple[-1]
print(sample_ele)


# Slicing  --> start is included, stop is excluded.
# Start at index 1 and stop before index 3.
sliced_tuple = sample_tuple[1:3]
print(sliced_tuple)



sliced_tuple_len = len(sliced_tuple)
print(sliced_tuple_len)

# sample_tuple[1] = "Shell"
# print(sample_tuple)



# Operations
res_tuple = sample_tuple + sliced_tuple
print(res_tuple)


res_tuple_1 = sliced_tuple * 2
print(res_tuple_1)


# Methods
k8s_index = res_tuple.index("Docker")
print(k8s_index)


# Tuple unpacking
ansible, terraform, jenkins, docker, k8s  = ("Ansible", "Terraform", "Jenkins", "Docker", "K8s")

print(ansible, terraform, jenkins, docker, k8s )



ansible, *tools , jenkins  = ("Ansible", "Terraform", "Jenkins", "Docker", "K8s")

print(ansible, *tools , jenkins)
print(*tools)