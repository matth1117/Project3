def main():
    import urllib.request

    import re

    data = urllib.request.urlopen('https://s3.amazonaws.com/tcmg476/http_access_log')
    count = 0
    txtlist = list()
    
    print("Running...")
    
    for line in data:
        line = line.strip()           
        #print(line)
        count += 1

        print (re.match(regex, line).groups())     

        #txtlist.append(line, sep='/n')


    #print (txtlist)

    print("Total number of requests =",count)
    
main()