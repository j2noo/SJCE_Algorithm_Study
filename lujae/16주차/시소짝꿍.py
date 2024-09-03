## 시간: 35분

# def binarySearchStart(weights, target, left, right):
#     if right - left <= 1:
#         return left
#
#     mid = (left + right) // 2
#
#     if right - left == 2:
#         if weights[mid] == target:
#             return mid
#         else:
#             return left
#
#     # print("left=%d mid=%d right=%d" %(left, mid, right))
#
#     if target > weights[mid]:
#         return binarySearchStart(weights, target, mid + 1, right)
#     elif target < weights[mid]:
#         return binarySearchStart(weights, target, left, mid)
#     else:
#         return binarySearchStart(weights, target, left, mid + 1)
# def binarySearchEnd(weights, target, left, right):
#     if right - left <= 1:
#         return left
#
#     mid = (left + right) // 2
#
#     # print("left=%d mid=%d right=%d" % (left, mid, right))
#
#     if target > weights[mid]:
#             return binarySearchEnd(weights, target, mid + 1, right)
#     elif target < weights[mid]:
#             return binarySearchEnd(weights, target, left, mid)
#     else:
#             return binarySearchEnd(weights, target, mid, right)
# def solution(weights):
#     ## 1:1, 2:1, 4:3, 3:2
#     weights.sort()
#     answer = 0
#
#     for i in range(len(weights) - 1):
#         ## 1:1
#         start = binarySearchStart(weights,weights[i], i + 1, len(weights))
#         end = binarySearchEnd(weights, weights[i], i + 1, len(weights))
#
#         if weights[end] == weights[i]:
#             answer += end - start + 1
#
#
#         ## 2:1
#         start = binarySearchStart(weights, 2 * weights[i], i+1, len(weights))
#         end = binarySearchEnd(weights, 2 * weights[i], i+1, len(weights))
#
#         if weights[end] == 2 * weights[i]:
#             answer += end - start + 1
#
#         ## 3:2
#         if weights[i] * 3 % 2 == 0:
#             start = binarySearchStart(weights, weights[i] * 3 // 2, i + 1, len(weights))
#             end = binarySearchEnd(weights, weights[i] * 3 // 2, i + 1, len(weights))
#
#             if weights[end] == weights[i] * 3 // 2:
#                 answer += end - start + 1
#
#         ## 4:3
#         if weights[i] * 4 % 3 == 0:
#             start = binarySearchStart(weights, weights[i] * 4 // 3, i + 1, len(weights))
#             end = binarySearchEnd(weights, weights[i] * 4 // 3, i + 1, len(weights))
#
#             if weights[end] == weights[i] * 4 // 3:
#                         answer += end - start + 1
#
#     return answer
#
# solution([100,180,360,100,270])

def solution(weights):
    answer = 0

    cnt = [0] * 1001

    for w in weights:
        cnt[w] += 1

    # 1 : 1
    for w in range(100, 1001):
        if cnt[w] >= 2:
            answer += cnt[w] * (cnt[w] - 1) // 2

    #  1 : 2, 2 : 3, 3 : 2, 3 : 4
    for w in weights:
        if w % 2 == 0:
            answer += cnt[w // 2]

        if w * 2 % 3 == 0:
            answer += cnt[w * 2 // 3]

        if w * 3 % 4 == 0:
            answer += cnt[w * 3 // 4]

    return answer

