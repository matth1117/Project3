def main():
    import urllib.request
    import re

    data = urllib.request.urlopen('https://s3.amazonaws.com/tcmg476/http_access_log')
    count = 0

    First_Week = 0
    Second_Week = 0
    Third_Week = 0
    Fourth_Week = 0
    Last_Week = 0

    JanCount = 0
    FebCount = 0
    MarCount = 0
    AprCount = 0
    MayCount = 0
    JunCount = 0
    JulCount = 0
    AugCount = 0
    SepCount = 0
    Oct94Count = 0
    Oct95Count = 0
    NovCount = 0
    DecCount = 0

    txtlist = list()

    regex = '(.*?) - (.*) \[(.*?)\] (.*?) (\d+) (\d+)'

    print("Running...")
    
    for line in data:
        #line = line.strip()  
                 
        count += 1
        line = line.decode('utf-8')
        LineMatch = re.match(regex, line).groups()

        txtlist.append(LineMatch)

        print (count, LineMatch)

        #WEEK COUNTING
        if (txtlist[count-1][2][0] == '0'):
            if (txtlist[count-1][2][1] == '1'):
                First_Week += 1
            if (txtlist[count-1][2][1] == '2'):
                First_Week += 1
            if (txtlist[count-1][2][1] == '3'):
                First_Week += 1
            if (txtlist[count-1][2][1] == '4'):
                First_Week += 1
            if (txtlist[count-1][2][1] == '5'):
                First_Week += 1
            if (txtlist[count-1][2][1] == '6'):
                First_Week += 1
            if (txtlist[count-1][2][1] == '7'):
                First_Week += 1

            if (txtlist[count-1][2][1] == '8'):
                Second_Week += 1
            if (txtlist[count-1][2][1] == '9'):
                Second_Week += 1
        if (txtlist[count-1][2][0] == '1'):
            if (txtlist[count-1][2][1] == '0'):
                Second_Week += 1
            if (txtlist[count-1][2][1] == '1'):
                Second_Week += 1
            if (txtlist[count-1][2][1] == '2'):
                Second_Week += 1
            if (txtlist[count-1][2][1] == '3'):
                Second_Week += 1
            if (txtlist[count-1][2][1] == '4'):
                Second_Week += 1

            if (txtlist[count-1][2][1] == '5'):
                Third_Week += 1
            if (txtlist[count-1][2][1] == '6'):
                Third_Week += 1
            if (txtlist[count-1][2][1] == '7'):
                Third_Week += 1
            if (txtlist[count-1][2][1] == '8'):
                Third_Week += 1
            if (txtlist[count-1][2][1] == '9'):
                Third_Week += 1
        if (txtlist[count-1][2][0] == '2'):
            if (txtlist[count-1][2][1] == '0'):
                Third_Week += 1
            if (txtlist[count-1][2][1] == '1'):
                Third_Week += 1

            if (txtlist[count-1][2][1] == '2'):
                Fourth_Week += 1
            if (txtlist[count-1][2][1] == '3'):
                Fourth_Week += 1
            if (txtlist[count-1][2][1] == '4'):
                Fourth_Week += 1
            if (txtlist[count-1][2][1] == '5'):
                Fourth_Week += 1
            if (txtlist[count-1][2][1] == '6'):
                Fourth_Week += 1
            if (txtlist[count-1][2][1] == '7'):
                Fourth_Week += 1
            if (txtlist[count-1][2][1] == '8'):
                Fourth_Week += 1

            if (txtlist[count-1][2][1] == '9'):
                Last_Week += 1
        if (txtlist[count-1][2][0] == '3'):
            if (txtlist[count-1][2][1] == '0'):
                Last_Week += 1
            if (txtlist[count-1][2][1] == '1'):
                Last_Week += 1

        #MONTH COUNTING
        #print (txtlist[count-1][2][3] + txtlist[count-1][2][4] + txtlist[count-1][2][5])
        if (txtlist[count-1][2][3] + txtlist[count-1][2][4] + txtlist[count-1][2][5] == 'Jan'):
            JanCount += 1
        
        if (txtlist[count-1][2][3] + txtlist[count-1][2][4] + txtlist[count-1][2][5] == 'Feb'):
            FebCount += 1

        if (txtlist[count-1][2][3] + txtlist[count-1][2][4] + txtlist[count-1][2][5] == 'Mar'):
            MarCount += 1

        if (txtlist[count-1][2][3] + txtlist[count-1][2][4] + txtlist[count-1][2][5] == 'Apr'):
            AprCount += 1

        if (txtlist[count-1][2][3] + txtlist[count-1][2][4] + txtlist[count-1][2][5] == 'May'):
            MayCount += 1

        if (txtlist[count-1][2][3] + txtlist[count-1][2][4] + txtlist[count-1][2][5] == 'Jun'):
            JunCount += 1

        if (txtlist[count-1][2][3] + txtlist[count-1][2][4] + txtlist[count-1][2][5] == 'Jul'):
            JulCount += 1

        if (txtlist[count-1][2][3] + txtlist[count-1][2][4] + txtlist[count-1][2][5] == 'Aug'):
            AugCount += 1

        if (txtlist[count-1][2][3] + txtlist[count-1][2][4] + txtlist[count-1][2][5] == 'Sep'):
            SepCount += 1

        if (txtlist[count-1][2][3] + txtlist[count-1][2][4] + txtlist[count-1][2][5] == 'Oct' and txtlist[count-1][2][10] == '4'):
            Oct94Count += 1

        if (txtlist[count-1][2][3] + txtlist[count-1][2][4] + txtlist[count-1][2][5] == 'Oct' and txtlist[count-1][2][10] == '5'):
            Oct95Count += 1

        if (txtlist[count-1][2][3] + txtlist[count-1][2][4] + txtlist[count-1][2][5] == 'Nov'):
            NovCount += 1

        if (txtlist[count-1][2][3] + txtlist[count-1][2][4] + txtlist[count-1][2][5] == 'Dec'):
            DecCount += 1




    print("Total number of requests =",count)

    print("Number of requests in October '94 =", Oct94Count)

    print("Total in first week of each month=", First_Week)
    print("Total in second week of each month=", Second_Week)
    print("Total in third week of each month=", Third_Week)
    print("Total in fourth week of each month=", Fourth_Week)
    print("Total in last few days of each month =", Last_Week)
    
main()