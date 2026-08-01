str = "Shahabuddin"
str1 = "Mohd"
str2="hahab"
str3= "Hello.World"
print(str[1])
print(str[0:5]) #substring
print(str+str1) #oncat
print(str2 in str)# contains

var=str3.split(".")
print(var)
print(var[0])
# extract email from this line
email="hello mohd shahabuddin i am sending mail to abc@gmail.com please revrt"
beforeTo=email.split("to")[0]
afterTo=email.split("to")[1]
afterTo=afterTo.lstrip()
email=afterTo.split(" ")[0]
print("Email is", email)


str4= " Hello "
print(str4.strip()) # trim
print(str4.lstrip()) # l trim
print(str4.rstrip()) # r trim


