import re


def header(func):
    def fout(*args):
        res = func(*args)
        print(f"({func.__name__.split('_')[-1].replace('d', '/')}, " + ', '.join(list(map(str, args))) + f")={res}")
        return res

    return fout


@header
def FdP(i, N):  # checked
    return (1 + i) ** N


@header
def PdF(i, N):  # checked
    return 1 / (1 + i) ** N


@header
def AdF(i, N):
    return i / ((1 + i) ** N - 1)


@header
def FdA(i, N):
    return ((1 + i) ** N - 1) / i


@header
def AdP(i, N):  # checked
    return i * (1 + i) ** N / ((1 + i) ** N - 1)


@header
def PdA(i, N):  # checked
    return ((1 + i) ** N - 1) / i / (1 + i) ** N


@header
def AdG(i, N):
    return 1 / i - N / ((1 + i) ** N - 1)


@header
def Geometric_PdA(g, i, N):  # checked
    io = (1 + i) / (1 + g) - 1
    if abs(io) < 1E-6:
        return N / (1 + g)

    print(f'i_o=(1+i)/(1+g)-1={io}')
    return PdA(io, N) / (1 + g)


func_pattern = re.compile(r'\([A-Z]/[A-Z],')


def func_conv(matchobj):
    m = matchobj.group(0)
    return f"{m[1]}d{m[3]}("


def interpret(s):
    cmd = func_pattern.sub(func_conv, s).strip()
    print(cmd)
    print(f'{s}={eval(cmd)}')
    # return eval(s)


def shell():
    cmd = 'print("Hello world")'
    while cmd != 'q':
        if len(cmd) > 0: interpret(cmd)
        cmd = input('> ').strip()

if __name__ == "__main__":
    shell()

'''
python main.py
> (4000-3000) * (A/P, 0.1, 1) + (3000)*(0.1)
(A/P, 0.1, 1) = 1.099999999999992
(4000-3000) * (A/P, 0.1, 1) + (3000)*(0.1) = 1399.999999999999
'''
