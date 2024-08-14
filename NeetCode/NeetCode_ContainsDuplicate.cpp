class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> traversed;
        for(const int& num : nums){
            if(traversed.find(num) != traversed.end()){
                return true;
            } else {
                traversed.insert(num);
            }
        }
        return false;
    }
};