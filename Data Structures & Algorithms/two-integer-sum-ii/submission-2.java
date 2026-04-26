class Solution {
    public int[] twoSum(int[] numbers, int target) {
        var output = new int [2];
        int i = 0, j = numbers.length - 1;
        while ( i < j ){
            if (numbers[i] + numbers[j] == target){
                output[0] = i + 1;
                output[1] = j + 1;
                return output;
            }
            else if (numbers[i] + numbers[j] < target){
                i++;
            }
            else{
                j--;
            }
        }

        return output;
    }
}
