def isBalanced(s):
    combos = ["[]", "{}", "()"]
    while len(s) > 0:
        new_s = s
        for c in combos:
            new_s = new_s.replace(c, "")
        if len(new_s) == len(s):
            return "NO"
        s = new_s
    return "YES"
if __name__ == '__main__':
    t = int(input().strip())   
    for _ in range(t):
        s = input().strip()    
        print(isBalanced(s))
