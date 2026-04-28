/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {
        intervals.sort((a, b) -> (a.start == b.start? a.end - b.end : a.start - b.start));
        for(int i = 1; i < intervals.size() ; i++){
            var prev = intervals.get(i - 1);
            var curr = intervals.get(i);
            if (prev.end > curr.start){
                return false;
            }
        }

        return true;
    }
}
