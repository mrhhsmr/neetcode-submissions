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
    public int minMeetingRooms(List<Interval> intervals) {
        intervals.sort((a, b) -> (a.start == b.start? a.end - b.end : a.start - b.start));
        if(intervals.size() == 0){
            return 0;
        }

        PriorityQueue<Integer> allocator = new PriorityQueue<>();
        allocator.add(intervals.get(0).end);
        for(int i = 1; i < intervals.size() ; i++){
            var curr = intervals.get(i);
            if (curr.start >= allocator.peek()){
                allocator.poll();
            }
  
            allocator.add(curr.end);
        }

        return allocator.size();
    }
}
