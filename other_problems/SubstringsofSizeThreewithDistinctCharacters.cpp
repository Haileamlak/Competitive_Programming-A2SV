/*
A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
 */

class Solution {
public:
    int countGoodSubstrings(string s) {
        int sz = s.size();
        if(sz < 3)
            return 0;

        int count = 0;
    
        for (int i = 0; i <= sz - 3; i++) {

            if (isUnique(s.substr(i,  3))) {
                count++;
            }
        }
        return count;
    }

    bool isUnique(string str)
    {
        set<char> strMap;

        strMap.insert(str[0]);        
        strMap.insert(str[1]);
        strMap.insert(str[2]);

        return strMap.size() == 3;
    }
};
