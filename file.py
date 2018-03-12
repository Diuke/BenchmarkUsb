import time
import os
import win32api
import win32file
import os
import shutil


class BenchTests:
    path = ''
    driveLetter = ""
    usbDrives = []

    def __init__(self):
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        for e in drives:
            if win32file.GetDriveType(e) == win32file.DRIVE_REMOVABLE:
                self.usbDrives.append(e)

    def testCreate(self):
        times = 0
        repeat = 1000
        stats = [0, -999999, 999999]
        for i in range(repeat):
            start = time.time()
            file = open(self.usbDrives[0]+"/file.txt", "w")
            end = time.time()
            times += (end - start)
            file.close()
            os.remove(self.usbDrives[0]+"/file.txt")
            timei = end - start
            times += timei
            if stats[1] < timei:
                stats[1] = timei
            if stats[2] > timei:
                stats[2] = timei
        stats[0] = times / repeat
        return stats

    def testDelete(self):
        times = 0
        repeat = 1000
        stats = [0, -999999, 999999]
        for i in range(repeat):
            file = open(self.usbDrives[0]+"/file.txt", "w")
            file.close()
            start = time.time()
            os.remove(self.usbDrives[0]+"/file.txt")
            end = time.time()
            timei = end-start
            times += timei
            if stats[1] < timei:
                stats[1] = timei
            if stats[2] > timei:
                stats[2] = timei
        stats[0] = times / repeat
        return stats

    def testSequential(self):
        times = 0
        repeat = 1
        for i in range(repeat):
            f = open('newfile.txt', "wb")
            f.seek((1024 * 1024 * 1024) - 1)
            f.write(b"\0")
            f.close()

            f = open('newfile.txt', "rb+")
            dist = open(self.usbDrives[0]+"/newfile.txt", "xb+")
            start = time.time()
            shutil.copyfileobj(f, dist, 16 * 1024 * 1024)
            end = time.time()
            f.close()
            dist.close()
            os.remove(self.usbDrives[0] + "/newfile.txt")
            os.remove("newfile.txt")
            times += (end - start)

        return times / repeat

    def test4k(self):
        times = 0
        repeat = 1000
        stats = [0, -999999, 999999]
        for i in range(repeat):
            f = open('newfile.txt', "wb")
            f.seek((4 * 1024) - 1)
            f.write(b"\0")
            f.close()
            f = open('newfile.txt', "rb+")
            dist = open(self.usbDrives[0]+"/newfile.txt", "xb+")
            start = time.time()
            shutil.copyfileobj(f, dist, 16 * 1024 * 1024)
            end = time.time()
            f.close()
            dist.close()
            os.remove(self.usbDrives[0] + "/newfile.txt")
            os.remove("newfile.txt")
            timei = end - start
            times += timei
            if stats[1] < timei:
                stats[1] = timei
            if stats[2] > timei:
                stats[2] = timei
        stats[0] = times / repeat
        return stats