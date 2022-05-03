import re
import sys
from u_compile import OP_CODES, INS_OP_NUMS
from i_config import REG_FL

symbols = {}
instructions = []


def isNum(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


with open("test2.s", encoding="utf-8") as f:
    line_id = 0
    bin_ad = 0
    for line in f.readlines():
        # print(line, "bin=", bin_ad)
        line_id += 1
        valid = line.strip().split(";")[0]

        if len(valid) == 0:
            continue

        tokens = re.split(",\s*|\s+", valid)

        if len(tokens) == 1:
            token = tokens[0]
            if token[0] == ".":
                symbols[token] = bin_ad
                continue
            elif isNum(token):
                instructions.append({
                    'type': "raw",
                    'line': line_id,
                    'bin': bin_ad,
                    'content': "{:016b}".format(int(token))
                })
                bin_ad += 1
                continue
        imme = 0
        for token in tokens:
            if token[0] == '.' or isNum(token):
                if imme:
                    print("ERROR on line {}: Cannot give more than 1 immediate.".format(line_id), file=sys.stderr)
                    exit(1)
                imme = 1

        instructions.append({
            'type': "instruction",
            'line': line_id,
            'bin': bin_ad,
            'tokens': tokens
        })
        bin_ad += 1 + imme

with open("test2.mif", "w") as f:
    f.write("""WIDTH=16;
DEPTH=256;

ADDRESS_RADIX=UNS;
DATA_RADIX=BIN;

CONTENT BEGIN
""")
    for instruction in instructions:
        print(instruction)
        if instruction['type'] == "raw":
            f.write("    {} :  {};\n".format(instruction['bin'], instruction['content']))
        elif instruction['type'] == "instruction":
            tmp = ""
            imm = 0
            opname = instruction['tokens'][0]
            opcode = OP_CODES[opname]
            opand = INS_OP_NUMS[opname]
            tmp += "{:07b}".format(opcode)
            for i in range(1, 4):
                if i > opand:
                    tmp += "000"
                    continue
                token = instruction['tokens'][i]
                if isNum(token):
                    imm = (int(token) + 2**16) % 2**16
                    tmp += "111"
                elif token[0] == '.':
                    imm = symbols[token]
                    tmp += "111"
                else:
                    tmp += REG_FL[token]
            f.write("    {} :  {};\n".format(instruction['bin'], tmp))
            if imm:
                f.write("    {} :  {:016b};\n".format(instruction['bin'] + 1, imm))

    f.write("END;")

print(symbols)
print("Compile RAM Completed.")
