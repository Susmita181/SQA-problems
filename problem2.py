def w_match(t, p):
    if not p:
        return not t

    if p[0] == '*':
        
        return (w_match(t, p[1:]) or
                (t and w_match(t[1:], p)))

    
    if t and (p[0] == '?' or p[0] == t[0]):
        return w_match(t[1:], p[1:])


    return False


t = input("Enter text: ")
p = input("Enter pattern: ")

if w_match(t, p):
    print(" Pattern matches.")
else:
    print(" Pattern does not match.")
