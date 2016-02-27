import json

def makeCITimesList():
    #Returns a list that contains all possible check in times. i.e. 23-0, 12-1, etc.
    checkInTimes = []

    for i in range(24):
        for j in range(7):
            checkInTimes.append( str(i)+'-'+str(j) )

    return checkInTimes

def find_peak_ci( json_str ):
    #input is a string representing a full JSON object

    elt = json.loads( json_str )

    #Prepare for loop that will find maximum number of check-ins
    maxCI_num  = 0
    maxCI_time = 'false'

    list_CITimes = makeCITimesList()

    print len(list_CITimes)

    for i in range(len(list_CITimes)):
        #Need to use the list of all possible to look into an individual check in,
        #because we don't know, a priori what check in times are actually in the
        #given object.

        if( list_CITimes[i] in elt ):
            #if a possible time does exist in the JSON object...
            #print 'Something in the list is in the JSON!'

            #Do comparison with max
            if( elt[list_CITimes[i]] > maxCI_num ):
                #if greater than the max, update the max
                maxCI_time = list_CITimes[i]
                maxCI_num  = elt[list_CITimes[i]]
        else:
            #print 'List contains something not in JSON'
            pass

    print 'Peak Number of Check Ins is:' , str( maxCI_num )
    print 'Peak Number of Check Ins occurs at ' + maxCI_time

    return (maxCI_num, maxCI_time)


def main():
    checkIn1_str = '{"23-1": 1, "13-4": 1, "17-6": 1, "15-1": 1, "15-0": 1, "15-2": 2, "15-5": 1, "15-4": 2, "18-3": 1, "18-4": 1, "8-4": 1, "14-0": 1, "14-2": 1, "14-3": 2, "19-5": 1, "19-4": 1, "13-3": 2, "13-2": 2, "13-0": 1, "11-1": 1, "11-0": 2, "11-2": 2, "12-4": 3, "12-2": 1, "9-1": 1, "9-4": 4, "20-4": 1, "10-5": 1, "16-3": 1, "17-5": 1, "17-4": 1, "17-3": 2, "16-4": 1, "16-5": 1, "21-4": 1, "21-5": 1, "10-3": 1, "10-4": 1, "8-1": 2, "21-2": 1, "8-3": 1}'

    find_peak_ci(checkIn1_str)

if __name__ == '__main__':
    main()
