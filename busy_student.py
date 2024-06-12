class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        result_count = 0 
        for interval in zip(startTime, endTime):
            if interval[0] <= queryTime <= interval[1]:
                result_count += 1
        return result_count
