import json
import sys
from form_blocks import form_blocks, print_blocks

def dead_code_unused_naive(bril):
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
                    func['instrs'].remove(instr)
            except KeyError:
                continue
    print(json.dumps(bril))

if __name__ == '__main__':
    dead_code_unused_naive(json.load(sys.stdin))
