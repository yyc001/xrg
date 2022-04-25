CM_CAPACITY_BITS = 7
CM_CAPACITY = 2 ** CM_CAPACITY_BITS

U_INS_ACTIONS = [
    {
        "name": "取指",
        "uaddr": 0,
        "operand": 0,
        "actions": [
            {
                "read": "pc",
                "write": "mar"
            }, {
                "read": "pc",
                "write": "spa"
            }, {
                "read": "alu_l",
                "write": "pc",
                "alu_op": "a+1",
                "alu_ena": "add"
            }, {
                "read": "ram",
                "write": "ir",
                "jmp": "if"
            }, {
                "read": "pc",
                "write": "mar"
            }, {
                "read": "pc",
                "write": "spa"
            }, {
                "read": "alu_l",
                "write": "pc",
                "alu_op": "a+1",
                "alu_ena": "add"
            }, {
                "read": "ram",
                "write": "imm",
                "jmp": "force"
            },
        ]
    }, {
        "name": "SLLV",
        "operand": 3,
        "actions": [
            {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "r3",
                "write": "spb"
            }, {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "sh_left",
                "alu_ena": "sh",
                "jmp": "0"
            }
        ]
    }, {
        "name": "SLLV.i",
        "operand": 1,
        "actions": [
            {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "sh_left",
                "alu_ena": "sh",
                "jmp": "0"
            }
        ]
    }, {
        "name": "SRLV",
        "operand": 3,
        "actions": [
            {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "r3",
                "write": "spb"
            }, {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "sh_right",
                "alu_ena": "sh",
                "jmp": "0"
            }
        ]
    }, {
        "name": "SRLV.i",
        "operand": 1,
        "actions": [
            {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "sh_right",
                "alu_ena": "sh",
                "jmp": "0"
            }
        ]
    }, {
        "name": "SLTU",
        "operand": 3,
        "actions": [
            {
                "read": "r3",
                "write": "spb"
            }, {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "a<b",
                "alu_ena": "cmp",
                "jmp": "0"
            }
        ]
    }, {
        "name": "SLTU.i",
        "operand": 1,
        "actions": [
            {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "a<b",
                "alu_ena": "cmp",
                "jmp": "0"
            }
        ]
    }, {
        "name": "ADD",
        "operand": 3,
        "actions": [
            {
                "read": "r3",
                "write": "spb"
            }, {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "a+b",
                "alu_ena": "add",
                "jmp": "0"
            }
        ]
    }, {
        "name": "ADD.i",
        "operand": 1,
        "actions": [
            {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "a+b",
                "alu_ena": "add",
                "jmp": "0"
            }
        ]
    }, {
        "name": "SUB",
        "operand": 3,
        "actions": [
            {
                "read": "r3",
                "write": "spb"
            }, {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "a-b",
                "alu_ena": "add",
                "jmp": "0"
            }
        ]
    }, {
        "name": "SUB.i",
        "operand": 1,
        "actions": [
            {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "a-b",
                "alu_ena": "add",
                "jmp": "0"
            }
        ]
    }, {
        "name": "AND",
        "operand": 3,
        "actions": [
            {
                "read": "r3",
                "write": "spb"
            }, {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "a&b",
                "alu_ena": "add",
                "jmp": "0"
            }
        ]
    }, {
        "name": "AND.i",
        "operand": 1,
        "actions": [
            {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "a&b",
                "alu_ena": "add",
                "jmp": "0"
            }
        ]
    }, {
        "name": "OR",
        "operand": 3,
        "actions": [
            {
                "read": "r3",
                "write": "spb"
            }, {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "a|b",
                "alu_ena": "add",
                "jmp": "0"
            }
        ]
    }, {
        "name": "OR.i",
        "operand": 1,
        "actions": [
            {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "a|b",
                "alu_ena": "add",
                "jmp": "0"
            }
        ]
    }, {
        "name": "XOR",
        "operand": 3,
        "actions": [
            {
                "read": "r3",
                "write": "spb"
            }, {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "a^b",
                "alu_ena": "add",
                "jmp": "0"
            }
        ]
    }, {
        "name": "XOR.i",
        "operand": 1,
        "actions": [
            {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "a^b",
                "alu_ena": "add",
                "jmp": "0"
            }
        ]
    }, {
        "name": "NXOR",
        "operand": 3,
        "actions": [
            {
                "read": "r3",
                "write": "spb"
            }, {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "a nxor b",
                "alu_ena": "add",
                "jmp": "0"
            }
        ]
    }, {
        "name": "NXOR.i",
        "operand": 1,
        "actions": [
            {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "a nxor b",
                "alu_ena": "add",
                "jmp": "0"
            }
        ]
    }, {
        "name": "JZ",
        "operand": 2,
        "actions": [
            {
                "read": "r1",
                "write": "spc"
            }, {
                "read": "pc",
                "write": "spa"
            }, {
                "read": "r2",
                "write": "spb"
            }, {
                "read": "alu_l",
                "write": "pc",
                "alu_op": "=0",
                "alu_ena": "se",
                "jmp": "0"
            }
        ]
    }, {
        "name": "JZR",
        "operand": 2,
        "actions": [
            {
                "read": "r1",
                "write": "spc"
            }, {
                "read": "pc",
                "write": "spa"
            }, {
                "read": "r2",
                "write": "spb"
            }, {
                "read": "alu_l",
                "write": "spb",
                "alu_op": "a+b",
                "alu_ena": "add",
            }, {
                "read": "alu_l",
                "write": "pc",
                "alu_op": "=0",
                "alu_ena": "se",
                "jmp": "0"
            }
        ]
    }, {
        "name": "JMP",
        "operand": 1,
        "actions": [
            {
                "read": "r1",
                "write": "pc",
                "jmp": "0"
            }
        ]
    }, {
        "name": "JMPR",
        "operand": 1,
        "actions": [
            {
                "read": "pc",
                "write": "spa"
            }, {
                "read": "r1",
                "write": "spb"
            }, {
                "read": "alu_l",
                "write": "pc",
                "alu_op": "a+b",
                "alu_ena": "add",
                "jmp": "0"
            }
        ]
    }, {
        "name": "LD",
        "operand": 2,
        "actions": [
            {
                "read": "r2",
                "write": "mar"
            }, {
                # WAIT
            }, {
                "read": "ram",
                "write": "r1",
                "jmp": "0"
            }
        ]
    }, {
        "name": "STR",
        "operand": 2,
        "actions": [
            {
                "read": "r2",
                "write": "mar"
            }, {
                "read": "r1",
                "write": "ram",
            }, {
                # WAIT
                "jmp": "0"
            }
        ]
    }, {
        "name": "MUL",
        "operand": 3,
        "actions": [
            {
                "read": "r3",
                "write": "spb"
            }, {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "alu_h",
                "write": "spc",
                "alu_op": "a*b",
                "alu_ena": "mul",
            }, {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "a*b",
                "alu_ena": "mul",
                "jmp": "0"
            }
        ]
    }, {
        "name": "DIV",
        "operand": 3,
        "actions": [
            {
                "read": "r3",
                "write": "spb"
            }, {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "alu_h",
                "write": "spc",
                "alu_op": "a/b",
                "alu_ena": "div",
                "jmp": "0"
            }, {
                "read": "alu_l",
                "write": "r1",
                "alu_op": "a/b",
                "alu_ena": "div",
                "jmp": "0"
            }
        ]
    }, {
        "name": "MOV",
        "operand": 2,
        "actions": [
            {
                "read": "r1",
                "write": "r2",
                "jmp": "0"
            }
        ]
    }, {
        "name": "HALT",
        "operand": 0,
        "actions": [
            {
                "G": "1"
            }
        ]
    }, {
        "name": "NOP",
        "operand": 0,
        "actions": [
            {
                # WAIT
                "jmp": "0"
            }
        ]
    }
]

U_BUS_CODES = [
    "jmp",  # 22-23
    "blank",  # 18---21
    "G",  # 17
    "alu_ena",  # 14-16
    "alu_op",  # 8----13
    "write",  # 4--7
    "read",  # 0--3
]

REG_CODES = {
    "none": "0000",
    "r1": "0000",
    "r2": "0001",
    "r3": "0010",
    "pc": "0011",
    "mar": "0100",
    "mdr": "0101",
    "ir": "0110",
    "spa": "0111",
    "spb": "1000",
    "spc": "1001",
    "imm": "1010",
    "alu_l": "1011",
    "alu_h": "1100",
    "ram": "1111",
}

U_CODES = {
    "alu_ena": {
        "none": "000",
        "add": "001",
        "sh": "010",
        "cmp": "011",
        "div": "100",
        "mul": "101",
        "se": "110"
    },
    "alu_op": {
        "none": "000000",
        # add
        # CN S3 S2 S1 S0 M
        "a+1": "000000",
        "a+b": "110010",
        "a-b": "001100",
        "a&b": "010111",
        "a|b": "011101",
        "a^b": "001101",
        "a nxor b": "010011",
        # sh
        "sh_left": "000001",
        "sh_right": "000010",
        # cmp
        "a<b": "000001",
        "a<=b": "000011",
        "a=b": "000010",
        # se
        "=0": "000001",
        # mul
        "a*b": "000010",  # 未用
        # "a*b_l": "000001",
        # div
        "a/b": "000010",  # 未用
        # "a mod b": "000001",
    },
    "jmp": {
        "none": "00",
        "if": "01",
        "force": "10",
        "0": "11"
    },
    "read": REG_CODES,
    "write": REG_CODES,
    "blank": {
        "none": "0000"
    },
    "G": {
        "none": "0",
        "1": "1"
    }
}
