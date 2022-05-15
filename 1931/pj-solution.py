input_size = int(input())
inputs = []
for i in range(input_size):
  inputs.append([int(x) for x in input().split()])
inputs.sort(key=lambda x: (x[1], x[0]))
last_end_time = 0
meeting_counts = 0
for meeting in inputs:
  possible_start_time = meeting[0]
  possible_end_time = meeting[1]
  if last_end_time <= possible_start_time:
    meeting_counts += 1
    last_end_time = possible_end_time
print(meeting_counts) 