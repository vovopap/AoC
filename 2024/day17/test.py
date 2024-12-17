import re

a, b, c, *prog = map(int, re.findall(r'\d+', 
                     open('in.txt').read()))

def run(a, b, c):
    i, R = 0, []

    while i in range(len(prog)):
        C = {0:0,1:1,2:2,3:3,4:a,5:b,6:c}

        match prog[i], prog[i+1]:
            case 0, op: a = a >> C[op]
            case 1, op: b = b ^ op
            case 2, op: b = 7 & C[op]
            case 3, op: i = op-2 if a else i
            case 4, __: b = b ^ c
            case 5, op: R = R + [C[op] & 7]
            case 6, op: b = a >> C[op]
            case 7, op: c = a >> C[op]
        i += 2
    return R

print(*run(a, b, c), sep=',')


todo = [(1, 0)]
for i, a in todo:
    for a in range(a, a+8):
        if run(a, 0, 0) == prog[-i:]:
            todo += [(i+1, a*8)]
            if i == len(prog): print(a)