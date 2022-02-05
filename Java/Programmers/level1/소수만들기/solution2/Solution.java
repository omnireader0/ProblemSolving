package Java.Programmers.level1.소수만들기.solution2;

public class Solution {
    public int solution(int[] nums) {
        int count = 0;
        for(int i=0; i<nums.length; i++){
            for(int j=i+1; j<nums.length; j++){
                for(int k=j+1; k<nums.length; k++){
                    int sum = nums[i]+nums[j]+nums[k];
                    if(isPrime(sum))
                        count++;
                }
            }
        }
        return count;
    }
    private boolean isPrime(int n){
        int sqrtN = (int)Math.sqrt(n)+1;
        for(int i=2; i<sqrtN; i++){
            if(n%i == 0)
                return false;
        }
        return true;
    }
}