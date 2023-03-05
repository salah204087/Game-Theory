R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix1 = []
matrix2 = []
print("Enter the entries player 1 by row:")
for i in range(R):          
    a =[]
    for j in range(C):      
         a.append(int(input()))
    matrix1.append(a)
print("Enter the entries player 2 by row:")
for i in range(R):        
    a =[]
    for j in range(C):      
         a.append(int(input()))
    matrix2.append(a)
print(matrix1)
print(matrix2)

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return i, x.index(v)
    

def strictly_dominated(player1,player2):
    payoff1=player1.copy()
    payoff2=player2.copy()
    n=len(payoff1)
    arr=[]
    ar=[]
    
    for k in range(n):
        for i in range(n):
            check1=0
            check2=0
            if i!=k:
               for j in range (len(payoff1[0])):   
                   if (payoff1[k][j]<payoff1[i][j]):       
                       check1+=1
                   else:
                      check2+=1
            if check1==len(payoff1[0]):
                if not payoff1[k] in arr: 
                    arr.append(payoff1[k])
                    ar.append(payoff2[k])
            elif check2==len(payoff1[0]):
                if not payoff1[i] in arr: 
                    arr.append(payoff1[i])
                    ar.append(payoff2[i])
    
    for i in arr:
        payoff1.remove(i)
    for i in ar:
        payoff2.remove(i)

    for i in range(len(payoff2)):
        check=0
        max_value=0
        max_value=max(payoff2[i])
        for j in range(len(payoff2[i])):
            if max_value==payoff2[i][j]:
                check+=1
        if check==1:
            max_index=payoff2[i].index(max_value)
            payoff2[i]=max_value
            payoff1[i]=payoff1[i][max_index]
    
    return payoff1,payoff2
   
#print(strictly_dominated(player1, player2))

def  weakly_dominated(player1,player2):
    payoff1=player1.copy()
    payoff2=player2.copy()
    n=len(payoff1)
    arr=[]
    ar=[]
    for k in range(n):
        for i in range(n):
            check1=0
            check2=0
            if i!=k:
               for j in range (len(payoff1[0])):   
                   if (payoff1[k][j]<=payoff1[i][j]):
                       check1+=1
                   else:
                      check2+=1
            if check1==len(payoff1[0]):
                if not payoff1[k] in arr: 
                    arr.append(payoff1[k])
                    ar.append(payoff2[k])
            elif check2==len(payoff1[0]):
                if not payoff1[i] in arr: 
                    arr.append(payoff1[i])
                    ar.append( payoff2[i])
    
    for i in arr:
        payoff1.remove(i)
    for i in ar:
         payoff2.remove(i)
    for i in range(len( payoff2)):
    
        max_value=0
        max_value=max( payoff2[i])
        max_index= payoff2[i].index(max_value)
        payoff2[i]=max_value
        payoff1[i]=payoff1[i][max_index]
    
    return payoff1, payoff2    
#print(weakly_dominated(player1, player2))

def pure_nash(player1,player2):
    payoff1=player1.copy()
    payoff2=player2.copy()
    n=len(payoff1)
    index1=[]
    index2=[]
    index_sol=[]
    count=0
    all_nash=[]
    for k in range(n):
        for i in range(n):
            if i!=k:
               for j in range (len(payoff1[0])):   
                   if (payoff1[k][j]<=payoff1[i][j]):       
                       index1.append(index_2d(payoff1, payoff1[i][j]))
                   else:
                      index1.append(index_2d(payoff1, payoff1[k][j]))

        for i in range(R):
            j=0
            while True:
                if  payoff2[i][j]>= payoff2[i][j+1]:
                    index2.append(index_2d( payoff2,  payoff2[i][j]))
                else:
                    index2.append(index_2d( payoff2,  payoff2[i][j+1]))
                count+=1
                if count>=C:
                    break
                    
    for i in range(len(index1)):
        for j in range(len(index2)):
            if (index1[i]==index2[j]):
                if index1[i] in index_sol:
                    continue
                else:
                    index_sol.append(index1[i])
    for i in range(len(index_sol)):
        nash=[]
        x=index_sol[i][0]
        y=index_sol[i][1]
        nash.append(payoff1[x][y])
        nash.append( payoff2[x][y])
        all_nash.append(nash)
    return all_nash
                  
#print(pure_nash(player1, player2))

def pure_strict_nash(player1,player2):
    payoff1=player1.copy()
    payoff2=player2.copy()
    n=len(payoff1)
    index1=[]
    index2=[]
    index_sol=[]
    count=0
    all_nash=[]
    for k in range(n):
        for i in range(n):
            if i!=k:
               for j in range (len(payoff1[0])):   
                   if (payoff1[k][j]<payoff1[i][j]):       
                       index1.append(index_2d(payoff1, payoff1[i][j]))
                   else:
                      index1.append(index_2d(payoff1, payoff1[k][j]))

        for i in range(R):
            j=0
            while True:
                if payoff2[i][j]>payoff2[i][j+1]:
                    index2.append(index_2d(payoff2, payoff2[i][j]))
                else:
                    index2.append(index_2d(payoff2, payoff2[i][j+1]))
                count+=1
                if count>=C:
                    break
                    
    for i in range(len(index1)):
        for j in range(len(index2)):
            if (index1[i]==index2[j]):
                if index1[i] in index_sol:
                    continue
                else:
                    index_sol.append(index1[i])
    for i in range(len(index_sol)):
        nash=[]
        x=index_sol[i][0]
        y=index_sol[i][1]
        nash.append(payoff1[x][y])
        nash.append(payoff2[x][y])
        all_nash.append(nash)
    return all_nash
#print(pure_strict_nash(player1, player2))
def  trembling_hand(player1,player2):
    payoff1=player1.copy()
    payoff2=player2.copy()
    nash=[]
    index1=[]
    index2=[]
    mistake=0.0
    while True:
        print("enter the value of mistake (should be a small value <0.05 )")
        mistake=float(input())
        if mistake<0.05:
            break
        else:
            print("please enter valued value")
    for i in range(len(pure_nash(payoff1, payoff2))):
        nash.append(pure_nash(payoff1, payoff2)[i])
    print(nash)
    for i in range(len(nash)):
        x=0
        y=0
        q=0
        w=0
        count=0
        for j in range(2):
            if j==0:
                index1.append(index_2d(payoff1, nash[i][j]))
                x1=index1[i][0]
                y1=index1[i][1]
            else:
                index2.append(index_2d(payoff2, nash[i][j]))
                x2=index2[i][0]
                y2=index2[i][1]
        for j in range(C):
            if j==y1:
                x+=payoff1[0][y1]*(1-mistake)
            else:
                x+=payoff1[0][j]*mistake
        for j in range(C):
            if j==y1:
                y+=payoff1[1][y1]*(1-mistake)
            else:
                y+=payoff1[1][j]*mistake
        if x>y and x1==0:
            count+=1
        else:
            count+=1
        for j in range(R):
            if i==x2:
                q+=payoff2[x2][0]*(1-mistake)
            else:
                q+=payoff2[i][0]*mistake
        for j in range(C):
            if j==y1:
                w+=payoff2[x2][1]*(1-mistake)
            else:
                w+=payoff2[i][1]*mistake
        if q>w and y2==0:
            count+=1
        else:
            count+=1
    if (count==2):
        print("the game is trembling hand perfection")
    else:
        print("the game is not trembling hand perfection")
                
            
            
#trembling_hand(player1, player2)
    
def positive_affine(player1,player2):
    payoff1=player1.copy()
    payoff2=player2.copy()
    while True:
        print("enter λ1:")
        y1=int(input())
        if y1>0:
            break
        else:
            print("please enter positive value")
    print("enter µ1 ")
    u1=int(input())
    while True:
        print("enter λ2:")
        y2=int(input())
        if y2>0:
            break
        else:
            print("please enter positive value")
    print("enter µ2 ")
    u2=int(input())
        
    for i in range(R):
        for j in range(C):
            payoff1[i][j]= payoff1[i][j]*y1+u1
            payoff2[i][j]=payoff2[i][j]*y2+u2
    return  payoff1,payoff2
#print (positive_affine(player1, player2))

def category1(player1):
    payoff1=player1.copy()
    if (R==2 and C==2):
        a1=payoff1[0][0]-payoff1[1][0]
        a2=payoff1[1][1]-payoff1[0][1]
        if (a1<0 and a2>0):
            return "player1 in category 1"
        elif(a1>0 and a2>0):
            return "player1 in category 2"
        elif(a1<0 and a2<0):
            return "player 1 in category 3"
        elif(a1>0 and a2<0):
            return "player 1 in category 4"
    else:
        return "you entered invalid matrix"
#print(category1(player1))

def category2(player2):
    payoff2=player2.copy()
    if (R==2 and C==2):
        b1=payoff2[0][0]-payoff2[1][0]
        b2=payoff2[1][1]-payoff2[0][1]
        if (b1<0 and b2>0):
            return "player2 in category 1"
        elif(b1>0 and b2>0):
            return "player2 in category 2"
        elif(b1<0 and b2<0):
            return "player 2 in category 3"
        elif(b1>0 and b2<0):
            return "player 2 in category 4"
    else:
        return "you entered invalid matrix"
#print(category2(player2))
       
def expected_payoff(player1,player2):
    payoff1=player1.copy()
    payoff2=player2.copy()
    if (R==2 and C==2):
        while True:
            print("enter a mixed strategy x for player 1 less than or equal 1:")
            x=float(input())
            if (x<=1):
                break
            else:
                print("please enter valid value")
        while True:
            print("enter a mixed strategy y for player 2 less than or equal 1:")
            y=float(input())
            if (y <=1):
                break
            else:
                print("please enter valid value")
        row1=(y*payoff1[0][0])+((1-y)*payoff1[0][1])
        row2=(y*payoff1[1][0])+((1-y)*payoff1[1][1])
        column1=(x*payoff2[0][0])+((1-x)*payoff2[1][0])
        column2=(x*payoff2[0][1])+((1-x)*payoff2[1][1])
        print("player 1 will play strategy 1 by expected value:")
        print(row1)
        print("player 1 will play strategy 2 by expected value:")
        print(row2)
        print("player 2 will play strategy 1 by expected value:")
        print(column1)
        print("player 2 will play strategy 2 by expected value:")
        print(column2)
    else:
        print("you entered invalid matrix")
#expected_payoff(player1, player2)
while True:
    print("\n1-strictly dominated\n2-weakly dominated\n3-pure Nash equilibria\n4-pure strict Nash\n5-expected payoff\n6-trembling hand perfect\n7-positive affine transformation\n8-categoty of players\n9-Exit\n")
    choice=int(input("Enter your choice:"))
    if (choice==1):
        print(strictly_dominated(matrix1, matrix2))
    elif(choice==2):
        print(weakly_dominated(matrix1, matrix2))
    elif(choice==3):
        print(pure_nash(matrix1, matrix2))
    elif(choice==4):
        print(pure_strict_nash(matrix1, matrix2))
    elif(choice==5):
        expected_payoff(matrix1, matrix2)
    elif(choice==6):
        trembling_hand(matrix1, matrix2)
    elif(choice==7):
        print(positive_affine(matrix1, matrix2))
    elif(choice==8):
        print(category1(matrix1))
        print(category2(matrix2))
    else:
        break