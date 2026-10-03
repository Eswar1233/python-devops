def sample_func():
  print("This is a sample function")

def sample_function2():
  print("This is a sample function2")

sample_func()
sample_function2()


def add(num_1, num_2):
  """
  This fucntion performs addition of 2 numbers
  """
  res = num_1 + num_2
  return res


res = add(1,2)
print(res)

res = add(num_2=1, num_1=2)

help(add)




def sum(num_1, num_2, num_3=10):
  """
  This fucntion performs addition of 2 numbers
  """
  res = num_1 + num_2 + num_3
  return res


res = sum(1,2)
print(res)