class member:
    def __init__(self,name,username,password):
        self.name=name
        self.username=username
        self.password=password

    def __str__(self):
        return f'member 이름 {self.name}, 아이디 {self.username}'

    def display(self):
        print(f'이름: {self.name}  아이디: {self.username}')

class post:
    def __init__(self,title,content,author):
        self.title=title
        self.content=content
        self.author=author

members=[]
post=[]

member1= member('가나다','abc','def')
member2= member('걔냬댸','king','queen')
member3= member('김고은','hwalym','fearless')

members=[member1,member2,member3]
print(members)