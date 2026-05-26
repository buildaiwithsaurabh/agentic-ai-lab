# Varible Scope = Where a varible is visible and accessible
# Scope resolution = Local - > Enclosed -> Global -> Built-in


# 1.  Local
def func1():
  a = 1
  print(a)


def func2():
  b = 2
  print(b)

func1()
func2()



# 2. Enclosed

def func1():
  b = 1
  
  def func2():
    print(b)
  func2()

func1()



# 3. Global

def func1():
  print(a)


def func2():
  print(a)

a = 3

func1()
func2()


# 4. Built-in
from math import e

def func1():
  print(e)

e = 3

func1()