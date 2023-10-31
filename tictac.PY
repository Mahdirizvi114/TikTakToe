from tkinter import *
root=Tk()
root.title('Tik Tak Toe')
root.geometry("500x600")
root.resizable(0,0)
root.configure(bg="#FFFEFA")

c=1
def show(b):
    global c
    c=c+1

    if (c%2==0):
        if b['text']=='':
            b['text']='0'
    else:
        if b['text']=='':
            b['text']='X'

    # Main Logic for row 1

    if (bt1['text']=='0' and bt2['text']=='0' and bt3['text']=='0'):
        lb.config(text="Player 1 is Winner ")
        bt1.config(bg='green')
        bt2.config(bg='green')
        bt3.config(bg='green')

    elif (bt1['text']=='X' and bt2['text']=='X' and bt3['text']=='X'):
        lb.config(text="Player 2 is Winner ")
        bt1.config(bg='red')
        bt2.config(bg='red')
        bt3.config(bg='red')

    # Main Logic for row 2    

    elif (bt4['text']=='0' and bt5['text']=='0' and bt6['text']=='0'):
        lb.config(text="Player 1 is Winner ")
        bt4.config(bg='green')
        bt5.config(bg='green')
        bt6.config(bg='green')

    elif (bt4['text']=='X' and bt5['text']=='X' and bt6['text']=='X'):
        lb.config(text="Player 2 is Winner ")
        bt4.config(bg='red')
        bt5.config(bg='red')
        bt6.config(bg='red')

    # Main Logic for row 3    

    elif (bt7['text']=='0' and bt8['text']=='0' and bt9['text']=='0'):
        lb.config(text="Player 1 is Winner ")
        bt7.config(bg='green')
        bt8.config(bg='green')
        bt9.config(bg='green')

    elif (bt7['text']=='X' and bt8['text']=='X' and bt9['text']=='X'):
        lb.config(text="Player 2 is Winner ")
        bt7.config(bg='red')
        bt8.config(bg='red')
        bt9.config(bg='red')

    # Main Logic for Column 1    
    
    elif (bt1['text']=='0'and bt4['text']=='0' and bt7['text']=='0'):
        lb.config(text="Player 1 is Winner ")
        bt1.config(bg='green')
        bt4.config(bg='green')
        bt7.config(bg='green')

    elif (bt1['text']=='X'and bt4['text']=='X' and bt7['text']=='X'):
        lb.config(text="Player 2 is Winner ")
        bt1.config(bg='red')
        bt4.config(bg='red')
        bt7.config(bg='red')  

    # Main Logic for Column 2    

    elif (bt2['text']=='0'and bt5['text']=='0' and bt8['text']=='0'):
        lb.config(text="Player 1 is Winner ")
        bt2.config(bg='green')
        bt5.config(bg='green')
        bt8.config(bg='green')

    elif (bt2['text']=='X'and bt5['text']=='X' and bt8['text']=='X'):
        lb.config(text="Player 2 is Winner ")
        bt1.config(bg='red')
        bt4.config(bg='red')
        bt7.config(bg='red')   

    # Main Logic for Column 3     

    elif (bt3['text']=='0'and bt6['text']=='0' and bt9['text']=='0'):
        lb.config(text="Player 1 is Winner ")
        bt3.config(bg='green')
        bt6.config(bg='green')
        bt9.config(bg='green')

    elif (bt3['text']=='X'and bt6['text']=='X' and bt9['text']=='X'):
        lb.config(text="Player 2 is Winner ")
        bt3.config(bg='red')
        bt6.config(bg='red')
        bt9.config(bg='red') 


    #Main Logic for Diagonal 1 

    elif (bt1['text']=='0'and bt5['text']=='0' and bt9['text']=='0'):
        lb.config(text="Player 1 is Winner ")
        bt1.config(bg='green')
        bt5.config(bg='green')
        bt9.config(bg='green')

    elif (bt1['text']=='X'and bt5['text']=='X' and bt9['text']=='X'):
        lb.config(text="Player 2 is Winner ")
        bt1.config(bg='red')
        bt5.config(bg='red')
        bt9.config(bg='red')  


    #Main Logic for Diagonal 2

    elif (bt3['text']=='0'and bt5['text']=='0' and bt7['text']=='0'):
        lb.config(text="Player 1 is Winner ")
        bt3.config(bg='green')
        bt5.config(bg='green')
        bt7.config(bg='green')

    elif (bt3['text']=='X'and bt5['text']=='X' and bt7['text']=='X'):
        lb.config(text="Player 2 is Winner ")
        bt3.config(bg='red')
        bt5.config(bg='red')
        bt7.config(bg='red') 


def Reset():
    bt1['text']=''
    bt2['text']=''
    bt3['text']=''
    bt4['text']=''
    bt5['text']=''
    bt6['text']=''
    bt7['text']=''
    bt8['text']=''
    bt9['text']=''
    
    bt1.config(bg='grey')
    bt2.config(bg='grey')
    bt3.config(bg='grey')
    bt4.config(bg='grey')
    bt5.config(bg='grey')
    bt6.config(bg='grey')
    bt7.config(bg='grey')
    bt8.config(bg='grey')
    bt9.config(bg='grey')






        


#row 1
bt1=Button(root, text="",width=10, height=5, font=("Arial",15),bg='grey', relief='groove', command=lambda :show(bt1))
bt1.grid(row=0, column=0)
bt1.place(x=73, y=70)

bt2=Button(root, text="",width=10, height=5, font=("Arial",15),bg='grey', relief='groove',command=lambda :show(bt2))
bt2.grid(row=0, column=1)
bt2.place(x=196, y=70)

bt3=Button(root, text="",width=10, height=5, font=("Arial",15),bg='grey', relief='groove',command=lambda :show(bt3))
bt3.grid(row=0, column=2)
bt3.place(x=320, y=70)

# row 2
bt4=Button(root, text="",width=10, height=5, font=("Arial",15),bg='grey', relief='groove',command=lambda :show(bt4))
bt4.grid(row=1, column=0)
bt4.place(x=73, y=205)

bt5=Button(root, text="",width=10, height=5, font=("Arial",15),bg='grey', relief='groove',command=lambda :show(bt5))
bt5.grid(row=1, column=1)
bt5.place(x=196, y=205)

bt6=Button(root, text="",width=10, height=5, font=("Arial",15),bg='grey', relief='groove',command=lambda :show(bt6))
bt6.grid(row=1, column=2)
bt6.place(x=320, y=205)

# Row 3
bt7=Button(root, text="",width=10, height=5, font=("Arial",15),bg='grey', relief='groove',command=lambda :show(bt7))
bt7.grid(row=2, column=0)
bt7.place(x=196, y=340)

bt8=Button(root, text="",width=10, height=5, font=("Arial",15),bg='grey',relief='groove', command=lambda :show(bt8))
bt8.grid(row=2, column=1)
bt8.place(x=73, y=340)

bt9=Button(root, text="",width=10, height=5, font=("Arial",15),bg='grey',relief='groove', command=lambda :show(bt9))
bt9.grid(row=2, column=2)
bt9.place(x=320, y=340)

#For Button
bt_reset=Button(root,text="Reset",font=("arial 15 bold"), relief='groove', command=Reset)
bt_reset.grid(row=10,column=8)
bt_reset.place(x=225, y=500)

#For label
lb=Label(root, text="",bg='white',fg='Black',font=("arial 15 bold"),relief='groove')
lb.grid(row=4,column=0)
lb.place(x=0, y=550)

lb1= Label(root, text="Welcome To My Game", font=("arial 15 bold"),relief='groove')
lb1.place(x=150, y=10)

root.mainloop()
