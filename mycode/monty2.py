import sys

sys.path.insert(0, '../thinkbayes2')

from thinkbayes2 import Suite

class Monty(Suite):

  def Likelihood(self, data, hypo):
    if hypo == data:
      return 0
    elif hypo == 'A':
      return 0.5
    else:
      return 1

monty = Monty('ABC')
monty.Update('B')
monty.Print()