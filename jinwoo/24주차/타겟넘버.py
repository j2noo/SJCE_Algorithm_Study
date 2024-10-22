class Solution {
    int[] buhos = new int[30];
    int N;
    int answer = 0;
    int gTarget;
     public void recur(int depth, int[] numbers){
        if(depth == N){
            int sum=0;
            for(int i=0; i< N; i++){
                // System.out.print(buhos[i]);
                sum = sum + numbers[i]*buhos[i];
            }
            if(sum==gTarget)
                answer++;
            
            return;
        }
        buhos[depth] = 1;
        recur(depth+1,numbers);
        buhos[depth] = -1;
        recur(depth+1,numbers);
        buhos[depth] = 0;
        return;
    }
    
    public int solution(int[] numbers, int target) {
        gTarget = target;
        N = numbers.length;
        recur(0,numbers);
        return answer;
    }
}

// 2^20 = 100만. 완탐.