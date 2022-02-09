def convertMillis(millis):
    totalSeconds = int(millis / 1000)
    seconds = int(totalSeconds % 60)
    totalMinutes = (totalSeconds - seconds) / 60
    minutes = int(totalMinutes % 60)
    hours = int((totalMinutes - minutes) /60)
    return (str(hours) + ':' + str(minutes) +':' + str(seconds))

milliseconds = input("Enter a time in milliseconds: ")
print(convertMillis(int(milliseconds)))
