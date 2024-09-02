## 효율성 테스트 실패

keyword = ["language", "area", "level", "food", "score"]

def binary_search(left, right, people, target):
    if left + 1 >= right:
        return left

    mid  = (left + right) // 2

    num = people[mid]["score"]
    if num == target:
        return binary_search(left, mid, people, target)
    elif num > target:
        return binary_search(left, mid, people, target)
    else:
        return binary_search(mid + 1, right, people, target)


def solution(infos, query):
    people = []
    answer = []

    for info in infos:
        info_map = {}
        split = list(info.split(" "))

        info_map["language"] = split[0]
        info_map["area"] = split[1]
        info_map["level"] = split[2]
        info_map["food"] = split[3]
        info_map["score"] = int(split[4])

        people.append(info_map)

    people.sort(key = lambda x : x["score"])

    for q in query:
        q_split_f = list(q.split(" and "))
        q_split_b = list(q_split_f[-1].split(" "))

        q_split = q_split_f[:-1] + q_split_b

        minimum_num = binary_search(0, len(people), people, int(q_split[4]))
        select_people = [i for i in range(minimum_num, len(people))]

        for i in range(4):
            if q_split[i] != "-":
                select_people = [num for num in select_people if people[num][keyword[i]] == q_split[i]]

        select_people = [num for num in select_people if people[num]["score"] >= int(q_split[4])]
        answer.append(len(select_people))

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))