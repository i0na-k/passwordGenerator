import urllib2
import json

def printResults(data):
    theJSON = json.loads(data)
    print "your encrypted password is" + theJSON['md5']


    
def main():
    plaintext = raw_input("enter plaintext to encrypt")
    print plaintext
    urlData ="http://md5.jsontest.com/?text=" + plaintext

    webUrl = urllib2.urlopen(urlData)
    print webUrl.getcode()
    if(webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print "Recieved an error from server, cannot read data" + str(webUrl.getcode())
        
if __name__ == "__main__":
    main()
