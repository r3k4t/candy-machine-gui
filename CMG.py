import tkinter
from tkinter import *
import os

rkt = Tk()
rkt.geometry('450x430')
rkt.title("Candy Machine Gui(CM Version:3)")
is_solana = BooleanVar()
is_solana.set(False)

# solana cli wallet configuration 

def func1():
    os.system("solana config get")

def func2():
    os.system("solana-keygen new --outfile devnet.json")

def func3():
    os.system("solana-keygen new --outfile mainnet-beta.json")

def func4():
    os.system("solana config set --url https://api.devnet.solana.com")
    
def func5():
    os.system("solana config set --url  https://api.mainnet-beta.solana.com")
    
def func6():
    os.system("solana config set --keypair devnet.json")
    
def func7():
    os.system("solana config set --keypair mainnet-beta.json")
        
    
def func8():
    os.system("solana airdrop 2")
    
def func9():
    os.system("solana balance")
    


# Sugar for candy machine cli v3


def func10():
    os.system("sugar create-config config.json")
    
def func11():
    os.system("sugar launch")

def func12():
    os.system("sugar upload")


def func13():
    os.system("sugar deploy")
    
def func14():
    while True:
        os.system("sugar mint")


button1 = tkinter.Button(rkt, width=20, text="Solana Config Get", command=func1)
button1.grid(row=23, column=1)


button2 = tkinter.Button(rkt, width=20, text="Generate Devnet Keypair", command=func2)
button2.grid(row=25, column=1)



button3 = tkinter.Button(rkt, width=20, text="Generate Mainnet Keypair", command=func3)
button3.grid(row=30, column=1)



button4 = tkinter.Button(rkt, width=20, text="Devnet Config", command=func4)
button4.grid(row=35, column=1)

button5 = tkinter.Button(rkt, width=20, text="Mainnet Config", command=func5)
button5.grid(row=40, column=1)

button6 = tkinter.Button(rkt, width=20, text="Set Devnet Keypair", command=func6)
button6.grid(row=45, column=1)


button7 = tkinter.Button(rkt, width=20, text="Set Mainnet Keypair", command=func7)
button7.grid(row=50, column=1)


button8 = tkinter.Button(rkt, width=20, text="Airdrop(DEVNET) ", command=func8)
button8.grid(row=55, column=1)

button9 = tkinter.Button(rkt, width=20, text="Check Wallet Balance", command=func9)
button9.grid(row=60, column=1)


button10 = tkinter.Button(rkt, width=20, text="Create Config", command=func10)
button10.grid(row=65, column=1)


button11 = tkinter.Button(rkt, width=20, text="Launch", command=func11)
button11.grid(row=70, column=1)


button14 = tkinter.Button(rkt, width=20,bg="green", fg="white", text="Start Auto Minter", command=func14)
button14.grid(row=80, column=1)


isSolana = tkinter.Checkbutton(rkt, text='https://solscan.io/',var=is_solana)
isSolana.grid(row=83, column=0)


isSolana = tkinter.Checkbutton(rkt, text='https://solana.fm/',var=is_solana)
isSolana.grid(row=84, column=0)


isSolana = tkinter.Checkbutton(rkt, text='https://opensea.io',var=is_solana)
isSolana.grid(row=85, column=0)



isSolana = tkinter.Checkbutton(rkt, text='Author:Rahat Khan Tusar',var=is_solana)
isSolana.grid(row=83, column=5)


isSolana = tkinter.Checkbutton(rkt, text='https://github.com/r3kt/',var=is_solana)
isSolana.grid(row=84, column=5)

isSolana = tkinter.Checkbutton(rkt, text='Solana Blockchain',var=is_solana)
isSolana.grid(row=20, column=0)



rkt.mainloop()
