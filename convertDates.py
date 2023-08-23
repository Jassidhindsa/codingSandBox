


def convertDates(dates):
    months = {"jan": "01", "feb": "02", "mar": "03", "apr": "04", "may": "05", "jun": "06", "jul": "07", "aug": "08", "sep": "09",
              "oct": "10", "nov": "11", "dec": "12"}
    finallDates = []


    for date in dates:
        splitDateInfo = date.split(" ")
        day = ""
        for i in splitDateInfo[0]:
            if i.isdigit():
                day += i
            else:
                break
        month = months[splitDateInfo[1].lower()]
        tempDate = splitDateInfo[2] + "-" + month + "-" + day

        finallDates.append(tempDate)
    
    return finallDates
