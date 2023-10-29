# https://leetcode.com/problems/power-of-three/

var isPowerOfThree = n => 3**parseInt(Math.log(n)/Math.log(3)) == n
