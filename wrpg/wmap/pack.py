from .common import (MapCompression, header_check_structure,
                     header_data_structure, header_structure)
import zlib
import struct
import tmx
from tmx import TileMap


def pack(mapFile):
    tileMap = TileMap.load(mapFile)

    if len(tileMap.tilesets) != 1:
        print('The map must contain only one tileset. It contains {}.'.format(
            len(tileMap.tilesets)
        ))

    map_width = tileMap.width
    map_height = tileMap.height
    map_version = 0
    map_tile_layers = [t for t in tileMap.layers if type(t) is tmx.Layer]
    map_n_layers = len(map_tile_layers)
    if map_n_layers > 2:
        print('Too much tile layers : {}'.format(map_n_layers))
        return
    map_n_events = 0  # TODO : event managment
    map_compression = MapCompression.RAW  # TODO : map compresison support.

    # TODO : add event size once defined and correct compressed map data size
    # sizof(uint16_t) = 2
    map_datasize = (map_width * map_height * map_n_layers * 2)

    data_part = struct.pack(header_data_structure(), map_datasize, map_version,
                            map_width, map_height, map_n_layers, map_n_events,
                            map_compression)

    header = struct.pack(header_structure(),
                         b'WMap', zlib.crc32(data_part),
                         map_version, map_datasize,
                         map_width, map_height,
                         map_n_layers, map_n_events,
                         map_compression)

    data = b''
    # Raw storage.
    for layer in map_tile_layers:
        for tile in layer.tiles:
            data += struct.pack('>H', tile.gid)

    return header + data
