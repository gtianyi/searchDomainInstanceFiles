import json
import os

with open("/home/aifs1/gu/phd/research/workingPaper/boundedCostSearch/optimalSolution/vaccumworld.uniform.json") as f:
    data = json.load(f)
    for key in data:
        if data[key] == '-1':
            if os.path.exists(key):
                os.remove(key)
