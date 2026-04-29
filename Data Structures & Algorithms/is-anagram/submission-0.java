class Solution {
    public boolean isAnagram(String s, String t) {
        if(s == null || t == null || s.length() != t.length()){
            return false;
        }

        int [] setA = new int[26];
        int [] setB = new int[26];
        for(int i = 0 ; i < s.length(); i ++){
            setA[s.charAt(i) - 'a']++;
        }

        for(int i = 0 ; i < t.length(); i ++){
            setB[t.charAt(i) - 'a']++;
        }

        for(int i = 0 ; i < 26; i ++){
            if(setA[i] != setB[i]){
                return false;
            }
        }

        return true;
    }
}
