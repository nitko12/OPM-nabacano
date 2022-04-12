import subprocess

from threading import Timer
from pprint import pprint
from multiprocessing import Pool


def kill(process): return process.kill()

# 32 ostalo vald, 27 rjeseno


opts = [

    (2, 19, 9, 4),
    (2, 23, 11, 5),
    (2, 25, 9, 3),
    (2, 27, 13, 6),
    (2, 31, 10, 3),
    (2, 31, 15, 7),
    (2, 8, 4, 3),
    (2, 10, 4, 2),
    (2, 10, 4, 4),
    (2, 10, 5, 4),
    (2, 11, 5, 4),
    (2, 12, 4, 3),
    (2, 12, 6, 5),
    (2, 13, 4, 2),
    (2, 13, 4, 3),
    (2, 16, 6, 3),
    (2, 19, 4, 2),
    # (2, 21, 3, 1),
    (2, 21, 5, 2),
    (2, 21, 6, 3),
    (2, 21, 7, 3),
    (2, 21, 3, 1),
    (2, 21, 3, 1),
    (2, 25, 4, 1),
    (2, 25, 5, 1),
    (2, 25, 5, 2),
    (2, 28, 4, 1),
    (2, 28, 7, 2),
    (2, 31, 6, 2),
    (3, 12, 4, 3),
    (5, 12, 6, 1),
    (3, 16, 7, 5),

]


def parse_output(s, x):
    cmd = ["python3", "parse.py", *map(str, x)]

    # print(cmd)

    f = open("solved/" + s, "r")
    o = open("parsed/" + s, "w")

    ping = subprocess.Popen(
        cmd,  stdin=f, stdout=o, stderr=subprocess.PIPE)

    my_timer = Timer(60 * 60, kill, [ping])

    try:
        my_timer.start()
        stdout, stderr = ping.communicate()

        o.flush()
        print(s, "parse done", ping.returncode, stderr)
    except:
        print(s, "parse time out")
    finally:
        my_timer.cancel()

    f.close()
    o.close()


def run_input(s, x):
    cmd = ["cryptominisat5"]

    # print(cmd)

    i = open("out/" + s, "r")
    f = open("solved/" + s, "w")

    ping = subprocess.Popen(
        cmd,  stdin=i, stdout=f, stderr=subprocess.PIPE)

    my_timer = Timer(60 * 60, kill, [ping])

    try:
        my_timer.start()
        stdout, stderr = ping.communicate()

        print(s, "calc done", ping.returncode)

        f.flush()

        parse_output(s, x)

    except Exception as e:
        print(e)
        print(s, "calc time out")
    finally:
        my_timer.cancel()

    i.close()
    f.close()


def run(x):
    cmd = ['python3', '5.py', *map(str, x)]

    # print(cmd)
    s = "_".join(map(str, x))+".txt"
    f = open("out/" + s, "w")
    ping = subprocess.Popen(
        cmd,  stdout=f, stderr=subprocess.PIPE)

    my_timer = Timer(60 * 60, kill, [ping])

    try:
        my_timer.start()
        stdout, stderr = ping.communicate()

        # print(x, "input done")
        f.flush()
        run_input(s, x)

    except:
        print(x, "input time out", ping.returncode)
    finally:
        my_timer.cancel()

    f.close()


if __name__ == "__main__":

    print(len(opts))

    opts.sort(key=lambda x: x[3])

    # run(opts[0])

    with Pool(2) as p:
        print(p.map(run, opts))

    # pprint(opts)
