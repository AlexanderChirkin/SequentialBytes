from typing import List


class SequentialBytes:
    """ Provides an interface for sequential getting chunks of the bytes object """
    def __init__(self, packet: bytes):
        self._packet = packet
        self._shift = 0
        self._log = []

    def get(self, n: int) -> bytes:
        """ Returns next n bytes """
        if self._shift + n > len(self._packet):
            raise EndOfPacketError(len(self._packet), self._shift, n, self.log)
        chunk = self._packet[self._shift: self._shift + n]
        self._shift += n
        self._log.append(chunk)
        return chunk

    @property
    def is_end(self) -> bool:
        return self._shift >= len(self._packet)

    @property
    def log(self) -> List[bytes]:
        return self._log + [self._packet[self._shift:]]


class EndOfPacketError(Exception):
    def __init__(self, packet_len: int, curr_shift: int, need_to_return: int, log: List[bytes]):
        self.packet_len = packet_len
        self.curr_shift = curr_shift
        self.need_to_return = need_to_return
        self.log = log

    def __str__(self):
        return f'{self.__class__.__name__}{self.__dict__}'
