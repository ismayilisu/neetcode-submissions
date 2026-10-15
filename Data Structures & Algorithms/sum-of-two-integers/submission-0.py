class Solution:
    def getSum(self, a: int, b: int) -> int:
        count = 0
        sumi = 0
        carry = 0

        while count < 32:
            bit_a = (a >> count) & 1
            bit_b = (b >> count) & 1

            # Sum bit = XOR of both bits and incoming carry
            bit_sum = bit_a ^ bit_b ^ carry

            # Put the bit at its original position
            sumi |= bit_sum << count

            # Calculate carry for the next position
            carry = (bit_a & bit_b) | (carry & (bit_a ^ bit_b))

            count += 1

        # Convert 32-bit signed result back to Python integer
        if sumi >= (1 << 31):
            sumi -= (1 << 32)

        return sumi