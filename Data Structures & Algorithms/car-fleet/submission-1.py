class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        c=sorted(zip(position,speed),reverse=True)
        stack=[]
       
        for p,s in c:
            cnt=(target-p)/s
            if not stack or cnt > stack[-1] :
                stack.append(cnt)
            
        return (len(stack))

        