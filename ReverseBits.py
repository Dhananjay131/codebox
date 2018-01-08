class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        """bins = bin(n)[2:]
        bins = bins[::-1]
        rev = bins + "0"*(32-len(bins))
        return int(rev, 2)"""
        
        return int(bin(n)[2:].zfill(32)[::-1], 2)   # ending ,2 -> bole to bit manipulation. power 2, bin to int
