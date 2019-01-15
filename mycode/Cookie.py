import sys

sys.path.insert(0, '../thinkbayes2')

from thinkbayes2 import Pmf

class Cookie(Pmf):

  def __init__(self, hypos):
    Pmf.__init__(self)
    for hypo in hypos:
      self.Set(hypo, 1)
    self.Normalize()

  def Update(self, data):
    for hypo in self.Values():
      like = self.Likelihood(data, hypo)
      self.Mult(hypo, like)
    self.Normalize()

  mixes = {
    'Bowl 1': dict(vanilla=0.75, chocolate=0.25),
    'Bowl 2': dict(vanilla=0.5, chocolate=0.5)
  }

  def Likelihood(self, data, hypo):
    mix = self.mixes[hypo]
    like = mix[data]
    return like

hypos = ['Bowl 1', 'Bowl 2']
pmf = Cookie(hypos)
pmf.Update('vanilla')

for hypo, prob in pmf.Items():
  print(hypo, prob)