import sys
from PySide import QtGui, QtCore

class Calculator(QtGui.QWidget):

 def __init__(self):
  super(Calculator, self).__init__()
  self.textAns = str()
  self.initUI()

 def initUI(self):
  
  self.setGeometry(300, 300, 100, 100) 
  self.setMaximumSize(100, 100)
  self.setWindowTitle('Calaculator')
  
  self.widgets()

  self.show  
  
 def widgets(self):
  
  self.buttons()
  self.setLayout(self.grid)
  self.show()
  
 def buttons(self): 
  
  self.grid = QtGui.QGridLayout()
  
  self.j = 0
  self.i = 0
  
  self.Pos = list()
  
  while self.j < 7:
   while self.i < 5:
    self.Pos.append([self.j, self.i])
    self.i = self.i + 1
   self.i = 0
   self.j = self.j + 1
    
  self.showAns()
    
  self.Bck = QtGui.QPushButton('Bck') 
  self.C = QtGui.QPushButton('C')
  self.Close = QtGui.QPushButton('Close')
  self.Pow = QtGui.QPushButton('Pow')
  self.Sqrt = QtGui.QPushButton('Sqtr')
  self.seven = QtGui.QPushButton('7')
  self.eight = QtGui.QPushButton('8')
  self.nine = QtGui.QPushButton('9')
  self.div = QtGui.QPushButton('/')
  self.pour = QtGui.QPushButton('%')
  self.four = QtGui.QPushButton('4')
  self.five = QtGui.QPushButton('5')
  self.six = QtGui.QPushButton('6')
  self.multi = QtGui.QPushButton('*')
  self.openP = QtGui.QPushButton('(')
  self.one = QtGui.QPushButton('1')
  self.two = QtGui.QPushButton('2')
  self.three = QtGui.QPushButton('3')
  self.minus = QtGui.QPushButton('-')
  self.closeP = QtGui.QPushButton(')')
  self.zero = QtGui.QPushButton('0')
  self.point = QtGui.QPushButton('.')
  self.neg = QtGui.QPushButton('+/-')
  self.plus = QtGui.QPushButton('+')
  self.equal = QtGui.QPushButton('=')  
   
  self.grid.addWidget(self.Bck, self.Pos[10][0], self.Pos[10][1])
  self.grid.addWidget(self.C, self.Pos[11][0], self.Pos[11][1])
  self.grid.addWidget(self.Close, self.Pos[12][0], self.Pos[12][1])
  self.grid.addWidget(self.Pow, self.Pos[13][0], self.Pos[13][1])
  self.grid.addWidget(self.Sqrt, self.Pos[14][0], self.Pos[14][1])
  self.grid.addWidget(self.seven, self.Pos[15][0], self.Pos[15][1])
  self.grid.addWidget(self.eight, self.Pos[16][0], self.Pos[16][1])
  self.grid.addWidget(self.nine, self.Pos[17][0], self.Pos[17][1])
  self.grid.addWidget(self.div, self.Pos[18][0], self.Pos[18][1])
  self.grid.addWidget(self.pour, self.Pos[19][0], self.Pos[19][1])
  self.grid.addWidget(self.four, self.Pos[20][0], self.Pos[20][1])
  self.grid.addWidget(self.five, self.Pos[21][0], self.Pos[21][1])
  self.grid.addWidget(self.six, self.Pos[22][0], self.Pos[22][1])
  self.grid.addWidget(self.multi, self.Pos[23][0], self.Pos[23][1])
  self.grid.addWidget(self.openP, self.Pos[24][0], self.Pos[24][1])
  self.grid.addWidget(self.one, self.Pos[25][0], self.Pos[25][1])
  self.grid.addWidget(self.two, self.Pos[26][0], self.Pos[26][1])
  self.grid.addWidget(self.three, self.Pos[27][0], self.Pos[27][1])
  self.grid.addWidget(self.minus, self.Pos[28][0], self.Pos[28][1])
  self.grid.addWidget(self.closeP, self.Pos[29][0], self.Pos[29][1])
  self.grid.addWidget(self.zero, self.Pos[30][0], self.Pos[30][1])
  self.grid.addWidget(self.point, self.Pos[31][0], self.Pos[31][1])
  self.grid.addWidget(self.neg, self.Pos[32][0], self.Pos[32][1])
  self.grid.addWidget(self.plus, self.Pos[33][0], self.Pos[33][1])
  self.grid.addWidget(self.equal, self.Pos[34][0], self.Pos[34][1])
  
  self.Bck.clicked.connect(self.buttonEvent) 
  self.C.clicked.connect(self.buttonEvent) 
  self.Close.clicked.connect(self.buttonEvent)
  self.Pow.clicked.connect(self.buttonEvent) 
  self.Sqrt.clicked.connect(self.buttonEvent) 
  self.seven.clicked.connect(self.buttonEvent) 
  self.eight.clicked.connect(self.buttonEvent) 
  self.nine.clicked.connect(self.buttonEvent) 
  self.div.clicked.connect(self.buttonEvent)
  self.pour.clicked.connect(self.buttonEvent)
  self.four.clicked.connect(self.buttonEvent)
  self.five.clicked.connect(self.buttonEvent)
  self.six.clicked.connect(self.buttonEvent)
  self.multi.clicked.connect(self.buttonEvent)
  self.openP.clicked.connect(self.buttonEvent)
  self.one.clicked.connect(self.buttonEvent)
  self.two.clicked.connect(self.buttonEvent) 
  self.three.clicked.connect(self.buttonEvent) 
  self.minus.clicked.connect(self.buttonEvent) 
  self.closeP.clicked.connect(self.buttonEvent)
  self.zero.clicked.connect(self.buttonEvent)
  self.point.clicked.connect(self.buttonEvent)
  self.neg.clicked.connect(self.buttonEvent)
  self.plus.clicked.connect(self.buttonEvent)
  self.equal.clicked.connect(self.buttonEvent)
  
  self.grid.setSpacing(10)	

 def buttonEvent(self):

   if self.sender() == self.Bck:
    self.textAns = self.textAns[:-1]    
   elif self.sender() == self.C:
    self.textAns = ""
   elif self.sender() == self.Close:
    self.close()
   elif self.sender() == self.Pow:
    self.textAns = self.textAns + '**'
   elif self.sender() == self.Sqrt:
    self.textAns = self.textAns + '**(1/'   
   elif self.sender() == self.pour:
    self.textAns = self.textAns + '/100'
   elif self.sender() == self.neg:
    self.textAns = self.textAns + '-'
   elif self.sender() == self.equal:
    if self.textAns == "":
     self.textAns = "0"
    self.ansEquation()
   else:
    self.textAns = self.textAns + self.sender().text()
	
	
   if self.sender() != self.equal:
    self.ans.setText(self.textAns)
    self.ans.displayText()
   
 def ansEquation(self):
  try:
   self.equat = eval(self.textAns)
   self.textAns = self.textAns + ' = ' + str(self.equat)
   
  except:
   self.textAns = 'ERROR!!!'  
  self.ans.setText(self.textAns)
  self.ans.displayText()
  self.textAns = ""
  
 def showAns(self):
  self.ans = QtGui.QLineEdit()
  self.grid.addWidget(self.ans, 0, 0, 1, 5)
 
def main():
 app = QtGui.QApplication(sys.argv)
 ex = Calculator() 
 sys.exit(app.exec_())
 
if __name__ == '__main__':
 main() 
