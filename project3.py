def main():
    import urllib.request
    import re

    data = urllib.request.urlopen('https://s3.amazonaws.com/tcmg476/http_access_log')
    count = 0
    OctCount = 0
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
        if (txtlist[count-1][2][3] + txtlist[count-1][2][4] + txtlist[count-1][2][5] == 'Oct'):
            OctCount += 1

        #txtlist.append(line, sep='/n')


    print("Total number of requests =",count)
    print("Number of requests in October =", OctCount)
    
main()