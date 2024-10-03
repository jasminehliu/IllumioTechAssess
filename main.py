import csv

class main:
    def parseLookup(self, lookup):
        lookupDict = dict()
        with open(lookup, mode='r') as file:
            fileLines = file.readlines()
            for i, line in enumerate(fileLines):
                if i == 0:
                    continue
                else:
                    elements = line.split(",")
                    lookupDict[elements[0].strip().lower()] = [elements[1].strip().lower(), elements[2].strip().lower()]
        return lookupDict

    def mapTag(self, dstPort):
        protocol = None
        tag = None
        # count tags
        if dstPort in self.lookupTable:
            dstPortMap = self.lookupTable[dstPort]
            protocol = dstPortMap[0]
            tag = dstPortMap[1]
            if tag in self.TagCount:
                self.TagCount[tag] += 1
            else:
                self.TagCount[tag] = 1
        else:
            self.TagCount["Untagged"] += 1
        # count combinations
        if dstPort in self.PortProtCount:
            if protocol in self.PortProtCount[dstPort]:
                self.PortProtCount[dstPort][protocol] += 1
            else:
                self.PortProtCount[dstPort][protocol] = 1
        else:
            self.PortProtCount[dstPort] = {protocol : 1}

    def parseInput(self, inputTable):
        with open(inputTable, mode='r') as file:
            fileLines = file.readlines()
            for line in fileLines:
                elements = line.split(" ")
                dstPort = elements[5].lower()
                self.mapTag(dstPort)
    
    def writeToFile(self):
        f = open("output.txt", "w")
        f.write("Tag Counts:\n")
        f.write("Tag,Count\n")
        for tag in self.TagCount:
            f.write(tag + "," + str(self.TagCount[tag]) + "\n")
        f.write("\n")
        f.write("Port/Protocol Combination Counts: \n")
        f.write("Port,Protocol,Count\n")
        for dstport in self.PortProtCount:
            protocols = self.PortProtCount[dstport]
            for protocol in protocols:
                f.write(dstport + "," + str(protocol) + "," + str(protocols[protocol]) + "\n")
        

    def mapLogData(self, input, lookup):
        self.TagCount = {"Untagged" : 0} # tag : count
        self.PortProtCount = dict() # dstport : {protocol : count}
        self.lookupTable = self.parseLookup(lookup) # dstport : protocol, tag
        self.parseInput(input)
        self.writeToFile()

main().mapLogData("input.txt", "lookup.csv")

