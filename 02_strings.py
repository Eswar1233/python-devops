sample_str = "This is a sample string"
print(sample_str)

# How to access individual characters form a string
#  zero indexing, space is also a character
#  strings are immutable --> values cant be altered after they are defined

print(sample_str[8])

# slicing --> to cut a chunk remove
sub_str = sample_str[2:7]
print(sub_str)

#  positive and negative indexing
#  0123456789 , -9,-8,-7,-6,-5,-4,-3,-2,-1
sub_str_negative = sample_str[-1:-4:-1]
print(sub_str_negative)


a = "sample"
# a[start : end : step size]
sample_str = "This-is-a-sample-string"
sub_str = sample_str[:]
print(sample_str)

sub_str = sample_str[1:]
print(sub_str)

sub_str = sample_str[:5]
print(sub_str)

sub_str = sample_str[::2]
print(sub_str)

# Reverse a string
sub_str = sample_str[::-1]
print(sub_str)

# Lenght of string
len_str = len(sample_str)
print("length of string:", len_str);




# Each and everydata types in python has several method that are given by default
sample_str = "this is a sample string"
print(sample_str.capitalize())


#  Method --> is used for class based object. -> aa particular datatype ki matrame aa method apply avuthundhi   
  # ex: capitalize() , split(), join() , format(), count() , strip() etc
# Function --> can be used for any object ---> len()

sample_str = "This is a sample string"

str_split = sample_str.split()
print(str_split, type(str_split))

join_split_str = " ".join(str_split)
print(join_split_str, type(join_split_str))



count_a = sample_str.count('a')
print(count_a)

#strip --> remove firts and last spaces, lstrip, rstrip 


sample_str = "              devops is a very god career chaoice    "
strip_str = sample_str.strip()

print(strip_str)


#  strings are immutable --> values cant be altered after they are defined
sample_str = "This is a sample string"
# we try changine last value g to G  --> we get error
sample_str[-1] = 'G'
print(sample_str)