def switch_five(num):
  return str(num).replace('5', '6')

def switch_six(num):
  return str(num).replace('6', '5')


input = input().split(' ')

minA = int(switch_six(input[0]))
minB = int(switch_six(input[1]))
  
maxA = int(switch_five(input[0]))
maxB = int(switch_five(input[1]))

print(minA + minB, maxA + maxB)