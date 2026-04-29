class Solution {
    public int characterReplacement(String s, int k) {
        int len = s.length();
        if(len == 0){
            return 0;
        }
        int[] count = new int[26];
        int res = 1, start = 0, maxCount = 0;
        for(int end = 0 ; end < len ; end ++){
            count[s.charAt(end)  - 'A']++;
            maxCount = Math.max(maxCount, count[s.charAt(end)  - 'A']);

            while (maxCount + k < end - start + 1){
                count[s.charAt(start) - 'A']--;
                start++;
            }

            res = Math.max(res, end - start + 1);
        }
        
        return res;
    }
}
