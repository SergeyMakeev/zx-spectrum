#!/usr/bin/env python
import sys
import argparse

def write(text):
    sys.stdout.write(text)

def info(text):
    sys.stderr.write(text + '\n')

def _convert_ctl_asm_directive(line):
    asm_fields = line[3:].rstrip().split(':', 1)
    if len(asm_fields) < 2:
        write(line)
        return 0
    directive = asm_fields[0]
    asm_fields[1] = asm_fields[1].split('=', 1)
    addr_str = asm_fields[1][0]
    if directive == 'ignoreua':
        comment_type = 'i'
        if ':' in addr_str:
            addr_str, comment_type = addr_str.split(':', 1)
        write('@ {} {}:{}\n'.format(addr_str, directive, comment_type))
    elif len(asm_fields[1]) == 2:
        write('@ {} {}={}\n'.format(addr_str, directive, asm_fields[1][1]))
    else:
        write('@ {} {}\n'.format(addr_str, directive))
    return 1

def _get_address(ctl_line):
    addr_str = ctl_line[1:].lstrip().split(' ', 1)[0].split(',')[0].split('-')[0]
    if addr_str.startswith('$'):
        return int(addr_str[1:], 16)
    return int(addr_str)

def convert_skool(skoolfile_f):
    count = 0
    for line in skoolfile_f:
        if line.startswith('; @'):
            write(line[2:])
            count += 1
        else:
            write(line)
    if count:
        info("Converted {} ASM directive(s)".format(count))
    else:
        info("No changes")

def convert_ctl(ctlfile_f):
    entry_addresses = set()
    for line in ctlfile_f:
        if line and line[0] in 'bcgistuw':
            entry_addresses.add(_get_address(line))

    ctlfile_f.seek(0)

    d_dir_count = 0
    asm_dir_count = 0
    range_count = 0
    for line in ctlfile_f:
        if line.startswith('; @'):
            asm_dir_count += _convert_ctl_asm_directive(line)
            continue
        if line.startswith('D') and _get_address(line) not in entry_addresses:
            write('N' + line[1:])
            d_dir_count += 1
            continue
        addr_str = line[1:].lstrip().split(' ', 1)[0].split(',')[0]
        if addr_str.count('-') == 1:
            start, end = [int(a) for a in addr_str.split('-')]
            write(line.replace(addr_str, '{},{}'.format(start, end - start + 1), 1))
            range_count += 1
            continue
        write(line)

    if asm_dir_count:
        info("Converted {} ASM directive(s)".format(asm_dir_count))
    if d_dir_count:
        info("Converted {} 'D' directive(s) to 'N'".format(d_dir_count))
    if range_count:
        info("Converted {} address range(s)".format(range_count))
    if asm_dir_count + d_dir_count + range_count == 0:
        info("No changes")

def convert_sft(sftfile_f):
    convert_skool(sftfile_f)

def convert_css(cssfile_f):
    css = cssfile_f.read()
    write(css.replace('a.link', 'a'))

def main(args):
    parser = argparse.ArgumentParser(
        usage='skoolkit4to5.py FILE',
        description="Convert a skool, ctl or sft file from SkoolKit 4 format to SkoolKit 5 format and print it on standard output.",
        add_help=False
    )
    parser.add_argument('infile', help=argparse.SUPPRESS, nargs='?')
    namespace, unknown_args = parser.parse_known_args(args)
    infile = namespace.infile
    if unknown_args or infile is None:
        parser.exit(2, parser.format_help())
    infile_l = infile.lower()
    with open(infile) as f:
        if infile_l.endswith('.ctl'):
            convert_ctl(f)
        elif infile_l.endswith('.sft'):
            convert_sft(f)
        elif infile_l.endswith('.css'):
            convert_css(f)
        else:
            convert_skool(f)

if __name__ == '__main__':
    main(sys.argv[1:])
