def main():
    import urllib.request

    data = urllib.request.urlopen('https://s3.amazonaws.com/tcmg476/http_access_log')
    count = 0
    txtlist = list()
    
    print("sup")

    for line in data:
        line = line.strip()           
        #print(line)
        count += 1
        
        #if (count == 3):
        #    print ("line{0 =" line[0])
        #    print ("line{1 =" line[1])
        #    print ("line{2 =" line[2])
        #    print ("line{3 =" line[3])
        #    print ("line{4 =" line[4])
        #    print ("line{5 =" line[5])
        #    print ("line{6 =" line[6])
        #    print ("line{7 =" line[7])
        #    print ("line{8 =" line[8])
        #    print ("line{9 =" line[9])
        #    print ("line{10 =" line[10])
        #    print ("line{11 =" line[11])

        txtlist.append(line)


    print (txtlist[0][1])

    print("Total number of requests =",count)
    
main()