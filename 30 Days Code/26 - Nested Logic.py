def getFines(da, de):
    dateAct = da[0]
    monthAct = da[1]
    yearAct = da[2]

    dateExp = de[0]
    monthExp = de[1]
    yearExp = de[2]

    fines = 0

    # ditahun yang sama atau sebelumnya
    if yearAct == yearExp:
        # di bulan yang sama dan sebelumnya
        if monthAct == monthExp:
            # di tanggal yang sama dan sebelumnya
            if dateAct > dateExp:
                daysLate = dateAct - dateExp
                fines = 15 * daysLate
        elif monthAct > monthExp:
            monthsLate = monthAct - monthExp
            fines = 500 * monthsLate
    elif yearAct > yearExp:
        fines = 10000

    return fines

if __name__ == '__main__':
    actualDate = []
    expectedDate = []

    actualDate = list(map(int, input().rstrip().split()))
    expectedDate = list(map(int, input().rstrip().split()))
        
    print(getFines(actualDate, expectedDate))