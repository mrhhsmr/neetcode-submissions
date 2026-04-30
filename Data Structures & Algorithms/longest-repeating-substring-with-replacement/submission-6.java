class Solution {
    public int characterReplacement(String s, int k) {
        int i = 0 , j = 0; 
        int res = 0 ;
        int[] map = new int [26];
        int maxCount = 0;
        while(i < s.length()){
            map[s.charAt(i) - 'A']++;
            maxCount = Math.max(maxCount, map[s.charAt(i) - 'A']);
            while((i- j + 1 ) - maxCount > k){
                map[s.charAt(j) - 'A']--;
                j++; 
            }
            res = Math.max(res, i- j  + 1);
            i++;
        }
        return res;
    }
}
