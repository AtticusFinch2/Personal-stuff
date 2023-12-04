import random
import time
import simulate2048

myname = "BradenMiller"

## 1. Change myname to a name WITH NO SPACES like EvanAssmus
## 2. Pick a number of trials that finishes in 5 minutes.
##    Make that number the default for runtrials.
##    Example: 24 runs finish in 5 minutes, so def runtrials(n=24): ...
## 3. There should be NO OTHER OUTPUT

# Evan: you asked to show my versions of solvers so i put them into the parameter of the run_your_solver function
def run_your_solver(version=3):
    match version:
        case 4:
            return simulate2048.doSimFast(1)[0]  # fast-ish but kinda bad
        case 3:
            return simulate2048.doSim(1)[0]  # Slowest but highest average score (use n=15)
        case 2:
            return simulate2048.doSim2(1)[0]  # minimax but with pretty bad weights
        case 1:
            return simulate2048.doSimDummyFast(1)[0]  # fast but stupid (n=2000)
def runtrials(n=15):
    for _ in range(n):
        starttime = time.time()
        maxtile = run_your_solver(3)
        endtime = time.time()
        runtime = endtime-starttime
        print(f'"REPORT","{myname}",{runtime},{maxtile}')
starttime2 = time.time()
if __name__ == '__main__':
    runtrials()
endtime2 = time.time()
print(endtime2-starttime2)