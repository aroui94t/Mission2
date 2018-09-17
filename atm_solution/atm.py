

# This part is for Workshop 8:
# Start code Workshop 8:
def withdraw(balance, request):
    list_order = []
    list_paper = [200, 100, 50, 10, 5, 2, 1]
    index = 0
    if request > balance or request <= 0:
        print """
                    There is a problem , \n
                    that the amount entered may be greater than the total amount,\n
                    or the amount entered will take a negative number
              """
    else:
        while index < len(list_paper):
            while request >= list_paper[index]:
                request -= list_paper[index]
                list_order.append(list_paper[index])
            index+=1

        for count in list_paper:
            if list_order.count(count) >= 1:
                print "give " + str(count)+"$ ===> number paper : " + str(list_order.count(count))
    return "Current balance :" + str(balance - sum(list_order))

print withdraw(740,424)
# End code Workshop 8

#========================================================================================================


# This part is for Workshop 10:
# Start code Workshop 10:

""" 
Define class ATM :
        methods => withdraw

"""
class ATM :

    def __init__(self,name_bank,balance):
        self.bank    =  name_bank
        self.balance =  balance

    def withdraw(self,request):

        print "="*len("Current balance = " + str(self.balance))
        print "Welcome to " + self.bank
        print "Current balance = " + str(self.balance)
        print "=" * len("Current balance = " + str(self.balance))


        list_order = []
        list_paper = [200, 100, 50, 10, 5, 2, 1]
        index = 0

        if request > self.balance or request <= 0:
            print """
                    There is a problem , \n
                    that the amount entered may be greater than the total amount,\n
                    or the amount entered will take a negative number
                  """
        else:
            while index < len(list_paper):
                while request >= list_paper[index]:
                    request -= list_paper[index]
                    list_order.append(list_paper[index])
                index+=1

            for count in list_paper:
                if list_order.count(count) >= 1:
                    print "give " + str(count)+"$ ===> number paper : " + str(list_order.count(count))
        print "="*len("Current balance :" + str(self.balance - sum(list_order)))
        print "Current balance :" + str(self.balance - sum(list_order))
        print "="*len("Current balance :" + str(self.balance - sum(list_order)))
        
# if want how to create objects , go to file main.py         


