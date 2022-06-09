def romanToInt(s):
    d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    for i in range (len(s)):
        n = d[s[i]]
        if i+1 <len(s):
            if n<d[s[i+1]]:
                result = result-n
            else:
                result = result+n
        else:
            result = result+n
    return result


print(romanToInt('MCMXCIV'))
