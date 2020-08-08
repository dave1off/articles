def encode(s: str) -> list:
    return list(map(ord, s))


def decode(b: list) -> str:
    return "".join(map(chr, b))

