def main():
    import urllib.request
    
    data = urllib.request.urlopen('https://s3.amazonaws.com/tcmg476/http_access_log')
    count = 0
    
    print("sup")

    for line in data:
        line = line.strip()           
        #print(line)
        count += 1
        
    print("Count =",count)
    
main()