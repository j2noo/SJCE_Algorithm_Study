def solve(initial_state, goal_state):
  W_initial = initial_state.count('W')
  W_goal = goal_state.count('W')
  letter_diff = abs(W_initial - W_goal) # W의 개수 차이
  
  length = len(initial_state)
  diff = 0 # 각 포지션 별 다른 개수
  for i in range(length):
    if initial_state[i] != goal_state[i]:
      diff += 1
  
  return letter_diff + (diff - letter_diff) // 2

# 입출력
T = int(input())
for _ in range(T):
  N = int(input())
  initial_state = input()
  goal_state = input()
  # print(initial_state, goal_state)
  answer = solve(initial_state, goal_state)
  print(answer)