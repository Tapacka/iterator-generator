nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, None, 3], ['q', 'w', 'e'], ['!' , '@', '#'], ['u' , 'i', 'o']]

class FlatIterator:
  def __init__(self, list_):
    self.list_ = sum(list_,[])

  def __iter__(self):
    
    self.count = -1
    return self
    
  def __next__(self):
    self.l=[]
    self.count += 1 
    if self.count == len(self.list_):
      raise StopIteration    
    
    self.newlist = self.list_[self.count]
     
    
    
    if isinstance(self.newlist, list):      
      for i in FlatIterator(self.newlist):
        return i
                   
    else:
      return self.newlist
    
    
    
    
for item in FlatIterator(nested_list):
  print(item)
