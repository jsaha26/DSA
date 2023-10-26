// https://leetcode.com/problems/intersection-of-two-arrays/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */

var intersection = function(nums1, nums2) 
{
    const set = new Set(nums1);
    const res = new Set();
    for (const num of nums2) 
        if (set.has(num)) 
            res.add(num);
    return [...res];
};
