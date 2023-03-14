import json
import sys
from form_blocks import form_blocks, print_blocks

def count_blocks(bril):
    """Given sequence of lists of instructions (basic blocks), 
       count total instructions / bbs"""
    total_instrs = 0
    total_bbs = 0
    funcs = bril['functions']
    for func in funcs:
        for block in form_blocks(func['instrs']):
            total_bbs += 1
            for instr in block:
                total_instrs += 1
    
    print("basic blocks: {}\ninstructions: {}".format(total_bbs, total_instrs))

if __name__ == '__main__':
    count_blocks(json.load(sys.stdin))
