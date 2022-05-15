
if __name__ == "__main__":
  input_size = int(input())
  list = []
  for i in range(input_size):
    list.append(int(input()))
  
  list.sort()
  for i in list:
    print(i)