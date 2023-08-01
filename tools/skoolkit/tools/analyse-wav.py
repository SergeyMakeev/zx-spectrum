#!/usr/bin/env python3
import sys
import argparse

class WaveError(Exception):
    pass

class WaveFile:
    def __init__(self, data):
        self.chunks = {}

        i = 0
        chunk_id = _to_chars(data[i:i + 4])
        if chunk_id != 'RIFF':
            raise WaveError('"RIFF" chunk not found')
        length = _to_int(data[i + 4:i + 8])
        self.chunks[chunk_id] = (i, length)
        i += 8

        chunk_id = _to_chars(data[i:i + 4])
        if chunk_id != 'WAVE':
            raise WaveError('"WAVE" chunk not found')
        i += 4

        while i < len(data):
            chunk_id = _to_chars(data[i:i + 4])
            length = _to_int(data[i + 4:i + 8])
            self.chunks[chunk_id] = (i, data[i + 8:i + 8 + length])
            i += 8 + length

        for exp_chunk_id in ('fmt ', 'data'):
            if exp_chunk_id not in self.chunks:
                raise WaveError('"{} " chunk not found'.format(exp_chunk_id))

        self.samples = self.chunks['data'][1]
        fmt = self.chunks['fmt '][1]
        self.audio_format = _to_int(fmt[0:2])
        self.num_channels = _to_int(fmt[2:4])
        self.sample_rate = _to_int(fmt[4:8])
        self.byte_rate = _to_int(fmt[8:12])
        self.bytes_per_sample = _to_int(fmt[12:14])
        self.bits_per_sample = _to_int(fmt[14:16])
        self.num_samples = len(self.samples) // self.bytes_per_sample
        self.duration = self.num_samples / (self.num_channels * self.sample_rate)

def _to_chars(data):
    return ''.join(chr(b) for b in data)

def _to_int(data, signed=False):
    if len(data) == 4:
        return 16777216 * data[3] + 65536 * data[2] + 256 * data[1] + data[0]
    value = 256 * data[1] + data[0]
    if value < 32768 or not signed:
        return value
    return value - 65536

def dump_wav(data):
    wav = WaveFile(data)
    print(f'audio format: {wav.audio_format}')
    print(f'channels: {wav.num_channels}')
    print(f'sample rate: {wav.sample_rate}')
    print(f'byte rate: {wav.byte_rate}')
    print(f'bytes per sample: {wav.bytes_per_sample}')
    print(f'bits per sample: {wav.bits_per_sample}')
    print(f'samples: {wav.num_samples} ({wav.duration:.03f}s)')
    n = 0
    sample_size = wav.bytes_per_sample
    samples = wav.samples
    for i in range(0, len(samples), sample_size):
        sample = _to_int(samples[i:i + sample_size], True)
        print(f'{n:>7} {sample}')
        n += 1

def show_diffs(fname1, data1, fname2, data2):
    wav1 = WaveFile(data1)
    wav2 = WaveFile(data2)

    diffs = []
    if wav1.audio_format != wav2.audio_format:
        diffs.append('audio format: {}, {}'.format(wav1.audio_format, wav2.audio_format))
    if wav1.num_channels != wav2.num_channels:
        diffs.append('channels: {}, {}'.format(wav1.num_channels, wav2.num_channels))
    if wav1.sample_rate != wav2.sample_rate:
        diffs.append('sample rate: {}, {}'.format(wav1.sample_rate, wav2.sample_rate))
    if wav1.byte_rate != wav2.byte_rate:
        diffs.append('byte rate: {}, {}'.format(wav1.byte_rate, wav2.byte_rate))
    if wav1.bytes_per_sample != wav2.bytes_per_sample:
        diffs.append('bytes per sample: {}, {}'.format(wav1.bytes_per_sample, wav2.bytes_per_sample))
    if wav1.bits_per_sample != wav2.bits_per_sample:
        diffs.append('bits per sample: {}, {}'.format(wav1.bits_per_sample, wav2.bits_per_sample))
    if not diffs:
        if len(wav1.samples) != len(wav2.samples):
            diffs.append('samples: {} ({:.02f}s), {} ({:.02f}s)'.format(len(wav1.samples), wav1.duration, len(wav2.samples), wav2.duration))
        else:
            sample_size = wav1.bytes_per_sample
            index = 1
            for i in range(0, len(wav1.samples), sample_size):
                sample1 = _to_int(wav1.samples[i:i + sample_size], True)
                sample2 = _to_int(wav2.samples[i:i + sample_size], True)
                if sample1 != sample2:
                    diffs.append('sample {}/{}: {}, {}'.format(index, wav1.num_samples, sample1, sample2))
                index += 1

    if diffs:
        print(fname1)
        print(fname2)
        for line in diffs:
            print('  {}'.format(line))

###############################################################################
# Begin
###############################################################################
parser = argparse.ArgumentParser(
    usage='\n  %(prog)s --dump FILE\n  %(prog)s --diff FILE FILE',
    description="Analyse a WAV file, or compare two WAV files.",
    add_help=False
)
parser.add_argument('wavfiles', help=argparse.SUPPRESS, nargs='*')
group = parser.add_argument_group('Options')
group.add_argument('--diff', action='store_true',
                   help='Show the differences between two WAV files')
group.add_argument('--dump', action='store_true',
                   help='Dump metadata and sample values')
namespace, unknown_args = parser.parse_known_args()
if unknown_args or not ((namespace.dump and len(namespace.wavfiles) == 1) or (namespace.diff and len(namespace.wavfiles) == 2)):
    parser.exit(2, parser.format_help())

files = []
for fname in namespace.wavfiles[:2]:
    with open(fname, 'rb') as f:
        files.append(list(f.read()))

try:
    if namespace.diff:
        show_diffs(namespace.wavfiles[0], files[0], namespace.wavfiles[1], files[1])
    elif namespace.dump:
        dump_wav(files[0])
except WaveError as e:
    sys.stderr.write('ERROR: {}\n'.format(e.args[0]))
