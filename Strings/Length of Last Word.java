# https://leetcode.com/problems/length-of-last-word/post-solution/4174572/

public class Solution 
{
    public int lengthOfLastWord(String s) 
    {
        int length = 0;
        for (int i = s.length() - 1; i >= 0; i--) 
        {
            if (s.charAt(i) != ' ') 
                length++;
            else if (length > 0)
                break;
        }
        return length;
    }
}
