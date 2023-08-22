class companyclass:
    companyname = "abc"
    companyregistration = "pvt ltd"
    companyaddress = "xyz"
    companysize = 100
    companylocation = "abcdeh"

    def __init__(self,cname,creg,caddress,csize,clocation):
        self.companyname = cname
        self.companyregistration = creg
        self.companyaddress=caddress
        self.companysize = csize
        self.companylocation = clocation
    def DisplayCompanyDetails(self):
        print("the companydetails are:","\n",self.companyname,"\n",self.companyregistration,"\n",self.companyaddress,"\n",self.companysize,"\n",self.companylocation )
DisplayCompanyDetails()