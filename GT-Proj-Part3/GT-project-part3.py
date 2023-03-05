
from treelib import Tree
x=[]
paths=[]
path1=[];path2=[];path3=[];path4=[];path5=[];path6=[];path7=[];path8=[]
tree = Tree()
for i in range (2):
    n=""
    print("please enter player's 1 action: ",n)
    n=input()
    x.append(n)
tree.create_node('root',"player") # The root node 
tree.create_node(x[0],'player1', parent='player')
tree.create_node(x[1], 'player11', parent='player')

for i in range (2):
    n=""
    print("please enter player's 2 action: ",n)
    n=input()
    x.append(n)
tree.create_node(x[2], 'player2', parent='player11')
tree.create_node(x[3], 'player22', parent='player11')
tree.create_node(x[2], 'player222', parent='player1')
tree.create_node(x[3], 'player2222', parent='player1')

for i in range (2):
    n=""
    print("please enter player's 3 action: ",n)
    n=input()
    x.append(n)
tree.create_node(x[4], 'player3', parent='player2')
tree.create_node(x[5], 'player32', parent='player2')
tree.create_node(x[4], 'player33', parent='player22')
tree.create_node(x[5], 'player34', parent='player22')
tree.create_node(x[4], 'player35', parent='player222')
tree.create_node(x[5], 'player36', parent='player222')
tree.create_node(x[4], 'player37', parent='player2222')
tree.create_node(x[5], 'player38', parent='player2222')

tree.show()
def get_paths():
        y=''
        dict_paths = dict([
        ('player', 'root'),
        ('player1', x[0]),
        ('player11', x[1]),
        ('player2', x[2]),
        ('player22', x[3]),
        ('player222', x[2]),
        ('player2222', x[3]),
        ('player3', x[4]),
        ('player32', x[5]),
        ('player33', x[4]),
        ('player34', x[5]),
        ('player35', x[4]),
        ('player36', x[5]),
        ('player37', x[4]),
        ('player38', x[5]),
         ])
        paths=tree.paths_to_leaves()
        for j in range (4):
            y=dict_paths[paths[0][j]]
            path1.append(y)
        for j in range (4):
            y=dict_paths[paths[1][j]]
            path2.append(y)
        for j in range (4):
            y=dict_paths[paths[2][j]]
            path3.append(y)
        for j in range (4):
            y=dict_paths[paths[3][j]]
            path4.append(y)
        for j in range (4):
            y=dict_paths[paths[4][j]] 
            path5.append(y)
        for j in range (4):
            y=dict_paths[paths[5][j]] 
            path6.append(y)
        for j in range (4):
            y=dict_paths[paths[6][j]] 
            path7.append(y)
        for j in range (4):
            y=dict_paths[paths[7][j]] 
            path8.append(y)
            
        
def players_payoff():
    p1=0
    p2=0
    p3=0
    print("please enter player's 1 payoff then player's 2 then player's 3 for path ",path1,":")
    p1=input()
    p2=input()
    p3=input()
    path1.append(p1)
    path1.append(p2)
    path1.append(p3)
    print("please enter player's 1 payoff then player's 2 then player's 3 for path ",path2,":")
    p1=input()
    p2=input()
    p3=input()
    path2.append(p1)
    path2.append(p2)
    path2.append(p3)
    print("please enter player's 1 payoff then player's 2 then player's 3 for path ",path3,":")
    p1=input()
    p2=input()
    p3=input()
    path3.append(p1)
    path3.append(p2)
    path3.append(p3)
    print("please enter player's 1 payoff then player's 2 then player's 3 for path ",path4,":")
    p1=input()
    p2=input()
    p3=input()
    path4.append(p1)
    path4.append(p2)
    path4.append(p3)
    print("please enter player's 1 payoff then player's 2 then player's 3 for path ",path5,":")
    p1=input()
    p2=input()
    p3=input()
    path5.append(p1)
    path5.append(p2)
    path5.append(p3)
    print("please enter player's 1 payoff then player's 2 then player's 3 for path ",path6,":")
    p1=input()
    p2=input()
    p3=input()
    path6.append(p1)
    path6.append(p2)
    path6.append(p3)
    print("please enter player's 1 payoff then player's 2 then player's 3 for path ",path7,":")
    p1=input()
    p2=input()
    p3=input()
    path7.append(p1)
    path7.append(p2)
    path7.append(p3)
    print("please enter player's 1 payoff then player's 2 then player's 3 for path ",path8,":")
    p1=input()
    p2=input()
    p3=input()
    path8.append(p1)
    path8.append(p2)
    path8.append(p3)
    print("path 1 : ",path1)
    print("path 2 : ",path2)
    print("path 3 : ",path3)
    print("path 4 : ",path4)
    print("path 5 : ",path5)
    print("path 6 : ",path6)
    print("path 7 : ",path7)
    print("path 8 : ",path8)
    
def backward_induction():
    newpath1=[]
    newpath2=[]
    newpath3=[]
    newpath4=[]
    newnewpath1=[]
    newnewpath2=[]
    game_solution=[]
    #player 3 is playing
    print("\nplayer 3 is choosing")
    if int(path1[6])>int(path2[6]):
        print("player 3 will choose :",path1)
        newpath1=path1
    elif int(path1[6])<int(path2[6]):
        print("player 3 will choose :",path2)
        newpath1=path2
    if int(path3[6])>int(path4[6]):
        print("player 3 will choose :",path3)
        newpath2=path3
    elif int(path3[6])<int(path4[6]):
        print("player 3 will choose :",path4)
        newpath2=path4
    if int(path5[6])>int(path6[6]):
        print("player 3 will choose :",path5)
        newpath3=path5
    elif int(path5[6])<int(path6[6]):
        print("player 3 will choose :",path6)
        newpath3=path6
    if int(path7[6])>int(path8[6]):
        print("player 3 will choose :",path7)
        newpath4=path7
    elif int(path7[6])<int(path8[6]):
        print("player 3 will choose :",path8)
        newpath4=path8
    #player 2 is playing
    print("\nplayer 2 is choosing")
    if int(newpath1[5])>int(newpath2[5]):
        print("player 2 will choose :",newpath1)
        newnewpath1=newpath1
    elif int(newpath1[5])<int(newpath2[5]):
        print("player 2 will choose :",newpath2)
        newnewpath1=newpath2
    if int(newpath3[5])>int(newpath4[5]):
        print("player 2 will choose :",newpath3)
        newnewpath2=newpath3
    elif int(newpath3[5])<int(newpath4[5]):
        print("player 2 will choose :",newpath4)
        newnewpath2=newpath4
    #player 1 is playing
    print("\nplayer 1 is choosing")
    if int(newnewpath1[4])>int(newnewpath2[4]):
        game_solution=newnewpath1
        print("player 1 will choose :",game_solution)
    else:
        game_solution=newnewpath2
        print("player 1 will choose :",game_solution)
        
whole_game=[]
whole_game=x
subgame1=[x[2],x[3],x[4],x[5],x[4],x[5]]
subgame2=[x[4],x[5]]

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return i, x.index(v)
def pure_nash(player1,player2):
    R=2
    C=2
    n=len(player1)
    index1=[]
    index2=[]
    index_sol=[]
    count=0
    for k in range(n):
        for i in range(n):
            if i!=k:
               for j in range (len(player1[0])):   
                   if (player1[k][j]<=player1[i][j]):       
                       index1.append(index_2d(player1, player1[i][j]))
                   else:
                      index1.append(index_2d(player1, player1[k][j]))

        for i in range(R):
            j=0
            while True:
                if player2[i][j]>=player2[i][j+1]:
                    index2.append(index_2d(player2, player2[i][j]))
                else:
                    index2.append(index_2d(player2, player2[i][j+1]))
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
        nash.append(player1[x][y])
        nash.append(player2[x][y])
        print(nash)    
get_paths()
players_payoff()
backward_induction()