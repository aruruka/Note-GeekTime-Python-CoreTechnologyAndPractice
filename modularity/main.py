import sys

sys.path.append('.')

from modularity.utils_pack import get_sum
from class_utils import *

print(get_sum(1, 2))

encoder = Encoder()
decoder = Decoder()

print(encoder.encode('abcde'))
print(decoder.decode('edcba'))