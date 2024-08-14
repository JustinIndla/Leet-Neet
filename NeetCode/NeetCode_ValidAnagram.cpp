class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> occurence_s;
        for(const char& letter : s){
            if(occurence_s.find(letter) != occurence_s.end()){
                occurence_s[letter]++;
            } else {
                occurence_s[letter] = 1;
            }
        }

        map<char, int> occurence_t;
        for(const char& letter : t){
            if(occurence_t.find(letter) != occurence_t.end()){
                occurence_t[letter]++;
            } else {
                occurence_t[letter] = 1;
            }
        }

        return(occurence_s == occurence_t);
    }
};
