#Look at the wallet Balance
#OCR a number friom it
#If the SMH is greater than zero
#Transfer some to Wallet 2
#Wait a while.
#Do it again.
#Test Address: stest1qqqqqqqk48z07g7u82wpjx9h9wfr88yyh2d3lxc4dz6m3

#Turbo Charge
Settings.MoveMouseDelay = 0
setWaitScanRate(10)

#Lets put run date and time on the front
import time
# Took seconds off to prevent overflow of Notes field in Spacemesh.
#now = time.strftime('%Y%m%d%H%M%S')
now = time.strftime('%Y%m%d%H%M')

import random

def spawn ():
        wait (Pattern("1678149157496.png").similar(0.32),5)
        click ("1678149199472.png")
        wait ("1678149296866.png",5)
        click("1678189106079.png")
        wait ("1678189193049.png",5)
        click ("1678189220917.png")
        click (Pattern("1678189287318.png").similar(0.78))
        click (Pattern("1678208370451.png").similar(0.98))
        click (Pattern("1678208392232.png").similar(0.81))
        click ("1678189193049.png")
        sleep (1)
        click ("1678189336202.png")
        sleep (1)
        click ("1678189399124.png")
        #Pending:
        wait ("1678189447125.png", 5)
        wait ("1678190127377.png", 600)        

def ReportError ():
        # may be going too far!
        sleep (1)

def SwitchAccount ():
        #Change from one account to another withion a Wallet
        sleep (1)

def StartSpacemesh():
        #Check if the client is running, If not start it.
        click ("1678212509607.png")
        type ( "space" )
        click ("Untitled-1.png")
        password = inputText("Wallet Password?")
        type ( password )
        click ("1678213223677.png")

def QuitSpacemesh():
        click( Pattern("1678212240975.png").targetOffset(610,-53))
        click( Pattern("1678212410453.png").targetOffset(-211,85))
        wait ("1678212974981.png",5)
      
wait ("1678149157496.png",5)
click ("1678149199472.png")
wait ("1690551177480.png",5)

#Pseudo code:  if the wallet is not spawned, spawn it! 

#StartSpacemesh()
#sleep (10)
#QuitSpacemesh()

walletaddress = inputText("Which address to send to?")
if (walletaddress == '' ):
    walletaddress = "stest1qqqqqqqk48z07g7u82wpjx9h9wfr88yyh2d3lxc4dz6m3"
transactioncount = int(inputText("How Many transactions to carry out?"))
if (transactioncount < 1):
    transactioncount = 1
pausetime = int(inputText("How long to pause between transactions?"))
sleep(5)

for step in range (transactioncount):
    wait ("1679075431924.png",5)
    # click send as an offset in the send or request section.
    click (Pattern("1679075431924.png").targetOffset(-113,87))
    wait("1688112449597.png",2)
    click(Pattern("1688112449597.png").targetOffset(32,-161))
    # Paste is faster than type
    paste ( walletaddress )
    click(Pattern("1688112449597.png").targetOffset(26,-56))
    # Network issues - use smaller for now 
    smidge = random.randrange(32000, 10000000)

    #TESTING TRANSACTION SEQUENCING AND INTEGRITY
    #smidge = (step +1)
    
    # paste is faster than type
    paste ( str(smidge) )
    # Click the Note as an offset into the Send Screen 
    click(Pattern("1688112449597.png").targetOffset(32,60))
    paste ( "Sikulix run " + now + ", transaction " + str (step + 1) + " of " + str (transactioncount))
    click (Pattern("1688112449597.png").targetOffset(63,8))
    wait ("1688079025113.png",5)
    
    fee=random.randrange(0,4)
    # TESTING SEQUENCING AND COMPLETENESS
    # fee=3
    
    if (fee == 1):
        click (Pattern("1688079025113.png").targetOffset(-17,-1))
    elif (fee ==2):
        click (Pattern("1688079025113.png").targetOffset(-11,33))
    else:
        click (Pattern("1688079025113.png").targetOffset(-11,-37))
    
    click (Pattern("1679075523312.png").targetOffset(195,208))
    wait ("1679072435800.png",5)
    # click Send (using Offset from Summary) 
    click (Pattern("1679072435800.png").targetOffset(461,410))
    wait (Pattern("1679412275834.png").similar(0.35),5) 
    # Click 'Done' As offset from Transaction sent
    click (Pattern("1679412275834.png").similar(0.35).targetOffset(350,431))
    sleep (pausetime)


