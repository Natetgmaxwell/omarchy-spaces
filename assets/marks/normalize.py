"""Re-serialises an SVG path with every number separated.

Simple Icons ships minified paths where arc flags run into the next number
("a1 1 0 01.5 2"). Qt's PathSvg misreads those and draws garbage, so every
path in Marks.js goes through this first.
"""
import re

NUM = re.compile(r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")
ARGS = {"m": 2, "l": 2, "h": 1, "v": 1, "c": 6, "s": 4, "q": 4, "t": 2, "a": 7, "z": 0}


def normalize(d):
    out, i, cmd, n = [], 0, None, 0
    while i < len(d):
        ch = d[i]
        if ch.isalpha():
            cmd, n = ch, 0
            out.append(ch)
            i += 1
            continue
        if ch in " ,\t\n":
            i += 1
            continue
        # Arc flags (args 4 and 5 of each 7) are single digits, never longer.
        if cmd and cmd.lower() == "a" and n % 7 in (3, 4):
            out.append(ch)
            i += 1
        else:
            m = NUM.match(d, i)
            if not m:
                raise ValueError("bad path near %r" % d[i:i + 20])
            out.append(m.group(0))
            i = m.end()
        n += 1
    return " ".join(out)


if __name__ == "__main__":
    import sys
    print(normalize(sys.stdin.read().strip()))
