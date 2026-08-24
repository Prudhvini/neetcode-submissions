class Solution {
    public int[] twoSum(int[] nums, int target) {
        if(nums.length<=1) return new int[2];
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        int[] result = new int[2];
        for(int i=0;i<nums.length;i++){
            int diff=target-nums[i];
            if(map.containsKey(diff)){
                return new int[]{map.get(diff), i};
            };
            map.put(nums[i],i);
        }

        return new int[2];
    }
}
