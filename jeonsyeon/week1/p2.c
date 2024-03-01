#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int Result(char **ch, int row1, int row2, int col1, int col2){
    int w1=0,b1=0,w2=0,b2=0;

    for(int i=row1; i<row2; i++){
        for(int j=col1; j<col2; j++){
            if((i+j)%2==0){
                if(ch[i][j]=='W') w1++;
                else b1++;            
            }
            else{
                if(ch[i][j]=='W') w2++;
                else b2++;  
            }
        }
    }

    if(w1>w2) return b1+w2;
    else return w1+b2;
}

int cut(char **ch, int a, int b){
    int result,min=Result(ch,0,8,0,8);

    for(int i=0; i<a-7; i++){
        for(int j=0; j<b-7; j++){
            result = Result(ch,i,i+8,j,j+8);
             if(result<min) min=result;
        }
    }
    return min;
}

int main(){

    char **ch;
    int a,b,result;

    scanf("%d %d",&a,&b);
    ch=(char**)calloc(a,sizeof(char*));
    for(int i=0; i<a; i++) ch[i]=(char*)calloc(b,sizeof(char)); 
    for(int i=0; i<a; i++){
        scanf("%s",ch[i]);
    }

    if(a==8&&b==8) result = Result(ch,0,8,0,8);
    else result = cut(ch,a,b);

    printf("%d",result);

    return 0;
}