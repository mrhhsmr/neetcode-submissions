class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        var res = new ArrayList<List<String>>();
        var map = new HashMap<String, List<String>>();
        if(strs == null || strs.length == 0){
            return res;
        }

        for(var str : strs){
            char[] charArr = str.toCharArray();
            Arrays.sort(charArr);
            var sorted = new String(charArr);
            if(!map.containsKey(sorted)){
                map.put(sorted, new ArrayList<>());
            }

            map.get(sorted).add(str);
        }

        res.addAll(map.values());
        return res;
    }
}
