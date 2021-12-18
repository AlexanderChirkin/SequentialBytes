# SequentialBytes
Class for sequential getting chunks of bytes

Example of usage
```
>>> from sequential_bytes import SequentialBytes, EndOfPacketError
>>> seq_bytes = SequentialBytes(bytes(b'qwerty'))
>>> seq_bytes.get(2)
b'qw'
>>> seq_bytes.get(3)
b'ert'
>>> seq_bytes.get(2)
Traceback (most recent call last):
  ...
sequential_bytes.EndOfPacketError: EndOfPacketError{'packet_len': 6, 'curr_shift': 5, 'need_to_return': 2, 'log': [b'qw', b'ert', b'y']}
```
