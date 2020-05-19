from time import *  
from datetime import *  
host_path = r"/etc/hosts"  
redirect = "127.0.0.1"  
websites = ["www.facebook.com", "https://www.facebook.com"]  
while True:  
	if datetime(datetime.now().year,datetime.now().month,datetime.now().day,9)<datetime.now()<datetime(datetime.now().year,datetime.now().month,datetime.now().day,17):  
		print("working hours")  
		with open(host_path,"r+") as fileptr:  
                	content = fileptr.read()  
                for website in websites:  
                	if website in content:  
                	        pass  
                	else:  
                        	fileptr.write(redirect+"    "+website+"\n")  
	else:  
        	print("Fun hours")  
sleep(5)  
