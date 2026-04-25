class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        var map = new HashMap<Integer, Integer>();
        for(int i = 0 ; i < nums.length ; i++){
            map.put(nums[i] ,map.getOrDefault(nums[i] , 0) + 1);
        }

        List<Integer>[] count = new List[nums.length + 1];
        for(var entry : map.entrySet()){
            var key = entry.getKey();
            var value = entry.getValue();
            if (count[value] == null) count[value] = new ArrayList<>();
            count[value].add(key);
        }

        
        int j = count.length - 1;
        var res = new int [k];
        int index = 0;
        while (index < k) {
            while(j >= 0 && count[j] == null ){
                j--;
            }
            for (int num : count[j]) {
                if (index < k) res[index++] = num;
            }
            j--;
        }
        return res;
    }
}
