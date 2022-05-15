class Solution:
  def __init__(self, input_size, threshold, card_list):
    self.input_size = input_size
    self.threshold = threshold
    self.card_list = card_list
    self.maximum = 0

  def solve(self):
    self.__travarse()
    return self.maximum

  def __travarse(self):
    for index1, first_num in enumerate(self.card_list):
      for index2, second_num in enumerate(self.card_list[index1 + 1:]):
        for index3, third_num in enumerate(self.card_list[index2 + 1:]):
          sum = first_num + second_num + third_num
          if self.__is_over_threshold(sum) or self.__is_under_maximum(sum):
            continue
          else:
            self.maximum = sum

  
  def __is_over_threshold(self, sum):
    return True if sum > self.threshold else False
  
  def __is_under_maximum(self, sum):
    return True if sum <= self.maximum else False

if __name__ == "__main__":
  input_size, threshold = [int(i) for i in input().split()]
  card_list = [int(i) for i in input().split()]
  solution = Solution(input_size, threshold, card_list)
  print(solution.solve())
