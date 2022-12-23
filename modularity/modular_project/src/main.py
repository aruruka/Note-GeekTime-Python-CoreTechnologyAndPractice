import sys
sys.path.append('.')

from modularity.modular_project.proto.mat import Matrix
from modularity.modular_project.utils.mat_mul import mat_mul

a = Matrix([[1,2], [3,4]])
b = Matrix([[5,6], [7,8]])

print(mat_mul(a, b).data)