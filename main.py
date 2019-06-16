from colorama import init, Fore, Back
init()

def gen_layer_2d(prev_layer):
    prev_layer.insert(0, 0)
    prev_layer.append(0)
    new_layer = [prev_layer[i] + prev_layer[i+1] for i in range(0, len(prev_layer) - 1)]
    prev_layer.pop()
    prev_layer.pop(0)
    return new_layer

def format_2d(seq, mod):
    # print(seq)
    for i, row in enumerate(seq):
        for j, num in enumerate(row):
            remainder = seq[i][j] % mod
            if remainder == 0: seq[i][j] = '  '
            elif remainder == 1: seq[i][j] = Fore.WHITE+'██'
            elif remainder == 2: seq[i][j] = Fore.RED+'██'
            elif remainder == 3: seq[i][j] = Fore.GREEN+'██'
            elif remainder == 4: seq[i][j] = Fore.BLUE+'██'
            elif remainder == 5: seq[i][j] = Fore.CYAN+'██'
            else: seq[i][j] = Fore.RESET+str(remainder)

def print_2d(seq, layers):
    for row in seq:
        string = ''.join(map(str, row))
        center_size = layers*2+5*string.count('█')//2
        print(string.center(center_size))

def gen_layer_3d(prev_layer):
    temp = [[0] * (len(prev_layer) + 2) for i in range(len(prev_layer[0]) + 2)]
    for i, row in enumerate(prev_layer):
        for j, num in enumerate(prev_layer[i]):
            temp[i+1][j+1] = prev_layer[i][j]
    
    return [[temp[i][j] + temp[i][j+1] + temp[i+1][j] + temp[i+1][j+1]\
    for i in range(len(prev_layer) + 1)] for j in range(len(prev_layer[0]) + 1)]

def format_3d(seq, mod):
    for i, layer in enumerate(seq):
        for j, row in enumerate(layer):
            for k, num in enumerate(row):
                remainder = seq[i][j][k] % mod
                if remainder == 0: seq[i][j][k] = '  '
                elif remainder == 1: seq[i][j][k] = Fore.WHITE+'██'
                elif remainder == 2: seq[i][j][k] = Fore.RED+'██'
                elif remainder == 3: seq[i][j][k] = Fore.GREEN+'██'
                elif remainder == 4: seq[i][j][k] = Fore.BLUE+'██'
                elif remainder == 5: seq[i][j][k] = Fore.CYAN+'██'
                else: seq[i][j][k] = Fore.RESET+str(remainder)

def print_3d(seq, layers):
    for layer in seq:
        print('\n')
        for row in layer:
            string = ''.join(map(str, row))
            center_size = layers*2+5*string.count('█')//2
            print(string.center(center_size))

#SET YOUR VARIABLES HERE

mod = 5
layers = 37
two_dim = False

seq = []

if two_dim:
    beginning_layer = [1]
    seq.append(beginning_layer)

    for i in range(layers-1):
        seq.append(gen_layer_2d(seq[i]))
    format_2d(seq, mod)
    print_2d(seq, layers)
else:
    beginning_layer = [[1]]
    seq.append(beginning_layer)

    for i in range(layers-1):
        seq.append(gen_layer_3d(seq[i]))
    format_3d(seq, mod)
    print_3d(seq, layers)