import re
import sys

symbols = {}
instructions = []


with open("source.s") as f:
    line_id = 0
    bin_ad = 0
    for line in f.readlines():
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
            elif token.isdigit():
                instructions.append({
                    'type': "raw",
                    'line': line_id,
                    'content': "{:016b}".format(int(token))
                })
            else:
                print("ERROR on line {}: Syntax error.".format(line_id), file=sys.stderr)
                exit(1)
        else:
            imme = 0
            for token in tokens:
                if token[0] == '.' or token.isdigit():
                    if imme:
                        print("ERROR on line {}: Cannot give more than 1 immediate.".format(line_id), file=sys.stderr)
                        exit(1)
                    imme = 1

            if imme:
                bin_ad += 1
            instructions.append({
                'type': "instruction",
                'line': line_id,
                'bin': bin_ad,
                'content': tokens
            })

        bin_ad += 1


with open("ram.mif","w") as f:
    f.write("""WIDTH=16;
DEPTH=256;

ADDRESS_RADIX=UNS;
DATA_RADIX=BIN;

CONTENT BEGIN
""")
    for instruction in instructions:
        if instruction['type'] == "raw":
            f.write("    {} :  {};\n".format())
    f.write("END;")