def printTable(table):

    # find longest string in each list within table
    maxStrLen = []
    for entry in table:
        maxLen = 0
        for ele in entry: 
            if len(ele) > maxLen: 
                maxLen = len(ele)
        maxStrLen.append(maxLen) 

    # print table in correct format, each column right justified
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(maxStrLen[j], ' '), end = ' ')
        print('')
    return 0

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)