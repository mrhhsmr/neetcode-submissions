class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;
        int[] map = new int [26];
        for ( int i = 0 ; i < s1.length() ; i++){
            map[s1.charAt(i) - 'a']++;
        }

        int[] s2map = new int [26];
        int start = 0 , end = 0;
        while(end < s2.length()){
            s2map[s2.charAt(end) - 'a']++;
            if(end - start + 1 == s1.length()){
                if(isPermutation(map, s2map)){
                    return true;
                }
                s2map[s2.charAt(start) - 'a']--;
                start++;
            }
            
            end++;
        }

        return false;
    }

    private boolean isPermutation(int[] map, int[] s2map){
        for(int i = 0 ; i < 26; i++){
            if(map[i] != s2map[i]){
                return false;
            }
        }

        return true;
    }
}
