from ch1.ex1_3 import *

preg = load_pregnancies()
first = get_first_babies(preg)
others = get_others(preg)

print 's.d. of gestation for first babies =', first['prglength'].std()
print 's.d. of gestation for other babies =', others['prglength'].std()
