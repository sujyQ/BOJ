
word = input()

dec = 0

for _, alpha in enumerate(word) :
    alpha = ord(alpha)
    dec += 2
    if alpha >= ord('A') and alpha <= ord('C') :
        dec += 1
    elif alpha >= ord('D') and alpha <= ord('F') :
        dec += 2
    elif alpha >= ord('G') and alpha <= ord('I') :
        dec += 3
    elif alpha >= ord('J') and alpha <= ord('L') :
        dec += 4
    elif alpha >= ord('M') and alpha <= ord('O') :
        dec += 5
    elif alpha >= ord('P') and alpha <= ord('S') :
        dec += 6
    elif alpha >= ord('T') and alpha <= ord('V') :
        dec += 7
    elif alpha >= ord('W') and alpha <= ord('Z') :
        dec += 8

print(dec)
