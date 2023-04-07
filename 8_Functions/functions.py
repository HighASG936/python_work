#Name: Aurelio Siordia
#Date: 06/04/23

# 8-1 Message
def display_message():
    """Describe that I want to learn on this         chapter"""
  
    message="I want to learn how declare"
    message+=" a function, called and how"
    message+=" create correctly docs about it.\n"
    print(message)



display_message()


# 8-2 Favorite Book
def favorite_book(title):
    """Display your favorite book"""
 
    print(f'One of my favorite books is "{title.title()}"')


my_book = input("Enter your favorite book: ")



favorite_book(my_book)

  



