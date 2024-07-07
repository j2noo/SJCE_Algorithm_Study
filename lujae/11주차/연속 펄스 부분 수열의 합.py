# 시간 : 21분 56초
# 레벨 : 3

sequence = [2, 3, -6, 1, 3, -1, 2, 4]
sequencePulseP = [0] * len(sequence)
sequencePulseN = [0] * len(sequence)

for i in range(len(sequence)):
    if i % 2 == 0:
        sequencePulseP[i] = sequence[i]
        sequencePulseN[i] = -sequence[i]
    else:
        sequencePulseP[i] = -sequence[i]
        sequencePulseN[i] = sequence[i]

## DP
maxSegmentP = [0] * len(sequencePulseP)
maxSegmentN = [0] * len(sequencePulseP)

maxSegmentP[0] = sequencePulseP[0]
for i in range(1, len(maxSegmentP)):
    maxSegmentP[i] = max(sequencePulseP[i], sequencePulseP[i] + maxSegmentP[i - 1])

maxSegmentN[0] = sequencePulseN[0]
for i in range(1, len(maxSegmentN)):
    maxSegmentN[i] = max(sequencePulseN[i], sequencePulseN[i] + maxSegmentN[i - 1])

print(max(max(maxSegmentP), max(maxSegmentN)))


