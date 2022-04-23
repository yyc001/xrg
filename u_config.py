CM_CAPACITY = 0x40

U_INS_ACTIONS = [
    {
        "name": "取指",
        "uaddr": 0x00,
        "actions": [
            {
                "read": "pc",
                "write": "mar"
            }, {
                "read": "pc",
                "write": "spa"
            }, {
                "read": "acc",
                "write": "pc",
                "alu": "a+1",
            }, {
                "read": "ram",
                "write": "ir",
                "jmp": "if"
            },
        ]
    }, {
        "name": "取立即数",
        "uaddr": 0x05,
        "actions": [
            {
                "read": "pc",
                "write": "mar"
            }, {
                "read": "pc",
                "write": "spa"
            }, {
                "read": "acc",
                "write": "pc",
                "alu": "a+1",
            }, {
                "read": "ram",
                "write": "imm",
                "jmp": "force"
            },
        ]
    }, {
        "name": "SLLV",
        "uaddr": 0X0A,
        "actions": [
            {
                "read": "r3",
                "write": "spa"
            }, {
                "read": "r2",
                "write": "spb"
            }, {
                "read": "sh",
                "write": "r1",
                "sh": "left",
                "jmp": "0"
            }
        ]
    }, {
        "name": "SRLV",
        "uaddr": 0X0D,
        "actions": [
            {
                "read": "r3",
                "write": "spa"
            }, {
                "read": "r2",
                "write": "spb"
            }, {
                "read": "sh",
                "write": "r1",
                "sh": "right",
                "jmp": "0"
            }
        ]
    }, {
        "name": "SLTU",
        "uaddr": 0x10,
        "actions": [
            {
                "read": "r3",
                "write": "spb"
            }, {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "cmp",
                "write": "r1",
                "cmp": "a<b",
                "jmp": "0"
            }
        ]
    }, {
        "name": "ADDU",
        "uaddr": 0x13,
        "actions": [
            {
                "read": "r3",
                "write": "spb"
            }, {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "acc",
                "write": "r1",
                "alu": "a+b",
                "jmp": "0"
            }
        ]
    }, {
        "name": "SUBU",
        "uaddr": 0x16,
        "actions": [
            {
                "read": "r3",
                "write": "spb"
            }, {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "acc",
                "write": "r1",
                "alu": "a-b",
                "jmp": "0"
            }
        ]
    }, {
        "name": "AND",
        "uaddr": 0x19,
        "actions": [
            {
                "read": "r3",
                "write": "spb"
            }, {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "acc",
                "write": "r1",
                "alu": "a&b",
                "jmp": "0"
            }
        ]
    }, {
        "name": "OR",
        "uaddr": 0X1C,
        "actions": [
            {
                "read": "r3",
                "write": "spb"
            }, {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "acc",
                "write": "r1",
                "alu": "a|b",
                "jmp": "0"
            }
        ]
    }, {
        "name": "XOR",
        "uaddr": 0x1F,
        "actions": [
            {
                "read": "r3",
                "write": "spb"
            }, {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "acc",
                "write": "r1",
                "alu": "a^b",
                "jmp": "0"
            }
        ]
    }, {
        "name": "XNOR",
        "uaddr": 0x22,
        "actions": [
            {
                "read": "r3",
                "write": "spb"
            }, {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "acc",
                "write": "r1",
                "alu": "a xnor b",
                "jmp": "0"
            }
        ]
    }, {
        "name": "JZ",
        "uaddr": 0x25,
        "actions": [
            {
                "read": "r3",
                "write": "spc"
            }, {
                "read": "r2",
                "write": "spa"
            }, {
                "read": "r1",
                "write": "spb"
            }, {
                "read": "se",
                "write": "pc",
                "se": "=0",
                "jmp": "0"
            }
        ]
    }, {
        "name": "LD",
        "uaddr": 0x29,
        "actions": [
            {
                "read": "r3",
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
        "uaddr": 0x2C,
        "actions": [
            {
                "read": "r2",
                "write": "mar"
            }, {
                "read": "r3",
                "write": "ram",
            }, {
                "jmp": "0"
            }
        ]
    },
]

U_BUS = [
    "jmp",  # [22, 23]
    "se",  # [20, 21],
    "cmp",  # [18, 19],
    "sh",  # [16, 17],
    "0s", # [14, 15]
    "alu",  # [8, 13],
    "write",  # [4, 7],
    "read",  # [0, 3],
]

REG_ID = {
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
    "acc": "1011",
    "cmp": "1100",
    "sh": "1101",
    "se": "1110",
    "ram": "1111",
}

U_CODES = {
    "alu": {
        # CN S3 S2 S1 S0 M
        "none": "000000",
        "a+1": "000000",
        "a+b": "110010",
        "a-b": "001100",
        "a&b": "010111",
        "a|b": "011101",
        "a^b": "001101",
        "a xnor b": "010011",
    },
    "sh": {
        "none": "00",
        "left": "01",
        "right": "00"
    },
    "cmp": {
        "none": "00",
        "a<b": "01",
        "a<=b": "11",
        "a=b": "10"
    },
    "se": {
        "none": "00",
        "=0": "00"
    },
    "jmp": {
        "none": "00",
        "if": "01",
        "force": "10",
        "0": "11"
    },
    "read": REG_ID,
    "write": REG_ID,
    "0s": {
        "none": "00"
    }
}

