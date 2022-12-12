from collections import defaultdict

def _parse(lines):
    cwd, sizes = "", defaultdict(int)
    for line in lines:
        match line.split():
            case ("$", "cd", "/"):
                cwd = ""
            case ("$", "cd", ".."):
                cwd = cwd[: cwd.rindex("/") if "/" in cwd else 0]
            case ("$", "cd", path):
                cwd = f"{cwd}/{path}" if cwd else path
            case (size, *_):
                try:
                    size = int(size)
                except ValueError as _:
                    continue
                path = cwd
                while True:
                    sizes[path] += size
                    if not path:
                        break
                    path = path[: path.rindex("/") if "/" in path else 0]
    return sizes


def part1(lines):
    return sum(size for size in _parse(lines).values() if size <= 100000)


def part2(lines):
    sizes = _parse(lines)
    total = sizes[""]
    for size in sorted(sizes.values()):
        if 70000000 - (total - size) >= 30000000:
            return size
    return total

lines = open("07/input.txt").read().split("\n")
print(part1(lines))
print(part2(lines))