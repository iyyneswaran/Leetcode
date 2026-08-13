# Optimal approach using monotonic stack. Time complexity: O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        answer = [0] * length
        for i in range(length):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                diff = i - idx
                answer[idx] = diff
            stack.append(i)
        return answer

# using enumerate 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)

        return answer


# Brute force: can pass the basic testcases. Time complexity: O(n^2)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        
        for top in range(length):
            curr = top + 1
            found_warmer = False
            
            while curr < length:
                if temperatures[curr] > temperatures[top]:
                    stack.append(curr - top)
                    found_warmer = True
                    break
                
                curr += 1
            if not found_warmer:
                stack.append(0)
                
        return stack