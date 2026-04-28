class KthLargest {
    PriorityQueue<Integer> minQ;
    int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.minQ = new PriorityQueue<Integer>();
        for(int num : nums){
             this.minQ.offer(num);
        }
    }
    
    public int add(int val) {
        this.minQ.offer(val);
        while(this.minQ.size() > this.k){
            this.minQ.poll();
        }
        
        return this.minQ.peek();
    }
}
