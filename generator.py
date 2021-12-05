nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, None, 3], [['q', 'w', 'e'], ['!' , '@', '#'], ['u' , 'i', 'o']]]


def flat_generator(list_):  
    for i in list_:
      if isinstance(i,list):
        for item in flat_generator(i):
	        print(item)
      else:
        yield i
  
for item in flat_generator(nested_list):  
	print(item)