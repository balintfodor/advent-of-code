from collections import defaultdict
import copy

# input = [125, 17]
input = [27, 10647, 103, 9, 0, 5524, 4594227, 902936]

n_1 = 25
n_2 = 75

# for i in range(n_2):
#     new_input = []
#     for j in range(len(input)):
#         if input[j] == 0:
#             new_input.append(1)
#         elif len(str(input[j])) % 2 == 0:
#             a = str(input[j])
#             n = len(a)
#             new_input.append(int(a[:(n//2)]))
#             new_input.append(int(a[(n//2):]))
#         else:
#             new_input.append(input[j] * 2024)
#     print(len(new_input))
#     input = new_input

orig_input = input

# cache = {}


compressed_input = defaultdict(int)
for k in orig_input:
    compressed_input[k] += 1

print(compressed_input)

for i in range(n_2):
    new_compressed_input = defaultdict(int)
    for cj, cjv in compressed_input.items():
        if cj == 0:
            new_compressed_input[1] += cjv
        elif len(str(cj)) % 2 == 0:
            a = str(cj)
            n = len(a)
            x1 = int(a[:(n//2)])
            x2 = int(a[(n//2):])
            new_compressed_input[x1] += cjv
            new_compressed_input[x2] += cjv
        else:
            x = cj * 2024
            new_compressed_input[x] += cjv
    print(new_compressed_input)
    z = sum([new_compressed_input[k] for k in new_compressed_input])
    compressed_input = copy.deepcopy(new_compressed_input)
    print(z)
