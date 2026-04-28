class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> res = new ArrayList<>();
        Arrays.sort(intervals, (a, b) -> (a[0] == b[0] ? a[1] - b[1] : a[0] - b [0]));
        if (intervals.length == 0){
            return res.toArray(new int[res.size()][]);
        }

        var prev = intervals[0];
        for(int i = 1; i < intervals.length ; i++){
            if(intervals[i][0] > prev[1]){
                res.add(prev);
                prev = intervals[i];
            }
            else{
                prev[1] = intervals[i][1] >  prev[1] ? intervals[i][1]: prev[1];
            }
        }
        res.add(prev);

        return res.toArray(new int[res.size()][]);
    }
}
