car ={'text':['mazda','Ferrari','Bugatti']}
word = input()

def search(car,word):
   if word in car['text']or word=='Mazda':
      price=3000
      print(word,'the price is',price)
      if word in car['text'] or word =='Mazda':
         print(word.count(str(word)))
      return("Search Word found!")
   elif word in car['text']or word=='ferrari':
      price=5000
      print(word,'the price is',price)
      if word in car['text'] or word =='ferrari':
         print(word.count(str(word)))
      return("Search Word found!")
   elif word in car['text']or word=='bugatti':
      price=10000
      print(word,'the price is',price)
      if word in car['text'] or word =='bugatti':
         print(word.count(str(word)))
      return("Search Word found!")
  
   else:
      if word not in car['text']:
         print(word.count(word))
      return("Search word but cannot found in car list")
print(search(car, word))

#update search word count found
