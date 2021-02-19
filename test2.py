# -*- coding: utf-8 -*-


mapData = {
    "MapData": (
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        (1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1),
        (1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
        (1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1),
        (1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1),
        (1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1),
        (1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1),
        (1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1),
        (1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1),
        (1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1),
        (1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1),
        (1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1),
        (1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1),
        (1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1),
        (1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1),
        (1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1),
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    ),
    "TestPoint": (
        (16, 15),
        (18, 4),
        (13, 2),
        (5, 2),
        (4, 12),
        (14, 2)
    )
}


def maze(mapData):
    map = mapData["MapData"]

    testPoint = mapData["TestPoint"]
    trackStack = []


    row = len(map)
    line = len(map[0])
    visitMap = [[0] * line for i in range(row)]

    for i in range(row):
        for j in range(line):
            if visitMap[i][j] == 0 and map[i][j] == 0:
                connectSet = set()
            visitMap[i][j] = 1


# 获取整个连通区域
def getConnectArea(map, i, j, visitMap, connectSet):
    childArr = getChildren(map, i, j, visitMap)
    connectQueue = []  # 存储中间连接点的队列
    connectQueue.append()
    for

def getChildren(map, i, j, visitMap):
    childArr = []
    if j - 1 >= 0 and visitMap[i][j - 1] == 0:
        childArr.append((i, j - 1))
    if i + 1 < len(map) and visitMap[i + 1][j] == 0:
        childArr.append((i + 1, j))
    if j + 1 < len(map[0]) and visitMap[i][j + 1] == 0:
        childArr.append((i, j + 1))
    return childArr


def getDownChild(map, i, j):
    if i + 1 < len(map):
        return map[i + 1][j]
    else:
        return None


def getRightChild(map, i, j):
    if j + 1 < len(map[0]):
        return map[i][j + 1]
    else:
        return None


def find(startR, startL, row, line):
    start0 = None
    end0 = None
    for i in range(startR, row):
        for j in range(startL, line):
            if map[i][j] == 0:
                start0 = j if start0 is None else start0


if __name__ == '__main__':
    map = (1, 2, 4)
    for i in range(2, 5, 1):
        print(i)
