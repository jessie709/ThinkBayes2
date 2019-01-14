import sys

sys.path.append('../thinkbayes2')

from thinkbayes2 import Pmf

pmf = Pmf()

pmf.Set('Bowl 1', 0.5)
pmf.Set('Bowl 2', 0.5)

pmf.Mult('Bowl 1', 0.75)
pmf.Mult('Bowl 2', 0.5)

pmf.Normalize()

print(pmf.Prob('Bowl 1'))
print(pmf.Prob('Bowl 2'))
