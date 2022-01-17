from user import User

app_user_one = User("nn@nn.com", "Andrew", "pwd1", "Engineer")
app_user_one.get_user_info()

app_user_two = User("tt@tt.com", "John", "pwd221", "Teacher")
app_user_two.get_user_info()

# Input to each attribute
# app_user_three = User(input(""), input(""), input(""), input(""))
# app_user_three.get_user_info()