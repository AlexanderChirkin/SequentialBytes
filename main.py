from sequential_bytes import SequentialBytes, EndOfPacketError

seq_bytes = SequentialBytes(bytes(b'qwerty'))
try:
    print(seq_bytes.get(2))
    print(seq_bytes.get(3))
    print(seq_bytes.get(2))
except EndOfPacketError as e:
    print(e)
