import time
import os


class BenchTests:
    driveLetter = ""

    def __init__(self, driveLetter):
        self.driveLetter = driveLetter

    def testCreate(self):
        times = 0
        repeat = 2000
        for i in range(repeat):
            start = time.time()
            file = open(self.driveLetter+":/A1/file.txt", "w")
            end = time.time()
            times += (end - start)
            file.close()
            os.remove(self.driveLetter+":/A1/file.txt")
            # time.sleep(0.005)
            if i % 200 == 0:
                print(i)
        return (times / repeat)*1000

    def testDelete(self):
        times = 0
        repeat = 2000
        for i in range(repeat):
            file = open("F:/A1/file.txt", "w")
            file.close()
            start = time.time()
            os.remove("F:/A1/file.txt")
            end = time.time()
            times += (end - start)
            if i % 200 == 0:
                print(i)
            # time.sleep(0.005)
        return (times / repeat)*1000
