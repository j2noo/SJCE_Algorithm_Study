#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

void PrintRank(map<int, string> m) {
    for (int i = 0; i < m.size(); i++) {
        cout << m[i] << ' ';
    }
    cout << endl;
}

vector<string> solution(vector<string> players, vector<string> callings) {
    vector<string> answer;

    map<int, string> map1;      //순위와 이름
    map<string, int> map2;      //이름과 순위

    for (int i = 0; i < players.size(); i++) {
        map1[i] = players[i];
        map2[players[i]] = i;
    }

    for (int i = 0; i < callings.size(); i++) {
        int rank = map2[callings[i]];

        map2[callings[i]] -= 1;
        map2[map1[rank - 1]] += 1;

        string tmp = map1[rank];
        map1[rank] = map1[rank - 1];
        map1[rank - 1] = tmp;

        //PrintRank(map1);
    }

    for (int i = 0; i < map1.size(); i++) {
        answer.push_back(map1[i]);
    }

    return answer;
}