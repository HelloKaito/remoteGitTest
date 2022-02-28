'''
Author: Zhang Qi
Date: 2022-02-17 15:59:27
LastEditTime: 2022-02-17 17:12:40
LastEditors: Zhang Qi
Description: file content
FilePath: \algorithm\Dijkstra\dicttest.py
copyright@ZhangQi
'''
dj = {1: {2: 1, 3: 12}, 2: {4: 6, 3: 9}, 3: {5: 5}, 4: {3: 4, 5: 13, 6: 15}, 5: {6: 4}}
print(dj[1])
print(dj["1"])
for key, value in dj.items():
    print(value)
print(len(dj))
for key, value in dj[2].items():
    print(key, value)

print(len(dj[2]))
print(type(dj[2]))
print('min',min(dj[2], key=lambda x: dj[2][x]))

currentNodeDict = {0: 3, 5: 7}
print(type(currentNodeDict))
nextNode = min(currentNodeDict, key = lambda x: currentNodeDict[x])
print(nextNode)