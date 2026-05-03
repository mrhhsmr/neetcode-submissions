class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] count = new int [26];
        for(int i = 0 ; i < tasks.length ; i++){
            count[tasks[i] - 'A']++;
        }

        var pq = new PriorityQueue<Integer>((a, b) -> (b - a));
        for (int ct : count){
            if (ct > 0){
                pq.offer(ct);
            }
        }

        int time = 0;

        while(!pq.isEmpty()){
            List<Integer> temp = new ArrayList<>();
            int cycle = n + 1;

            while(!pq.isEmpty() && cycle > 0){
                int currTask = pq.poll();
                if(currTask > 1){
                    temp.add(currTask - 1);
                }
                cycle--;
                time++;
            }

            for(int nextTask : temp){
                pq.offer(nextTask);
            }

            //还没执行完，但是必须把空的cycle加上去
            if (!pq.isEmpty()) {
                time += cycle;
            }
        }

        
        return time;
    }
}
