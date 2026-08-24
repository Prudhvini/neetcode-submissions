class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()) return false;
        Map<Character,Integer> map1 = new HashMap<>();
        Map<Character,Integer> map2 = new HashMap<>();
        for(char c:s.toCharArray()){
            if(map1.containsKey(c)){
                map1.put(c,map1.get(c)+1);
            }
            else{
                map1.put(c,1);
            }
        }
        for(char c:t.toCharArray()){
            if(map2.containsKey(c)){
                map2.put(c,map2.get(c)+1);
            }
            else{
                map2.put(c,1);
            }
        }

        for(Map.Entry<Character,Integer> e:map1.entrySet()){
            if(!map2.containsKey(e.getKey()) || map2.get(e.getKey())!=e.getValue())
                return false;
        }

        return true;
    }
}
