class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create a hashmap of the position and the speed
        # sort the position array
        # create a new array with how many iterations it takes for it to reach the end goal
        #iterate through the sorted position array
            #we can pop from the stack and make a while loop, while stack
            # pop a value, if the popped value is greater than the top of the stack, then fleet += 1
            # if not, continue, then at the end just add 1 to the fleet because if it catches up to the 1st position its its own fleet
            #return fleet.

        map = {}
        stack = []
        sorted_pos = sorted(position, reverse = True)
        for idx in range(len(position)):
            map[position[idx]] = speed[idx]
        for i in sorted_pos:
            iter = (target - i) / map[i]
            if not stack or iter > stack[-1]:
                stack.append(iter)
        return len(stack)

