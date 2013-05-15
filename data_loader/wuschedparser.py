from HTMLParser import HTMLParser

from time import asctime

class CourseHandler:
  def __init__(self):
    print "Course handler initialized."

  def add_course(course):
    print "LOAD",course.div,course.dept,course.coursenum,course.title

class Course:
  def __init__(self):
    pass
    """
    self.div = None
    self.dept = None
    self.coursenum = None
    self.sec = None
    self.title = None
    self.days = None
    self.begin = None
    self.end = None
    self.instr = None
    self.seats = None
    self.enroll = None
    self.wait = None
    self.attr = None
    """

class WUSCHEDParser(HTMLParser):
  def __init__(self, course_handler):
    HTMLParser.__init__(self)
    self.course_handler = course_handler
    self.found_table = False
    self.in_data = False
    self.course = None
    self.cell_num = -1
    print "Parser initialized."

  def handle_starttag(self,tag,attrs):
    tag = tag.lower()
    # wait until we find the table.
    if tag == "thead":
      self.found_table = True
      return
    if not self.found_table:
      return

    # wait until we reach the appropriate location in the data.
    if tag == "tbody":
      self.in_data = True
      return
    if not self.in_data:
      return

    # begin parsing a row of data.
    if tag == "tr":
      self.course = {}
      self.cell_num = -1

    elif tag == "td":
      self.cell_num += 1

    elif tag == "a":
      if self.cell_num == 0:
        pass
      elif self.cell_num == 1:
        pass
      elif self.cell_num == 2:
        pass
      elif self.cell_num == 3:
        pass
      elif self.cell_num == 4:
        pass
      elif self.cell_num == 5:
        pass
      elif self.cell_num == 6:
        pass
      elif self.cell_num == 7:
        pass
      elif self.cell_num == 8:
        pass
      elif self.cell_num == 9:
        pass
      elif self.cell_num == 10:
        pass
      elif self.cell_num == 11:
        pass
      elif self.cell_num == 12:
        pass

  def handle_endtag(self,tag):
    if not self.found_table:
      return
    if not self.in_data:
      return
    tag = tag.lower()

    if tag=="tbody":
      self.in_data = False
      self.found_table = False

    elif tag=="tr":
      self.cell_num = -1
      if len(self.course)!=0:
        print self.course

  def handle_data(self,data):
    # wait until we find the table.
    if (not self.found_table) or (not self.in_data):
      return

    # begin parsing a row of data.
    if self.cell_num == 0:
      self.course["id"] = data
    elif self.cell_num == 1:
      self.course["sec"] = data
    elif self.cell_num == 2:
      if "title" not in self.course:
        self.course["title"] = data
    elif self.cell_num == 3:
      pass
    elif self.cell_num == 4:
      pass
    elif self.cell_num == 5:
      pass
    elif self.cell_num == 6:
      pass
    elif self.cell_num == 7:
      pass
    elif self.cell_num == 8:
      pass
    elif self.cell_num == 9:
      pass
    elif self.cell_num == 10:
      pass
    elif self.cell_num == 11:
      pass
    elif self.cell_num == 12:
      pass

if __name__ == '__main__':
  print "WUSCHEDParser provider running at", asctime()
  course_handler = CourseHandler()
  parser = WUSCHEDParser(course_handler)
  
  with open("../../wu_e_list.html") as f:
    for line in f:
      parser.feed(line)

  print "Done."

