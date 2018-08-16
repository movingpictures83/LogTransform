import sys
import numpy
#from plugins.CSV2GML.CSV2GMLPlugin import *
#from CSV2GML.CSV2GMLPlugin import *
import math

eps = numpy.finfo(float).tiny

class LogTransformPlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      self.firstline = filestuff.readline()
      lines = []
      for line in filestuff:
         lines.append(line)

      self.m = len(lines)
      self.samples = []
      self.bacteria = self.firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)
      self.ADJ = numpy.zeros([self.m, self.n])
      i = 0
      for i in range(self.m):
            contents = lines[i].split(',')
            self.samples.append(contents[0])
            for j in range(self.n):
               value = float(contents[j+1])
               if (value == 0):
                  value += eps
               self.ADJ[i][j] = value
            i += 1

   def output(self, filename):
      filestuff = open(filename, 'w')
      filestuff.write('\"\",')
      for i in range(self.n-1):
         filestuff.write(self.bacteria[i]+",")
      filestuff.write(self.bacteria[self.n-1])
      for i in range(self.m):
         #if (i == self.m-1): 
         #   filestuff.write(self.samples[i][0:len(self.samples[i])-1]+",")
         #else:
         filestuff.write(self.samples[i]+",")
         for j in range(self.n-1):
            filestuff.write(str(math.log(self.ADJ[i][j]))+",")
         filestuff.write(str(math.log(self.ADJ[i][self.n-1])))
         filestuff.write("\n")




