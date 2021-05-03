class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        res = []
        if numerator*denominator >= 0:
            numerator,denominator = abs(numerator), abs(denominator)
            integer = numerator//denominator
            numerator = (numerator-integer*denominator)*10
        else:
            numerator,denominator = -abs(numerator), abs(denominator)
            integer = numerator//denominator
            if numerator%denominator == 0: 
                numerator = 0
            else:
                integer += 1
                numerator = ((integer*denominator)-numerator)*10
                if integer == 0:
                    integer = '-0'
                    
        
        if numerator==0:
            return str(integer)
        
        d = dict()
        repeat_flag = 0
        i = 0
        
        while numerator>0:
            if numerator in d:
                repeat_flag = 1
                i = d[numerator]
                break
            d[numerator]=i
            i += 1
            
            res.append(str(numerator//denominator))
            numerator = (numerator-(numerator//denominator)*denominator)*10
            
        if integer != '-0':
            integer = str(integer)
            
        if repeat_flag:
            return ''.join([integer,'.']+res[:i]+['(']+res[i:]+[')'])
        else:
            return ''.join([integer,'.']+res)
            
            
            
        
        