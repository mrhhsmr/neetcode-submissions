class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        if (n == 0){
            return res;
        }
        Set<String> set = new HashSet<>();
        dfs("", n, n, set);
        for(var str : set){
            res.add(str);
        }
        return res;
    }

    private void dfs( String str, int left, int right, Set<String> set){
        if(left == 0 && right == 0){
            set.add(str);
            return;
        }

        if(left > 0){
            dfs(str + "(", left -1 ,right, set);
        }
        
        if (right > left){
            dfs(str + ")", left , right -1 , set);
        }
    }
}
