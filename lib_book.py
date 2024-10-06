book = {"xyz": 10, "abc": 35, "lmn": 30}

choice=1
while(choice!=4):
 print("enter the choice 1:add book to stock 2:sell 3:display 4:exit") 
 choice=int(input("enter ur choice:"))

if(choice==1):
  book_name=input("enter the book to be added:")
  count=int(input("enter the count:"))
  key=book.keys()
  for i in key:
    if(book_name==i):
     book[i]=book[i]+count
     break
  else:
    book[book_name]=count

elif(choice==2):
 book_name=input("enter the book to be sold:")
 count=int(input("enter the count:"))
 key=book.keys()
 for i in key:
   if(book_name==i):
    if(count<=book[i]):
      book[i]=book[i]-count
      break
    else:
      print("insufficient number of books")
      break

 else:
  print("no book exists")
 
elif(choice==3):
 print("the stock is")
 print(book)
elif(choice==4):
 pass
else:
 print("wrong choice")