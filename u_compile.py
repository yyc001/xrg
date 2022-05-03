import sys

from u_config import U_INS_ACTIONS, CM_CAPACITY, U_BUS_CODES, U_CODES

output_arr = [0] * CM_CAPACITY
OP_CODES = {}
INS_OP_NUMS = {}
naddr = 0

for instruction in U_INS_ACTIONS:
    if "uaddr" in instruction:
        naddr = instruction["uaddr"]
    OP_CODES[instruction['name']] = naddr
    INS_OP_NUMS[instruction['name']] = instruction['operand']
    for action in instruction["actions"]:
        print(naddr, instruction['name'])
        if output_arr[naddr] != 0:
            print("Conflict address: {}".format(naddr), file=sys.stderr)
            exit(1)
        tmp = ""
        for item in U_BUS_CODES:
            if item not in U_CODES:
                print("Lack info: {}".format(item), file=sys.stderr)
                exit(0)
            # print("[")
            # print(item, U_CODES[item])
            # print(action[item] if item in action else "none")
            # print("]")
            tmp += U_CODES[item][action[item]] if item in action else U_CODES[item]["none"]

        assert naddr < CM_CAPACITY - 1
        output_arr[naddr] = tmp
        naddr += 1

with open("CM0.mif", "w") as f:
    f.write("""WIDTH=24;
DEPTH=256;

ADDRESS_RADIX=UNS;
DATA_RADIX=BIN;
    
CONTENT BEGIN
""")
    for idx in range(len(output_arr)):
        f.write("    {}   :   {};\n".format(idx, output_arr[idx]))
    f.write("END;")

print("Compile CM completed.")
