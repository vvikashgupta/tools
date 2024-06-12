class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        psum = [0]
        for num in gain:
            psum.append(psum[-1]+num)
        return max(psum)
