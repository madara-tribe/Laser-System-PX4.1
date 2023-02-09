# https://atmarkit.itmedia.co.jp/ait/articles/2104/16/news022.html
# https://qiita.com/s_fujii/items/5dde7376a8d9a853bd0c

import psutil
import csv

class CPULog:
    def __init__(self, fname="cpu_burden.csv"):
        self.f = open(fname, 'a')
        self.writer = csv.writer(self.f, quoting=csv.QUOTE_NONNUMERIC)
        self.count = 0
        
    def write(self):
        mem = psutil.virtual_memory()
        # count, cpu_memory, cpu_used_ratio
        logs = str(self.count) + "," + str(mem.percent) + "," + str(mem.used)
        logs = logs.split(',')
        self.writer.writerow(logs)
        self.count +=1
        
    def close(self):
        self.f.close()
