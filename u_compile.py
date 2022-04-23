import sys

from u_config import U_INS_ACTIONS, CM_CAPACITY, U_BUS, U_CODES

output_arr = [0] * CM_CAPACITY

for instruction in U_INS_ACTIONS:
    naddr = instruction["uaddr"]
    for action in instruction["actions"]:
        if output_arr[naddr] != 0:
            print("Conflict address: {}".format(naddr),file=sys.stderr)
            exit(1)
        tmp = ""
        for item in U_BUS:
            if item not in U_CODES:
                print("Lack info: {}".format(item), file=sys.stderr)
                exit(0)
            tmp += U_CODES[item][action[item]] if item in action else U_CODES[item]["none"]
        output_arr[naddr] = tmp
        naddr += 1

with open("cm.mif","w") as f:
    f.write("""WIDTH=24;
    DEPTH=256;
    
    ADDRESS_RADIX=UNS;
    DATA_RADIX=BIN;
    
    CONTENT BEGIN
    """)
    for idx in range(len(output_arr)):
        f.write("    {}   :   {};\n".format(idx,output_arr[idx]))
    f.write("END;")

print("Compile completed.")