from WUSCHEDParser import *
from WUSCHEDDataGenerator import *
import datetime

print "WUSCHED database update running..."
start = datetime.datetime.now()
print "Started at",start.ctime()

"""
BEGIN UPDATE
"""
dg = WUSCHEDDataGenerator()
parser = WUSCHEDParser(dg)
with open("../../wu_l_list.html") as f:
  for line in f:
    parser.feed(line)
"""
END UPDATE
"""

end = datetime.datetime.now()
print "Finished update at",end.ctime()
length = end-start
print "WUSCHED database update finished in",length
