from .random_generator import *
import sys
import time
import matplotlib.pyplot as plt

def eval_stats(algo, iters=100, n=100):
    worst   = 0
    mean    = 0
    best    = sys.maxsize

    for i in range(iters):
        l = get_random_ints(n)
        
        stime = time.time_ns()
        algo(l)
        ttime = time.time_ns() - stime
        
        mean += ttime
        if ttime > worst:
            worst = ttime
        elif ttime < best:
            best = ttime
            
    return (worst, mean/iters, best)

def disp_stats(w, m, b):
    plt.bar([0, 1, 2], [w, m, b])
    plt.show()