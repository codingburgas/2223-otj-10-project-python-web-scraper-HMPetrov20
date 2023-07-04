import requests
from bs4 import BeautifulSoup

class Computer:
    #constructor
    def __init__(self, cpu, gpu, ram, memory, warranty):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.memory = memory
        self.warranty = warranty

    #display method
    def display(self):
        print("CPU: " + self.cpu)
        print("GPU: " + self.gpu)
        print("RAM: " + self.ram)
        print("Memory: " + self.memory)
        print("Warranty: " + self.warranty)
        print()

URL = "https://ardes.bg/kompyutri/nastolni-kompyutri/za-igri-gaming?sort=default&direction=asc&_gl=1*1nx3ljv*_up*MQ..&gclid=EAIaIQobChMI-OH5yb30_wIVHZGDBx1YmQZDEAAYASAAEgIV-vD_BwE"
page = requests.get(URL)

#Get HTML
soup = BeautifulSoup(page.content, "html.parser")

#Get price HTML
pricesPC = soup.find_all("span", class_="price-num")
#Strip price HTML
pricePC = [x.get_text(strip=True)[:-2] for x in pricesPC]

#Get unordered list of specifications
dataPC = soup.find_all("ul", class_="parameters list-unstyled parameters-ellipsis")

priceNumber = 0
pcNumber = 1

for pcSpecsAll in dataPC:
    #Get all <li> tags in the <ul> tag
    pcSpecs = pcSpecsAll.find_all("li")
    print("PC", pcNumber)
    pcSpecsLen = len(pcSpecs)
    if pcSpecsLen == 5:

        #Strip Specifications
        line1 = pcSpecs[0]['title']
        line2 = pcSpecs[1]['title']
        line3 = pcSpecs[2]['title']
        line4 = pcSpecs[3]['title']
        line5 = pcSpecs[4]['title']

        #Gives the specifications to the constructor
        com = Computer(line1, line2, line3, line4, line5)

        #Print price
        print("Price:", pricePC[priceNumber][:-2], "лв")

        #Print specifications
        com.display()

        pcNumber += 1
        priceNumber += 1

    #Account for 2 memory modules    
    elif pcSpecsLen == 6:

        #Strip Specifications
        line1 = pcSpecs[0]['title']
        line2 = pcSpecs[1]['title']
        line3 = pcSpecs[2]['title']
        line4 = pcSpecs[3]['title']
        line5 = pcSpecs[4]['title']
        line6 = pcSpecs[5]['title']

        #Gives the specifications to the constructor
        com = Computer(line1, line2, line3, line4 + " | " + line5, line6)

        #Print price
        print("Price:", pricePC[priceNumber][:-2], "лв")

        #Print specifications
        com.display()
        
        pcNumber += 1
        priceNumber += 1