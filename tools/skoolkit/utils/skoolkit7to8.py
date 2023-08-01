#!/usr/bin/env python3
import sys
import re
import argparse

DESCRIPTION = """
Convert a control file or ref file from SkoolKit 7 format to SkoolKit 8 format
and print it on standard output.
"""

def _parse_ref(reffile_f):
    preamble = []
    sections = []
    section = []
    section_name = None
    for line in reffile_f:
        s_line = line.rstrip()
        if line.startswith('[') and not line.startswith('[[') and s_line.endswith(']'):
            if section_name:
                sections.append([section_name, section])
            else:
                preamble = section
            section_name = s_line[1:-1]
            section = []
        else:
            section.append(s_line)
    if section_name:
        sections.append([section_name, section])
    else:
        preamble = section
    return preamble, sections

def _get_section(sections, name):
    for index, section in enumerate(sections):
        if name == section[0]:
            return index, section[1]
    return -1, None

def convert_ref(reffile_f):
    preamble, sections = _parse_ref(reffile_f)

    # AsmSinglePageTemplate, TitlePrefix, TitleSuffix
    index, game_section = _get_section(sections, 'Game')
    prefixes = ('TitlePrefix=', 'TitleSuffix=')
    values = ['The complete', 'RAM disassembly']
    title_set = False
    if game_section:
        for i, line in enumerate(game_section):
            if line.startswith(prefixes[0]):
                values[0] = line[len(prefixes[0]):]
                title_set = True
            elif line.startswith(prefixes[1]):
                values[1] = line[len(prefixes[1]):]
                title_set = True
            elif line.startswith('AsmSinglePageTemplate='):
                game_section[i] = 'AsmSinglePage=1'
    if title_set:
        sections[index][1] = [line for line in game_section if not line.startswith(prefixes)]
        param = 'GameIndex=' + '<>'.join(values)
        ph_section = _get_section(sections, 'PageHeaders')[1]
        if ph_section:
            ph_section.insert(0, param)
        else:
            sections.append(('PageHeaders', [param]))

    # Titles:Asm-*
    titles_section = _get_section(sections, 'Titles')[1]
    if titles_section:
        for i, line in enumerate(titles_section):
            if line.startswith(('Asm-b', 'Asm-c', 'Asm-g', 'Asm-s', 'Asm-t', 'Asm-u', 'Asm-w')):
                titles_section[i] += ' {entry[address]}'

    # Print ref file
    if preamble:
        print('\n'.join(preamble))
    for section_name, lines in sections:
        print('[{}]'.format(section_name))
        print('\n'.join(lines).rstrip() + '\n')

def convert_ctl(ctlfile_f):
    for line in ctlfile_f:
        if line.startswith((' ', 'B ', 'T')):
            fields = [line[0]] + [t for t in line[1:].lstrip().split(' ', 1) if t]
            if len(fields) > 1:
                fields[1] = re.sub('([,:])B([1-9$%])', r'\1n\2', fields[1])
                fields[1] = re.sub('([,:])T([1-9$%])', r'\1c\2', fields[1])
                line = ' '.join(fields)
        sys.stdout.write(line)

def main(args):
    parser = argparse.ArgumentParser(
        usage='skoolkit7to8.py FILE',
        description=DESCRIPTION,
        add_help=False
    )
    parser.add_argument('infile', help=argparse.SUPPRESS, nargs='?')
    namespace, unknown_args = parser.parse_known_args(args)
    infile = namespace.infile
    if unknown_args or infile is None:
        parser.exit(2, parser.format_help())
    infile_l = infile.lower()
    with open(infile) as f:
        if infile_l.endswith('.ref'):
            convert_ref(f)
        elif infile_l.endswith('.ctl'):
            convert_ctl(f)
        else:
            print('Input file must be a ref file or control file', file=sys.stderr)

if __name__ == '__main__':
    main(sys.argv[1:])
