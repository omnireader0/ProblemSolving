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
    public boolean isPrime(int n){
        for(int i=2; i<Math.sqrt(n)+1; i++){
            if(n%i == 0)
                return false;
        }
        return true;
    }
}