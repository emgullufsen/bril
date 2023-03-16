import json
import sys
from form_blocks import form_blocks, print_blocks
from copy import deepcopy

def dead_code_unused_naive(bril):
    changed = False
    funcs = bril['functions']
    for func in funcs:
        used = set()
        for instr in func['instrs']:
            try:
                for a in instr['args']:
                    used.add(a)
            except KeyError:
                continue
        
        for instr in func ['instrs']:
            try:
                if instr['dest'] not in used:
                    changed = True
                    func['instrs'].remove(instr)
            except KeyError:
                continue
    return changed

def until_convergence(bril1, func):
    res = func(bril1)
    if not res:
        return
    else:
        until_convergence(bril1, func)

if __name__ == '__main__':
    jl = json.load(sys.stdin)
    until_convergence(jl, dead_code_unused_naive)
    print(json.dumps(jl))
