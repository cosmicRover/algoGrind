def play(arr):
    tScore = 0; jScore = 0
    width = len(arr[0])
    maxVals = []

    #store the max values on each column
    for i in range(width):
        column = [row[i] for row in arr]
        maxVals.append(max(column))

    #sort in descending order since we care about the bigger numbers first
    maxVals.sort(reverse = True)

    #start playing
    tTurn = True
    
    #keep looping and getting the bigger values according to payer's turn
    for i in range(len(maxVals)):
        if tTurn: 
            tScore += maxVals[i]; tTurn = False
        elif not tTurn:
            jScore += maxVals[i]; tTurn = True

    return abs(tScore - jScore)