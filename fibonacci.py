import clr
import random
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')
from System.Drawing import *
from System.Windows.Forms import *
from System.Threading import *

def show(param):
    a = param[0]
    n = param[1]
    form = Form()
    form.ClientSize = Size(a*n,a*n)
    buttom = [[Button() for j in range(n)] for i in range(n)]
    def sh(i,j):
        shh(i,j,Color.FromArgb(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    def shh(i,j,c):
        if buttom[i][j].BackColor == c:
            return
        buttom[i][j].BackColor = c
        shh(j,(i+j)%n,c)
    def cl(i,j):
        return lambda o,e:sh(i,j)
    for i in range(n):
        for j in range(n):
            form.Controls.Add(buttom[i][j])
            buttom[i][j].BackColor = Color.AliceBlue
            buttom[i][j].Location = Point(a*i,a*j)
            buttom[i][j].ClientSize = Size(a,a)
            buttom[i][j].MouseDown += cl(i,j)
    Application.Run(form)

st = ParameterizedThreadStart(show)

def click(o,e):
    th = Thread(st)
    th.Start((int(t1.Text),int(t2.Text)))

m = Form()
m.ClientSize = Size(275,110)
t1 = TextBox()
t2 = TextBox()
t1.Text = "30"
t2.Text = "10"
m.Controls.Add(t1)
m.Controls.Add(t2)
t1.Location = Point(25,25)
t2.Location = Point(150,25)
b = Button()
m.Controls.Add(b)
b.Location = Point(25,60)
b.Size = Size(225,25)
b.Click += click
Application.Run(m)
