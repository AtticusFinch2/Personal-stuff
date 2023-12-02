import random
import time
import simulate2048

myname = "BradenMiller"

## 1. Change myname to a name WITH NO SPACES like EvanAssmus
## 2. Pick a number of trials that finishes in 5 minutes.
##    Make that number the default for runtrials.
##    Example: 24 runs finish in 5 minutes, so def runtrials(n=24): ...
## 3. There should be NO OTHER OUTPUT


def run_your_solver(isfast=True):
    if isfast:
        return simulate2048.doSimFast(1)[0]
    return simulate2048.doSim(1)[0]
def runtrials(n=90):
    for _ in range(n):
        starttime = time.time()
        maxtile = run_your_solver()
        endtime = time.time()
        runtime = endtime-starttime
        print(f'"REPORT","{myname}",{runtime},{maxtile}')
runtrials()
if __name__ == '__main__':
    runtrials()