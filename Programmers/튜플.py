import re
def solution(s):
    ans = []
    s = s.lstrip('{').rstrip('}').split(',{')
    s.sort(key=len)
    for i in range(len(s)):
        s[i] = list(map(int,re.findall("\d+",s[i])))
        
    mask = set(map(int,s[-1]))
    
    for match_text in s:
        for x in match_text:
            if int(x) in mask:
                int_x = int(x)
                ans.append(int_x)
                mask.remove(int_x)
                
    return ans