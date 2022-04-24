from u_config import U_INS_ACTIONS, U_BUS_CODES, U_CODES
from u_compile import OP_CODES, INS_OP_NUMS
with open("u_program.csv", "w", encoding='utf-8') as f:
    f.write("指令,")
    for s in U_BUS_CODES:
        f.write(s + ",")
    f.write("\n")
    for instruction in U_INS_ACTIONS:
        for action in instruction['actions']:
            f.write(instruction["name"] + ",")
            for s in U_BUS_CODES:
                tmp = U_CODES[s][action[s]] if s in action else U_CODES[s]['none']
                f.write("'" + tmp + ",")
            f.write("\n")

print("Generate u_program Completed.")

with open("i_program_table.csv", "w", encoding='utf-8') as f:
    f.write("op,opcode,r1,r2,r3,\n")
    for op,opcode in OP_CODES.items():
        f.write(op + ",'" + "{:07b}".format(opcode) + ",")
        for i in range(3):
            if i >= INS_OP_NUMS[op]:
                f.write("xxx,")
            else:
                f.write("r" + str(i+1) + ",")
        f.write("\n")

print("Generate i_program_table Completed.")