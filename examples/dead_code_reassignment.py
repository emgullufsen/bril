import json
import sys
from form_blocks import form_blocks, print_blocks
from dead_code import until_convergence

def dead_code_reassignment(bril):
    changed = False
    funcs = bril['functions']
    for func in funcs:
        for block in form_blocks(func['instrs']):
            last_def = {}
            for instr in block:
                # check for uses
                try:
                    for arg in instr['args']:
                        if arg in last_def:
                            del last_def[arg]
                except:
                    pass

                try:
                    if instr['dest'] in last_def:
                        func['instrs'].remove(last_def[instr['dest']])
                        changed = True
                    last_def[instr['dest']] = instr
                except:
                    continue
    return changed

if __name__ == '__main__':
    jl = json.load(sys.stdin)
    until_convergence(jl, dead_code_reassignment)
    print(json.dumps(jl))
