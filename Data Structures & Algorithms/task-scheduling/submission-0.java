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
            int taskCount = 0; // 记录这一轮实际做了几个任务
            //Simulation
            while(cycle > 0 && !pq.isEmpty()){
                int curr = pq.poll();
                if(curr > 1){
                    temp.add(curr - 1);
                }
                cycle --;
                taskCount ++;
                time++;
            }
            //next round
            for(int remain: temp){
                pq.offer(remain);
            }

            if(pq.isEmpty()){
                break;
            }
            time += cycle;
        }

        
        return time;
    }
}
