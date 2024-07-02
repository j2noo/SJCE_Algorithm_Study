def solution(players, callings):
    dic={player: idx for idx, player in enumerate(players)}
    
    for name in callings:
        index=dic[name]
        players[index], players[index-1]=players[index-1], players[index]
        dic[players[index]], dic[players[index-1]]=index,index-1
    
    return players
