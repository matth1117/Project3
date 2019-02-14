def main():
    import urllib.request

    import re

    data = urllib.request.urlopen('https://s3.amazonaws.com/tcmg476/http_access_log')
    count = 0
    txtlist = list()
    regex = '(.*?) - (.*) \[(.*?)\] (.*?) (\d+) (\d+)'

    print("Running...")
    
    for line in data:
        line = line.strip()           
        #print(line)
        count += 1

        line = line.decode('utf-8')

        LineMatch = re.match(regex, line).groups()

        print (count, LineMatch)

        print ()

        if AttributeError == True:
            print ("Attribute error")
            continue

        #txtlist.append(line, sep='/n')


    #print (txtlist)

    print("Total number of requests =",count)
    
main()