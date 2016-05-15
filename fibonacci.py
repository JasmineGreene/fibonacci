import clr
import random
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System.Drawing import *
from System.Windows.Forms import *

def show(a,n):
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

show(30,10)
