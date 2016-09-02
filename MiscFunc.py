import struct


def calc_crc(chrs):
    arc = struct.unpack("%dB" % len(chrs), chrs)
    csum = 0
    for c in arc:
        csum += c
    return csum & 0xff


def get_short_from_buf(buf):
    return struct.unpack("!H", buf[:2])[0]
