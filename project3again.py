def main():
    import urllib.request
    import re

    data = urllib.request.urlopen('https://s3.amazonaws.com/tcmg476/http_access_log')
    count = 0

    Day_1 = 0
    Day_2 = 0
    Day_3 = 0
    Day_4 = 0
    Day_5 = 0
    Day_6 = 0
    Day_7 = 0
    Day_8 = 0
    Day_9 = 0
    Day_10 = 0
    Day_11 = 0
    Day_12 = 0
    Day_13 = 0
    Day_14 = 0
    Day_15 = 0
    Day_16 = 0
    Day_17 = 0
    Day_18 = 0
    Day_19 = 0
    Day_20 = 0
    Day_21 = 0
    Day_22 = 0
    Day_23 = 0
    Day_24 = 0
    Day_25 = 0
    Day_26 = 0
    Day_27 = 0
    Day_28 = 0
    Day_29 = 0
    Day_30 = 0
    Day_31 = 0   

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

    ThreeXXCount = 0
    FourXXCount = 0

    LineErrors = 0

    txtlist = list()

    regex = '(.*?) - (.*) \[(.*?)\] (.*?) (\d+) (\d+)'

    print("Running...")
    
    for line in data:

        count += 1

        try:
            #line = line.strip()  
                    
            line = line.decode('utf-8')
            LineMatch = re.match(regex, line).groups()

            txtlist.append(LineMatch)

            #print (count, LineMatch)

            #print("Linematch2", LineMatch[2])
            #print("errors:", LineErrors)

            #WEEK and DAY COUNTING
            if (LineMatch[2][0] == '0'):
                if (LineMatch[2][1] == '1'):
                    First_Week += 1
                    Day_1 += 1
                if (LineMatch[2][1] == '2'):
                    First_Week += 1
                    Day_2 += 1
                if (LineMatch[2][1] == '3'):
                    First_Week += 1
                    Day_3 += 1
                if (LineMatch[2][1] == '4'):
                    First_Week += 1
                    Day_4 += 1
                if (LineMatch[2][1] == '5'):
                    First_Week += 1
                    Day_5 += 1
                if (LineMatch[2][1] == '6'):
                    First_Week += 1
                    Day_6 += 1
                if (LineMatch[2][1] == '7'):
                    First_Week += 1
                    Day_7 += 1

                if (LineMatch[2][1] == '8'):
                    Second_Week += 1
                    Day_8 += 1
                if (LineMatch[2][1] == '9'):
                    Second_Week += 1
                    Day_9 += 1
            if (LineMatch[2][0] == '1'):
                if (LineMatch[2][1] == '0'):
                    Second_Week += 1
                    Day_10 += 1
                if (LineMatch[2][1] == '1'):
                    Second_Week += 1
                    Day_11 += 1
                if (LineMatch[2][1] == '2'):
                    Second_Week += 1
                    Day_12 += 1
                if (LineMatch[2][1] == '3'):
                    Second_Week += 1
                    Day_13 += 1
                if (LineMatch[2][1] == '4'):
                    Second_Week += 1
                    Day_14 += 1

                if (LineMatch[2][1] == '5'):
                    Third_Week += 1
                    Day_15 += 1
                if (LineMatch[2][1] == '6'):
                    Third_Week += 1
                    Day_16 += 1
                if (LineMatch[2][1] == '7'):
                    Third_Week += 1
                    Day_17 += 1
                if (LineMatch[2][1] == '8'):
                    Third_Week += 1
                    Day_18 += 1
                if (LineMatch[2][1] == '9'):
                    Third_Week += 1
                    Day_19 += 1
            if (LineMatch[2][0] == '2'):
                if (LineMatch[2][1] == '0'):
                    Third_Week += 1
                    Day_20 += 1
                if (LineMatch[2][1] == '1'):
                    Third_Week += 1
                    Day_21 += 1

                if (LineMatch[2][1] == '2'):
                    Fourth_Week += 1
                    Day_22 += 1
                if (LineMatch[2][1] == '3'):
                    Fourth_Week += 1
                    Day_23 += 1
                if (LineMatch[2][1] == '4'):
                    Fourth_Week += 1
                    Day_24 += 1
                if (LineMatch[2][1] == '5'):
                    Fourth_Week += 1
                    Day_25 += 1
                if (LineMatch[2][1] == '6'):
                    Fourth_Week += 1
                    Day_26 += 1
                if (LineMatch[2][1] == '7'):
                    Fourth_Week += 1
                    Day_27 += 1
                if (LineMatch[2][1] == '8'):
                    Fourth_Week += 1
                    Day_28 += 1

                if (LineMatch[2][1] == '9'):
                    Last_Week += 1
                    Day_29 += 1
            if (LineMatch[2][0] == '3'):
                if (LineMatch[2][1] == '0'):
                    Last_Week += 1
                    Day_30 += 1
                if (LineMatch[2][1] == '1'):
                    Last_Week += 1
                    Day_31 += 1

            #MONTH COUNTING
            #print (txtlist[count-1][2][3] + txtlist[count-1][2][4] + txtlist[count-1][2][5])
            if (LineMatch[2][3] + LineMatch[2][4] + LineMatch[2][5] == 'Jan'):
                JanCount += 1
            
            if (LineMatch[2][3] + LineMatch[2][4] + LineMatch[2][5] == 'Feb'):
                FebCount += 1

            if (LineMatch[2][3] + LineMatch[2][4] + LineMatch[2][5] == 'Mar'):
                MarCount += 1

            if (LineMatch[2][3] + LineMatch[2][4] + LineMatch[2][5] == 'Apr'):
                AprCount += 1

            if (LineMatch[2][3] + LineMatch[2][4] + LineMatch[2][5] == 'May'):
                MayCount += 1

            if (LineMatch[2][3] + LineMatch[2][4] + LineMatch[2][5] == 'Jun'):
                JunCount += 1

            if (LineMatch[2][3] + LineMatch[2][4] + LineMatch[2][5] == 'Jul'):
                JulCount += 1

            if (LineMatch[2][3] + LineMatch[2][4] + LineMatch[2][5] == 'Aug'):
                AugCount += 1

            if (LineMatch[2][3] + LineMatch[2][4] + LineMatch[2][5] == 'Sep'):
                SepCount += 1

            if (LineMatch[2][3] + LineMatch[2][4] + LineMatch[2][5] == 'Oct' and LineMatch[2][10] == '4'):
                Oct94Count += 1

            if (LineMatch[2][3] + LineMatch[2][4] + LineMatch[2][5] == 'Oct' and LineMatch[2][10] == '5'):
                Oct95Count += 1

            if (LineMatch[2][3] + LineMatch[2][4] + LineMatch[2][5] == 'Nov'):
                NovCount += 1

            if (LineMatch[2][3] + LineMatch[2][4] + LineMatch[2][5] == 'Dec'):
                DecCount += 1


            #3xx & 4xx CODE COUNT
            if (LineMatch[4][0] == '3'):
                ThreeXXCount += 1
            if (LineMatch[4][0] == '4'):
                FourXXCount += 1
        
        except AttributeError:
            LineErrors += 1



    print("\n\nTotal number of requests =",count)

    print("\nNumber of requests in January =", JanCount)
    print("Number of requests in February =", FebCount)
    print("Number of requests in March =", MarCount)
    print("Number of requests in April =", AprCount)
    print("Number of requests in May =", MayCount)
    print("Number of requests in June =", JunCount)
    print("Number of requests in July =", JulCount)
    print("Number of requests in August =", AugCount)
    print("Number of requests in September =", SepCount)
    print("Number of requests in October '94 =", Oct94Count)
    print("Number of requests in October '95 =", Oct95Count)
    print("Number of requests in November =", NovCount)
    print("Number of requests in December =", DecCount)

    print("\nTotal in first week of each month=", First_Week)
    print("Total in second week of each month=", Second_Week)
    print("Total in third week of each month=", Third_Week)
    print("Total in fourth week of each month=", Fourth_Week)
    print("Total in last few days of each month =", Last_Week)

    print("\nDay 1 =", Day_1)
    print("Day 2 =", Day_2)
    print("Day 3 =", Day_3)
    print("Day 4 =", Day_4)
    print("Day 5 =", Day_5)
    print("Day 6 =", Day_6)
    print("Day 7 =", Day_7)
    print("Day 8 =", Day_8)
    print("Day 9 =", Day_9)
    print("Day 10 =", Day_10)
    print("Day 11 =", Day_11)
    print("Day 12 =", Day_12)
    print("Day 13 =", Day_13)
    print("Day 14 =", Day_14)
    print("Day 15 =", Day_15)
    print("Day 16 =", Day_16)
    print("Day 17 =", Day_17)
    print("Day 18 =", Day_18)
    print("Day 19 =", Day_19)
    print("Day 20 =", Day_20)
    print("Day 21 =", Day_21)
    print("Day 22 =", Day_22)
    print("Day 23 =", Day_23)
    print("Day 24 =", Day_24)
    print("Day 25 =", Day_25)
    print("Day 26 =", Day_26)
    print("Day 27 =", Day_27)
    print("Day 28 =", Day_28)
    print("Day 29 =", Day_29)
    print("Day 30 =", Day_30)
    print("Day 31 =", Day_31)
    

    print("\nPercentage of 3xx codes = ", "{:.4%}".format(ThreeXXCount / count))
    print("Percentage of 4xx codes =", "{:.4%}".format(FourXXCount / count))

    print("\nTotal line errors =", LineErrors)


main()  