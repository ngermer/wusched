from HTMLParser import HTMLParser

class WUSCHEDParser(HTMLParser):
  def __init__(self, course_handler):
    HTMLParser.__init__(self)
    self.course_handler = course_handler
    self.found_table = False
    self.in_data = False
    self.course = None
    self.cell_num = -1
    self.title_caught = False
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
      self.title_caught = False

    elif tag == "td":
      self.cell_num += 1

    elif tag == "a":
      if self.cell_num == 0:
        pass
      elif self.cell_num == 1:
        pass
      elif self.cell_num == 2:
        if not self.title_caught:
          self.title_caught = True
        else:
          #found a syllabus link.
          for k,v in attrs:
            if k == "href":
              self.course["syl"]=v
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
        self.course_handler.add_course(self.course)

  def handle_data(self,data):
    # wait until we find the table.
    if (not self.found_table) or (not self.in_data):
      return

    #strip whitespace.
    data = data.strip()

    # begin parsing a row of data.
    if self.cell_num == 0:
      self.course["dept"],data = data.split(" ",1)
      data,self.course["num"] = data.rsplit(" ",1)
    elif self.cell_num == 1:
      self.course["sec"] = data
    elif self.cell_num == 2:
      #avoid overwriting names with "syllabus"
      if "name" not in self.course:
        self.course["name"] = data
    elif self.cell_num == 3:
      pass
    elif self.cell_num == 4:
      self.course["days"] = data
    elif self.cell_num == 5:
      self.course["begin"] = data
    elif self.cell_num == 6:
      self.course["end"] = data
    elif self.cell_num == 7:
      self.course["inst"] = data
    elif self.cell_num == 8:
      pass
    elif self.cell_num == 9:
      self.course["seats"] = int(data)
    elif self.cell_num == 10:
      self.course["enrolled"] = int(data)
    elif self.cell_num == 11:
      self.course["waits"] = int(data)
    elif self.cell_num == 12:
      self.course["attr"] = data.split(", ")

if __name__ == '__main__':
  print "WUSCHEDParser provider running at", asctime()
  course_handler = CourseHandler()
  parser = WUSCHEDParser(course_handler)
  
  with open("../../wu_l_list.html") as f:
    for line in f:
      parser.feed(line)

  print "Done."

