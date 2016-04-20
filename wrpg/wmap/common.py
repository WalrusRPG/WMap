from enum import IntEnum
import struct


class MapCompression(IntEnum):
    UNKNWON = 0
    RAW = 1
    RLE_PER_LAYER = 2
    RLE_ALL_LAYERS = 3
    ZLIB = 4


def header_check_structure():
    return ('>' +  # Big endian
            '4s' +  # 'WMap' magic cookie (0->4)
            'I'  # Checksum : unsigned int (4->8)
            )


def header_data_structure():
    return (
        '>'
        'I' +  # Version : unsigned int (8->12)
        'I' +  # Data size : unsigned int (12->16)
        'H' +  # Map width : unsigned short (16->18)
        'H' +  # Map height : unsigned short (18->20)
        'H' +  # Number of layers : unsigned short (20->22)
        'H' +  # Number of events : unsigned short (22->24)
        'I'   # Map data compression type : Enum (unsigned int) (24->28)
    )


def header_structure():
    return(
        '>' +
        header_check_structure()[1:] +
        header_data_structure()[1:]
    )
