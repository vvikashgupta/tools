class Solution:
# If astroide is same size and opposite directions, clear them
# Same direction astroide does not collide
# Smaller astroide gets finished.
#Input [5,10,-5], [10,2,-5]
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for num in asteroids:
            if not result:
                result.append(num)
            else:
                if num > 0 and result[-1] > 0:
                    #Both moving in the same direction
                    result.append(num)
                elif num < 0 and result[-1] < 0:
                    result.append(num)
                else:
                    while result:
                        if abs(num) > abs(result[-1]):
                            result.pop()
                            continue
                            #result.append(num)
                            
                        elif abs(num) < abs(result[-1]):
                            # No need to do anything , since new element is smaller in size
                            break
                        elif abs(num) == abs(result[-1]):
                            #They both are of same size.
                            result.pop()
                            break
        return result
