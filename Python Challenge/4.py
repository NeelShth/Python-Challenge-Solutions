#Replace "linkedlist.html" with "linkedlist.php"
#Run "pip install urllib3" in cmd ("pip install urllib" for Python version < 3.x)
#Click on the image in the middle of the page to go to "linkedlist.php?nothing=12345"

import urllib.request

#Page source for "linkedlist.php" recommends only 400 runs of GET requests:
#(as the numbers loop infintely)
#(spolier -> you only need 233 runs)
"""urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
end. 400 times is more than enough."""

#Opening the page source for "linkedlist.php?nothing=12345" shows a pattern of:
"""and the next nothing is XXXXX"""
#which we need to change "nothing={12345}" to, 400 times

request_url = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")

#(Programmer comment) -> this way is hugely inefficient, however, I will try to find a way to make it faster
#(Programmer comment) -> it still works though btw
request_url_num_list = []
for i in range(400):
    request_url_decode = (request_url.read()).decode()
    request_url_num = "".join(char for char in request_url_decode if char.isdigit())
    #If we find a repeat, we have found the loop
    if request_url_num in request_url_num_list:
        break
    #Else, carry on
    request_url_num_list.append(request_url_num)
    request_url = urllib.request.urlopen(f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={request_url_num}")

print(request_url_num_list[-1])
#Now replace "nothing=12345" with "nothing=66831"
#Now replace "linkedlist.php?nothing=66831" with "peak.html"
