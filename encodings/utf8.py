def up_to(number: int, up: int) -> str:
    b: str = bin(number)[2:]
    needed: str = "0" * (up - len(b))
    return needed + b


def convert_to(str1: str, str2: str) -> int:
    return int(str1 + str2, 2)


def encode(inp: str) -> list:
    result: list = []

    for sym in inp:
        code_point: int = ord(sym)

        if 0x00 <= code_point <= 0x7f:
            b: str = up_to(code_point, 7)
            first: int = convert_to("0", b)
            result.append(first)
        elif 0x80 <= code_point <= 0x7ff:
            b: str = up_to(code_point, 11)
            first: int = convert_to("110", b[:5])
            second: int = convert_to("10", b[5:])
            result.append(first)
            result.append(second)
        elif 0x800 <= code_point <= 0xffff:
            b: str = up_to(code_point, 16)
            first: int = convert_to("1110", b[:4])
            second: int = convert_to("10", b[4:10])
            third: int = convert_to("10", b[10:])
            result.append(first)
            result.append(second)
            result.append(third)
        elif 0x10000 <= code_point <= 0x10ffff:
            b: str = up_to(code_point, 21)
            first: int = convert_to("11110", b[:3])
            second: int = convert_to("10", b[3:9])
            third: int = convert_to("10", b[9:15])
            fourth: int = convert_to("10", b[15:])
            result.append(first)
            result.append(second)
            result.append(third)
            result.append(fourth)

    return result


def decode(numbers: list) -> str:
    result: list = []
    i: int = 0

    while i < len(numbers):
        byte: int = numbers[i]
        binary: str = up_to(byte, 8)

        if binary[0] == "0":
            ordinary: int = int(binary[1:], 2)
            result.append(chr(ordinary))
            i += 1
            continue
        elif binary[:3] == "110":
            nxt: int = numbers[i + 1]
            nxt_binary: str = up_to(nxt, 8)
            ordinary: int = int(binary[3:] + nxt_binary[2:], 2)
            result.append(chr(ordinary))
            i += 2
            continue
        elif binary[:4] == "1110":
            nxt: int = numbers[i + 1]
            nxt_binary: str = up_to(nxt, 8)

            nxt_nxt: int = numbers[i + 2]
            nxt_nxt_binary: str = up_to(nxt_nxt, 8)

            ordinary: int = int(binary[4:] + nxt_binary[2:] + nxt_nxt_binary[2:], 2)
            result.append(chr(ordinary))
            i += 3
            continue
        elif binary[:5] == "11110":
            nxt: int = numbers[i + 1]
            nxt_binary: str = up_to(nxt, 8)

            nxt_nxt: int = numbers[i + 2]
            nxt_nxt_binary: str = up_to(nxt_nxt, 8)

            nxt_nxt_nxt: int = numbers[i + 3]
            nxt_nxt_nxt_binary: str = up_to(nxt_nxt_nxt, 8)

            ordinary: int = int(binary[5:] + nxt_binary[2:] + nxt_nxt_binary[2:] + nxt_nxt_nxt_binary[2:], 2)
            result.append(chr(ordinary))
            i += 4
            continue

    return "".join(result)
