#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int graph[26][26] = {0};
int apart[26*26] = {0};
int n, count, sum = 0;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int dfs(int x, int y){
    if(x < 0 || y < 0 || x >= n || y >= n) return 0;
        
    if(graph[x][y] == 1) {
        graph[x][y] = 0;
        count++;
        
        for(int i = 0; i < 4; i++) {
            dfs(x + dx[i], y + dy[i]);
        }
        return 1;
        
    }
    return 0;
    
}

int main()
{
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            scanf("%1d", graph[i] + j);
        }
    }
    
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if(dfs(i, j) == 1) {
                apart[count]++;
                count = 0;
                sum++;
            }
        }
    }
    
    printf("%d\n", sum);
    
    for(int i = 0; i < 26*26; i++) {
        if(apart[i] != 0){
            int k = apart[i];
            for(int j = 0; j < k; j++) {
                printf("%d\n", i);
            }
        }
    }
    
    return 0;
}