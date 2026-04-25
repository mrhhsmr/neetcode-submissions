class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        var map = new HashMap<Integer, Integer>();
        for(int i = 0 ; i < nums.length ; i++){
            map.put(nums[i] ,map.getOrDefault(nums[i] , 0) + 1);
        }

        List<Integer>[] bucket = new List[nums.length + 1];
        for(var entry : map.entrySet()){
            var key = entry.getKey();
            var value = entry.getValue();
            if (bucket[value] == null) bucket[value] = new ArrayList<>();
            bucket[value].add(key);
        }

        
        int j = bucket.length - 1;
        var res = new int [k];
        int index = 0;
        while (index < k) {
            while(j >= 0 && bucket[j] == null ){
                j--;
            }
            for (int num : bucket[j]) {
                if (index < k) res[index++] = num;
            }
            j--;
        }
        return res;
    }
}
