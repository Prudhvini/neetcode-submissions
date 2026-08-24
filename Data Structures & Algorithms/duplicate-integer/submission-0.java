class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> hashSet = new HashSet<>();
        for(int i=0;i<nums.length;i++){
            if(!hashSet.contains(nums[i])){
                hashSet.add(nums[i]);
            }
            else{
                return true;
            }
        }
        return false;
    }
}
