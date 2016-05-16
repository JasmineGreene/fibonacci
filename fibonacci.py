import clr
import System
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

rand = System.Random()

def show(param):
    a = param[0]
    n = param[1]
    form = System.Windows.Forms.Form()
    form.ClientSize = System.Drawing.Size(a*n,a*n)
    buttom = [[System.Windows.Forms.Button() for j in range(n)] for i in range(n)]
    def sh(i,j):
        shh(i,j,System.Drawing.Color.FromArgb(rand.Next(256),rand.Next(256),rand.Next(256)))
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
            buttom[i][j].BackColor = System.Drawing.Color.AliceBlue
            buttom[i][j].Location = System.Drawing.Point(a*i,a*j)
            buttom[i][j].ClientSize = System.Drawing.Size(a,a)
            buttom[i][j].MouseDown += cl(i,j)
    System.Windows.Forms.Application.Run(form)

st = System.Threading.ParameterizedThreadStart(show)

def click(o,e):
    th = System.Threading.Thread(st)
    th.Start((int(t1.Text),int(t2.Text)))

m = System.Windows.Forms.Form()
m.ClientSize = System.Drawing.Size(275,110)
t1 = System.Windows.Forms.TextBox()
t2 = System.Windows.Forms.TextBox()
t1.Text = "30"
t2.Text = "10"
m.Controls.Add(t1)
m.Controls.Add(t2)
t1.Location = System.Drawing.Point(25,25)
t2.Location = System.Drawing.Point(150,25)
b = System.Windows.Forms.Button()
m.Controls.Add(b)
b.Location = System.Drawing.Point(25,60)
b.Size = System.Drawing.Size(225,25)
b.Click += click
System.Windows.Forms.Application.Run(m)
