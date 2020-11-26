class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []

        def VALID(ip, left, x):
            if x > 4:
                return
            elif x == 4:
                if left == '':
                    if ip not in answer:
                        answer.append(ip)
                    return
                else:
                    return
            elif x < 4 and left == "":
                return
            if left[0] == '0':
                if x == 3:
                    VALID(ip+'0', left[1:], x+1)
                else:
                    VALID(ip+'0.', left[1:], x+1)

            else:
                if x == 3:
                    VALID(ip+left[:1], left[1:], x+1)
                    VALID(ip+left[:2], left[2:], x+1)
                    if int(left[:3]) <= 255:
                        VALID(ip+left[:3], left[3:], x+1)
                else:
                    VALID(ip+left[:1]+'.', left[1:], x+1)
                    VALID(ip+left[:2]+'.', left[2:], x+1)
                    if int(left[:3]) <= 255:
                        VALID(ip+left[:3]+'.', left[3:], x+1)

        VALID('', s, 0)
        return answer
