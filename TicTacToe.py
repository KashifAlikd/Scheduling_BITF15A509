import os #To clear console
name1="PLayer1 "
name2="Player2 "
tictac=['0','1','2','3','4','5','6','7','8']
count1=0
count2=0
def Board():
	os.system('clear')	
	print "  Tic Tac Toe\n\n"
	print "Player 1=X","  ","Player 2=O"	 
	print tictac[0],"  |  ",tictac[1],"  |  ",tictac[2]
	print "____|_______|_____"
	print tictac[3],"  |  ",tictac[4],"  |  ",tictac[5]
	print "____|_______|_____" 
	print tictac[6],"  |  ",tictac[7],"  |  ",tictac[8]
	print "____|_______|_____"
	print name1,count1," ",name2,count2	
def  Winner():
	if tictac[0]==tictac[1] and tictac[1]==tictac[2]:
            if tictac[0]=='X':
	        return 1
	    else:
		return 2
	elif tictac[3]==tictac[4] and tictac[4]==tictac[5]:
            if tictac[3]=='X':
	        return 1
	    else:
		return 2
	elif tictac[6]==tictac[7] and tictac[7]==tictac[8]:
            if tictac[6]=='X':
	        return 1
	    else:
		return 2
	elif tictac[0]==tictac[3] and tictac[3]==tictac[6]:
            if tictac[0]=='X':
	        return 1
	    else:
		return 2
	elif tictac[1]==tictac[4] and tictac[4]==tictac[7]:
            if tictac[1]=='X':
	        return 1
	    else:
		return 2
	elif tictac[2]==tictac[5] and tictac[5]==tictac[8]:
            if tictac[2]=='X':
	        return 1
	    else:
		return 2
	elif tictac[0]==tictac[4] and tictac[4]==tictac[8]:
            if tictac[0]=='X':
	        return 1
	    else:
		return 2
	elif tictac[2]==tictac[4] and tictac[4]==tictac[6]:
            if tictac[2]=='X':
	        return 1
	    else:
		return 2
	
def Play():
	turn=0
	n=0
        while 1:	
		    Board()
		    if turn==0:
		        n=input('Player 1 Enter a number from 1 to 9: ')
			if n>=0 and n<=10 and (tictac[n]!='X' or tictac[n]!='O'):
			    tictac[n]='X'
			    Board()
			    turn=1
			else:
		        	print "Wrong Choice\n"
			if Winner()==1:
			    #count1=count1+1;
			    print("Player 1 wins")
			    break
		    if turn==1:
		        n=input('Player 2 turn,Enter a number from 1 to 9: ')
			if n>=0 and n<=10 and (tictac[n]!='X' or tictac[n]!='O'):
			    tictac[n]='0'
			    Board()
			    turn=0	
		    else:
			print("Wrong Choice Turn Lost")
		 
		    if Winner()==2:
			#count2=count2+1
			print("Player 2 wins")	
		        break
	 		
						
Play()


