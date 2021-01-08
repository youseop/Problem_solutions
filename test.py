
def func(i):
  a = set()
  a.add(1)
  if i ==999: return
  func(i+1)
  return

@profile    
def main():
  func(100)

if __name__=="__main__":
  main()