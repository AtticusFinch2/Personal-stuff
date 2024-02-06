import random
import time
import contextlib
import sys
import pandas as pd

## Comment out the next line if you just coy and paste your code in this file
from HeapTesting import Heap, heapify, is_heap

name = "BradyMiller"
MAXITER = 12  # doubling 12x
RUNTIME_ALLOWED = 0.5  # sec

## Edit comments in speedrun() if you want to save to a file. (Just before submitting.)


def random_list(length, value_range=(-1000, 1000)):
    rlow, rhigh = value_range
    ans = [0] * length
    for k in range(length):
        ans[k] = random.randint(rlow, rhigh)
    return ans


def random_heap(length, value_range=(-1000, 1000)):
    ans = random_list(length, value_range)
    heapify(ans, length)
    return ans


## heapify needs to return the data
assert heapify([10], 1) is not None

## Make sure the random heap function is working (usually a problem bc heapify is bad)
assert len(random_heap(5)) == 5
## heapify should actually make a heap (of some size)
assert heapify([50, 45, 40], 3)[0:3] == [40, 45, 50] or heapify([50, 45, 40], 3)[0:3] == [40, 50, 45]


def timing_of(
    title, proc=None, wanted="heap", start_power_of_2=4, cutoff_time_sec=0.5, maxiter=20
):
    last_duration = 0
    ans = []
    n = 2**start_power_of_2
    while 0 < maxiter and last_duration < cutoff_time_sec * (10**9):
        h = random_list(n, value_range=(-1_000_000, 1_000_000))
        if wanted == "heap":
            heapify(h)
        elif wanted == "object":
            h = Heap(h, n)
        tstart = time.perf_counter_ns()
        if wanted == "random":
            result = proc(h, n)
        elif wanted == "heap":
            result = proc(h, n)
        elif wanted == "object":
            result = proc(h)
        tend = time.perf_counter_ns()
        last_duration = tend - tstart
        ans.append([n, last_duration, title, name])
        print(f"[{title}] completed {n} in {last_duration/10**9} sec")
        n *= 2
        maxiter -= 1
    return ans


def generate_1(do_timing_of):
    def get_until_empty(h: Heap):
        while not h.empty():
            h.get()

    def repeated_insert(vals: [int], n: int):
        h = Heap(contents=[])
        while vals:
            h.put(vals.pop())
        return h

    d1 = do_timing_of("is_heap", wanted="heap", proc=is_heap)
    d2 = do_timing_of("heapify", wanted="random", proc=heapify)
    d3 = do_timing_of("get_until_empty", wanted="object", proc=get_until_empty)
    d4 = do_timing_of("repeated_insert", wanted="random", proc=repeated_insert)

    data = d1 + d2 + d3 + d4
    return pd.DataFrame(data, columns=["num", "time", "title", "who"])


def generate_data(outfile, cutoff_time_sec=RUNTIME_ALLOWED, maxiter=MAXITER):
    def do_timing_of(title, wanted, proc):
        return timing_of(
            title, wanted, proc, cutoff_time_sec=cutoff_time_sec, maxiter=maxiter
        )

    df = generate_1(do_timing_of)
    df.to_csv(outfile)
    return df


"""def make_plot_1(infile):
    df = pd.read_csv(infile)
    plot1 = sns.scatterplot(df, x="num", y="time", hue='title')
    plot2 = sns.lineplot(df, x="num", y="time", hue='title')
    plt.xscale("log")
    plt.yscale("log")
    plt.show()
"""



def speedrun():
    filename = "data-BradyMiller.csv"
    with open(filename, "w") as outf:
    ## with contextlib.nullcontext(sys.stdout) as outf:
        generate_data(outf)


if __name__ == "__main__":
    speedrun()
