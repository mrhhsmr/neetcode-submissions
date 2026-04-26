class Solution {
    public int lengthOfLongestSubstring(String s) {
        var set = new HashSet<Character>();
        int i = 0;
        int j = 0;
        int res = 0;
        while (i < s.length()){
            while(j < s.length() && !set.contains(s.charAt(j))){
                set.add(s.charAt(j));
                j++;
            }
            res = Math.max(res, j - i);
            set.remove(s.charAt(i));
            i++;
        }

        return res;
    }
}
