import graphics as gr
win=gr.GraphWin("Jackpot",400,400)
win.setCoords(0,0,20,20)
import random
import time
a=100;b=0
def check(list):
    global b
    if list==[7,7,7]:
        b=b+1000
    elif list[0]+1==list[1] and list[1]+1==list[2]:
        b=b+142
    elif list[0]==list[1]==list[2]:
        b=b+111
m=[[0]*3,[0]*3,[0]*3]
num=list(range(0,10))*2
num.__delitem__(7);num.append(6)
def roll():
    global m
    global num
    global diagmain
    global diag2
    for i in range(3):
        for k in range(3):
            x = random.randint(0, 19)
            m[i][k] = num[x]
    diagmain=[m[0][0],m[1][1],m[2][2]]
    diag2=[m[0][2],m[1][1],m[2][0]]
def updatemoney():
    global money
    money.undraw()
    money = gr.Text(p, a)
    money.draw(win)
def updateanounce():
    global anounce
    anounce.undraw()
    con = str("You have won $") + str(b)
    anounce = gr.Text(q, con)
    anounce.draw(win)
p=gr.Point(2,19)
money=gr.Text(p,a)
money.draw(win)
q=gr.Point(10,2)
con=str("You have won $")+str(b)
anounce=gr.Text(q,con)

c1=gr.Point(1.5,18); c2=gr.Point(4.5,17);choice1=gr.Rectangle(c1,c2);choice1.draw(win);color1=0
cen1=choice1.getCenter();text1=gr.Text(cen1,"1st row");text1.setSize(7);text1.draw(win)
c3=gr.Point(5,18);c4=gr.Point(8,17);choice2=gr.Rectangle(c3,c4);choice2.draw(win);color2=0
cen2=choice2.getCenter();text2=gr.Text(cen2,"2nd row");text2.setSize(7);text2.draw(win)
c5=gr.Point(8.5,18);c6=gr.Point(11.5,17);choice3=gr.Rectangle(c5,c6);choice3.draw(win);color3=0
cen3=choice3.getCenter();text3=gr.Text(cen3,"3rd row");text3.setSize(7);text3.draw(win)
c7=gr.Point(12,18);c8=gr.Point(15,17);choice4=gr.Rectangle(c7,c8);choice4.draw(win);color4=0
cen4=choice4.getCenter();text4=gr.Text(cen4,"1st diagonal");text4.setSize(7);text4.draw(win)
c9=gr.Point(15.5,18);c10=gr.Point(18.5,17);choice5=gr.Rectangle(c9,c10);choice5.draw(win);color5=0
cen5=choice5.getCenter();text5=gr.Text(cen5,"2nd diagonal");text5.setSize(7);text5.draw(win)
ok1=gr.Point(8.5,16);ok2=gr.Point(11.5,14);ok=gr.Rectangle(ok1,ok2);ok.draw(win)
cenok=ok.getCenter();text6=gr.Text(cenok,"Start");text6.draw(win)

t1=gr.Point(5.5,13);t2=gr.Point(8.5,10);t3=gr.Point(11.5,13);t4=gr.Point(14.5,10)
t5=gr.Point(5.5,7);t6=gr.Point(8.5,4);t7=gr.Point(11.5,7);t8=gr.Point(14.5,4)
table1=gr.Rectangle(t1,t2);table2=gr.Rectangle(t2,t3);table3=gr.Rectangle(t3,t4)
table4=gr.Rectangle(t2,t5);table5=gr.Rectangle(t7,t2);table6=gr.Rectangle(t4,t7)
table7= gr.Rectangle(t5,t6);table8=gr.Rectangle(t6,t7);table9=gr.Rectangle(t7,t8)
table1.draw(win);table2.draw(win);table3.draw(win)
table4.draw(win);table5.draw(win);table6.draw(win)
table7.draw(win);table8.draw(win);table9.draw(win)
tcen1=table1.getCenter();tnum1=gr.Text(tcen1,m[0][0])
tcen2=table2.getCenter();tnum2=gr.Text(tcen2,m[0][1])
tcen3=table3.getCenter();tnum3=gr.Text(tcen3,m[0][2])
tcen4=table4.getCenter();tnum4=gr.Text(tcen4,m[1][0])
tcen5=table5.getCenter();tnum5=gr.Text(tcen5,m[1][1])
tcen6=table6.getCenter();tnum6=gr.Text(tcen6,m[1][2])
tcen7=table7.getCenter();tnum7=gr.Text(tcen7,m[2][0])
tcen8=table8.getCenter();tnum8=gr.Text(tcen8,m[2][1])
tcen9=table9.getCenter();tnum9=gr.Text(tcen9,m[2][2])
ex1=gr.Point(18,2);ex2=gr.Point(20,0);ex=gr.Rectangle(ex1,ex2);ex.draw(win);ex.setFill("Red")
x=win.getMouse()
while x.getY()>2 or x.getX()<18:
    if c1.getX()<x.getX()<c2.getX() and c1.getY()>x.getY()>c2.getY():
        if color1==0:
            choice1.setFill("Blue")
            color1=1
            a=a-1
            updatemoney()
        elif color1==1:
            choice1.setFill("White")
            color1=0
            a=a+1
            updatemoney()
    elif c3.getX()<x.getX()<c4.getX() and c3.getY()>x.getY()>c4.getY():
        if color2==0:
            choice2.setFill("Blue")
            color2=1
            a = a - 1
            updatemoney()
        elif color2==1:
            choice2.setFill("White")
            color2=0
            a = a + 1
            updatemoney()
    elif c5.getX()<x.getX()<c6.getX() and c5.getY()>x.getY()>c6.getY():
        if color3==0:
            choice3.setFill("Blue")
            color3=1
            a = a - 1
            updatemoney()
        elif color3==1:
            choice3.setFill("White")
            color3=0
            a = a + 1
            updatemoney()
    elif c7.getX()<x.getX()<c8.getX() and c7.getY()>x.getY()>c8.getY():
        if color4==0:
            choice4.setFill("Blue")
            color4=1
            a = a - 1
            updatemoney()
        elif color4==1:
            choice4.setFill("White")
            color4=0
            a = a + 1
            updatemoney()
    elif c9.getX()<x.getX()<c10.getX() and c9.getY()>x.getY()>c10.getY():
        if color5==0:
            choice5.setFill("Blue")
            color5=1
            a = a - 1
            updatemoney()
        elif color5==1:
            choice5.setFill("White")
            color5=0
            a = a + 1
            updatemoney()
    elif ok1.getX()<x.getX()<ok2.getX() and ok1.getY()>x.getY()>ok2.getY():
        roll()
        tnum1.undraw();tnum1=gr.Text(tcen1,m[0][0]);tnum1.draw(win)
        tnum2.undraw();tnum2=gr.Text(tcen2,m[0][1]);tnum2.draw(win)
        tnum3.undraw();tnum3 = gr.Text(tcen3, m[0][2]);tnum3.draw(win)
        tnum4.undraw();tnum4 = gr.Text(tcen4, m[1][0]);tnum4.draw(win)
        tnum5.undraw();tnum5 = gr.Text(tcen5, m[1][1]);tnum5.draw(win)
        tnum6.undraw();tnum6 = gr.Text(tcen6, m[1][2]);tnum6.draw(win)
        tnum7.undraw();tnum7 = gr.Text(tcen7, m[2][0]);tnum7.draw(win)
        tnum8.undraw();tnum8 = gr.Text(tcen8, m[2][1]);tnum8.draw(win)
        tnum9.undraw();tnum9 = gr.Text(tcen9, m[2][2]);tnum9.draw(win)
        if color1==1: check(m[0]);choice1.setFill("White");color1=0
        if color2==1: check(m[1]);choice2.setFill("White");color2=0
        if color3==1: check(m[2]);choice3.setFill("White");color3=0
        if color4==1: check(diagmain);choice4.setFill("White");color4=0
        if color5==1: check(diag2);choice5.setFill("White");color5=0
        a=a+b
        updateanounce()
        b=0
        time.sleep(1)
        updatemoney()
    x=win.getMouse()
win.close()