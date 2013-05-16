import WUSCHEDParser
import WUSCHEDDataGenerator
import time

print "WUSCHED database update running..."
print "Started at", time.asctime()

dg = WUSCHEDDataGenerator()
parser = WUSCHEDParser(dg)
with open("../../wu_e_list.html") as f:
  for line in f:
    parser.feed(line)

print "Finished update at", time.asctime()
