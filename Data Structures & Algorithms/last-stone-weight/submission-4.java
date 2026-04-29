class Solution {
    public int lastStoneWeight(int[] stones) {
        if (stones.length == 0){
            return 0;
        }
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> (b - a));
        for(int i = 0; i < stones.length ;i++){
            pq.offer(stones[i]);
        }
        
        while(pq.size() > 1){
            int stone1 = pq.poll();
            if(pq.isEmpty()){
                return stone1;
            }
            int stone2 = pq.poll();
            if (stone1 > stone2){
                int stone = stone1 - stone2;
                pq.offer(stone);
            }
            else if (stone2 < stone1){
                int stone = stone2 - stone1;
                pq.offer(stone);
            }
        }

        return pq.isEmpty() ? 0 : pq.poll();
    }
}
