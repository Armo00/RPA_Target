from datetime import datetime
import os


def newFile(localMode, localContent='placeholder'):
    target = 'database/' + localMode + '/' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.txt'

    localFile = open(target, 'w')
    localFile.write(str(localContent))
    localFile.close()

    return


def readFile(localMode):
    target = 'database/' + localMode
    result = {}
    for item in os.listdir(target):
        localFile = open(target + '/' + item, 'r')
        localTempItem = eval(localFile.readlines()[0])
        localFile.close()
        result[item] = localTempItem
        result[item]['fileName'] = item
    for i in result:
        print(i, result[i])
    return result


if __name__ == "__main__":
    content = {'aaa': 111, 'bbb': 222, 'ccc': [{'ddd': 444, 'eee': 555}, {'ddd': 666, 'eee': 777}]}
    mode = 'awaitingAuditTicket'
    newFile(mode, content)
    readFile(mode)
