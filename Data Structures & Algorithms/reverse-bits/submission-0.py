class Solution:
    def reverseBits(self, n: int) -> int:
        n = (n << 16 & (0xFFFFFFFF) | (n>> 16))
        n = (n << 8) & (0xFF00FF00) | (n>>8 & (0x00FF00FF) )
        n = (n << 4 & (0xF0F0F0F0) ) | (n>>4 & (0x0F0F0F0F))
        n = (n << 2 & (0xCCCCCCCC) ) | (n>>2 & (0x33333333))
        n = ((n << 1) & 0xAAAAAAAA ) | ((n >> 1) & 0x55555555 )
        return n
 