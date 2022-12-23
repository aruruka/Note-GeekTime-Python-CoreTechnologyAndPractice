import sys
sys.path.append("./modularity")

from utils.class_utils import *
# from class_utils import *

encoder = Encoder()
decoder = Decoder()

print(encoder.encode('abcde'))
print(decoder.decode('edcba'))
