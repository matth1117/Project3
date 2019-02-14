def main():
    import urllib.request
    import re

    data = urllib.request.urlopen('https://s3.amazonaws.com/tcmg476/http_access_log')
    count = 0
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
        print (txtlist[count-1][2][3] + txtlist[count-1][2][4] + txtlist[count-1][2][5])
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

        print("Number of requests in October '94 =", Oct94Count)



    print("Total number of requests =",count)
    print("Number of requests in October '94 =", Oct94Count)
    
main()