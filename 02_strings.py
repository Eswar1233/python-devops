sample_str = "This is a sample string"
print(sample_str)

# How to access individual characters form a string
#  zero indexing, space is also a character
print(sample_str[8])

# slicing --> to cut a chunk remove
sub_str = sample_str[2:7]
print(sub_str)

#  positive and negative indexing
#  0123456789 , -9,-8,-7,-6,-5,-4,-3,-2,-1
sub_str_negative = sample_str[-1:-4]
# print(sub_str_negative)


a = "sample"
# a[start : end : step size]
len(a)