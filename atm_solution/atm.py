
request = 452   # Amount to be extracted
money   = 700   # Full amount

paper_200 = 0   # count paper 200
paper_100 = 0   # count paper 100
paper_50  = 0   # count paper 50
paper_10  = 0   # count paper 10
paper_5   = 0   # count paper 5
rest      = 0   # count rest


print "The number of amount is:"+str(money)
if request > money or request < 0:
    print """
           There is a problem , \n
           that the amount entered may be greater than the total amount,\n 
           or the amount entered will take a negative number 
           """
else:
    print "The amount that will remain in your account :" + str(money - request)
    while request > 0:
        if request >= 200:
            request -= 200
            paper_200 += 1
            print "give 200$"
        elif request >= 100:
            request -= 100
            paper_100 +=1
            print "give 100$"
        elif request >=50:
            request -= 50
            paper_50 += 1
            print "give 50$"
        elif request >= 10:
            paper_10 += 1
            request -= 10
            print "give 10$"
        elif request>=5:
            request -= 5
            paper_5 += 1
            print "give 5$"
        else:
            rest+=1
            print"give "+str(request)+"$"
            request = 0
            # or used break , but break is a bomb 


    if paper_200 > 0:
        print "count paper 200$ : "+  str(paper_200) +" papers"
    if paper_100 > 0:
        print "count paper 100$ : "+  str(paper_100) +" papers"
    if paper_50 > 0:
        print "count paper 50$ : "+ str(paper_50) + " papers"
    if paper_10 > 0:
        print "count paper 10$ : " + str(paper_10) + " papers"
    if paper_5 > 0:
        print "count paper 5$ : " + str(paper_5) +" papers"
    if rest > 0:
            print "rest : " + str(rest)
