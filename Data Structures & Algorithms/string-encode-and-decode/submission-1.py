class Solution:
    
    def encode(self, strs: List[str]) -> str:
        x = [len(i) for i in strs]
        s=""
        for i in range(len(strs)):
            s=s+(str(len(strs[i])) +"#"+strs[i])
        return s
    def decode(self, s: str) -> List[str]:
        sol = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":      # find where the length number ends
                j += 1
            length = int(s[i:j])    # the full number, however many digits
            start = j + 1
            sol.append(s[start:start+length])
            i = start + length      # jump straight past this chunk
        return sol

            
