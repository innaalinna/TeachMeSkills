
#возможно я недопоняла задачу, но count работает в бесконечный цикл :(

def count(start, step=1):
    seq = [start]

    while True:
        if step != 0:
            seqq = list.copy(seq)
            val = seqq.pop(seq.count(seqq) - 1)
            seq.append(val + step)
        else:
            break
    return seq


for i in count(35, 3):
    print(i)
