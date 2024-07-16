# 시간: 30분

def checkNoWord(cardIdxOfGoal):
    if -1 not in cardIdxOfGoal:
        return True

    firstNoWord = cardIdxOfGoal.index(-1)
    lastNoWord = (len(cardIdxOfGoal) - 1) - cardIdxOfGoal[::-1].index(-1)

    if lastNoWord != len(cardIdxOfGoal) - 1:
        return False

    for i in range(firstNoWord, lastNoWord + 1):
        if cardIdxOfGoal[i] != -1:
            return False

    return True

def checkOrder(cardIdxOfGoal):
    newCardIdxOfGoal = [x for x in cardIdxOfGoal if x != -1]

    beforeValue = -1
    for value in newCardIdxOfGoal:
        if value <= beforeValue:
            return False

        beforeValue = value
    return True

def canMakeWord(card1IdxOfGoal, card2IdxOfGoal):
    if not checkNoWord(card1IdxOfGoal) or not checkNoWord(card2IdxOfGoal):
        return False
    if not checkOrder(card1IdxOfGoal) or not checkOrder(card2IdxOfGoal):
        return False

    return True

def solution(cards1, cards2, goal):
    answer = 'Yes'

    card1IdxOfGoal = []
    card2IdxOfGoal = []

    for i, card in enumerate(cards1):
        idx = goal.index(card) if card in goal else -1
        card1IdxOfGoal.append(idx)

    for i, card in enumerate(cards2):
        idx = goal.index(card) if card in goal else -1
        card2IdxOfGoal.append(idx)

    if canMakeWord(card1IdxOfGoal, card2IdxOfGoal):
        answer = 'Yes'
    else:
        answer = 'No'

    return answer