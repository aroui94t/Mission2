# This part is for Workshop 12:
# Start code Workshop 12:

""" 
Define class ATM :
        
        methods:
                pablic:
                  ==> withdraw
                  ==> display_withdrawals
                private:
                  ==> __add_in_withdrawals
                  ==> __process_request  
 
"""
class ATM :

    def __init__(self,name_bank,balance):
        self.bank    =  name_bank
        self.balance =  balance
        self.__withdrawals_dict = {}

    def __add_in_withdrawals(self,paper,count):
    	  self.__withdrawals_dict[paper]:count    

    
    def __process_request(self,request):
        list_order = []
        list_paper = [200, 100, 50, 10, 5, 2, 1]
        index = 0
        while index < len(list_paper):
                while request >= list_paper[index]:
                    request -= list_paper[index]
                    list_order.append(list_paper[index])
                index+=1

            for count in list_paper:
                if list_order.count(count) >= 1:
                	  self.__add_in_withdrawals(count,list_order.count(count))	
                    print "give " + str(count)+"$ ===> number paper : " + str(list_order.count(count))
            
            print "="*len("Current balance :" + str(self.balance - sum(list_order)))
            print "Current balance :" + str(self.balance - sum(list_order))
            print "="*len("Current balance :" + str(self.balance - sum(list_order)))
    
    

    def withdraw(self,request):

        print "="*len("Current balance = " + str(self.balance))
        print "Welcome to " + self.bank
        print "Current balance = " + str(self.balance)
        print "=" * len("Current balance = " + str(self.balance))
       
        if request > self.balance or request <= 0:
            print """
                    There is a problem , \n
                    that the amount entered may be greater than the total amount,\n
                    or the amount entered will take a negative number
                  """
        else:
            self.__process_request(request)
      
    def display_withdrawals(self):
        if len(self.__withdrawals_dict) == 0:
            print "There is no extract amount"
        else:
            s = (key*value for key,value in self.__withdrawals_dict.items())
            print "Amount extracted : " + str(sum(s))
            print "Papers extracted :"
            for paper, count in self.__withdrawals_dict.items():
                print "paper ==> :" + str(paper), "count ==> :" + str(count)


# End code Workshop 12        
# if want how to create objects , go to file main.py         


