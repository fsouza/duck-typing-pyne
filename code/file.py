def copy(dst, src, filter):
    for line in src:
        if filter(line):
            dst.write(line)
