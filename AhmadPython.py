#number = int(input("adad aval ra vared kon"))
#numbertwo = int(input("adad dovom ra vared kon"))
#result = 0
#for i in range(numbertwo):
   #number = number / 2
#print(number)


#x = int(input("adad aval ra vared kon:"))
#y = int(input("adad dovom ra vared kon:"))
#print(x)
#print(y)
#z = x
#x = y
#y = z
#print(x)
#print(y)





#number = int(input("adad aval ra vared kon"))
#numbertwo = int(input("adad dovom ra vared kon"))
#result = 0
#for i in range(number, numbertwo, 2):
  #result += i 
#print(result)




#number = int(input("adad aval ra vared kon"))
#numbertwo = int(input("adad dovom ra vared kon"))
#result = 0
#for i in range(numbertwo):
   #number = number * 1
#print(number)
#for j in range(numbertwo):
   #number = number * 2
#print(number)

#seats = 300
#while seats > 0:
  #print("Sell ticket")
  #seats = seats - 1

#counter = input("Addad Ra Vared Konid:")
#while counter < 5:
  #print(counter)
  #counter = counter + 1


#x = int(input("adad aval ra vared kon"))
#y = int(input("adad dovom ra vared kon"))
#d = 0
#if x > y:
  #d = y
  #y = x
  #x = d
#for j in range(x,y):
  
  #for i in range(2,j):
    #if j % i == 0:
      #print("اول نيست")
   
    #else:
      #print(j)



#a = [10, 6, 20, 3, 15, 14, 30, 13, 18, 30]
#b = 0
#for i in a:
  #if i > b:
    #b = i

#print(b)



#a = int(input("adad aval ra vared kon"))
#b = int(input("adad dovom ra vared kon"))
#c = 0
#if c % a // b == 0:
   #for i in range(a,b):
        #c = a
        #b = c
        #a = c
        #c = b
#print(b)





# دریافت دو عدد از کاربر
#num1 = int(input("عدد اول را وارد کنید: "))
#num2 = int(input("عدد دوم را وارد کنید: "))

# تعیین مقدار اولیه برای GCD
#gcd = 1  # مقسوم‌علیه مشترک اولیه

# تعیین کمترین عدد برای محدودیت حلقه
#min_num = min(num1, num2)

# بررسی مقسوم‌علیه‌ها
#for i in range(1, min_num + 1):
    #if num1 % i == 0 and num2 % i == 0:
        #gcd = i  # به‌روزرسانی GCD با مقسوم‌علیه جدید

# چاپ نتیجه
#print(gcd)



# دریافت دو عدد از کاربر
#num1 = int(input("عدد اول را وارد کنید: "))
#num2 = int(input("عدد دوم را وارد کنید: "))

# تعیین کوچکترین و بزرگترین عدد
#if num1 < num2:
    #min_num = num1
    #max_num = num2
#else:
    #min_num = num2
    #max_num = num1

# چاپ نتیجه
#print(f"کوچکترین عدد بین {num1} و {num2} برابر است با: {min_num} 🎉")
#print(f"بزرگترین عدد بین {num1} و {num2} برابر است با: {max_num} 🎉")






#a = int(input("Addad Aval Ra Vared Kon"))
#b = int(input("Addad Dovom Ra Vared Kon"))
#c = int(input("Addad Sevom Ra Vared Kon"))
#d = int(input("Addad Chaharom Ra Vared Kon"))
#e = int(input("Addad Panjom Ra Vared Kon"))
#max = 0
#min = 0
#z = 0
#for i in range(5):
    #max = a
    #min = a
    #if b > max:
        #max = b
        #if c > max:
         #   max = c
        #if d > max:
           # max = d
        #if e > max:
            #max = e
   # print(max)
    #print(min)
    







#a = 1
#b = 1

#for i in range(a + b):
    #sum = i
#print(i)
   

#تمرين#يک عدد از کاربر دريافت کنيد عدد را معکوس کنيد



#a = 25
#b = 30
#if a > b or a > 5:
    #print("OutPut-1")
#else:
    #print("OutPut-2")



#a = 25
#b = 30
#if a > b and a > 5:
 #   print("OutPut-1")
#elif a>5:
 #   print("OutPut-2")
#else:
    #print("Other OutPut")



#.........................................

# تمرين يک معکوس کردن عدد

# دریافت عدد از کاربر
#number = int(input("ek Addad Vared Kon: "))

# تبدیل عدد به رشته برای پردازش راحت‌تر
#number_str = str(number)

# ایجاد یک رشته خالی برای ذخیره نتیجه معکوس
#reversed_str = ""

# استفاده از حلقه for برای معکوس کردن
#for digit in number_str:
    #reversed_str = digit + reversed_str

# تبدیل نتیجه معکوس شده به عدد
#reversed_number = int(reversed_str)

# نمایش نتیجه
#print("عدد معکوس شده:", reversed_number)




#تمرين دوم نمايش بزرگترين و کوچکترين عدد

# دریافت دو عدد از کاربر
#numberone = int(input("Addad Aval Ra Vared Kon: "))
#numbertwo = int(input("Addad Dovoom Ra Vared Kon: "))

# مقداردهی اولیه
#max_num = numberone
#min_num = numbertwo

# استفاده از حلقه for برای مقایسه (با 2 تکرار)
#for num in [numberone, numbertwo]:
    #if num > max_num:
        #max_num = num
    #if num < min_num:
        #min_num = num

# نمایش نتایج
#print(f"بزرگترین عدد: {max_num}")
#print(f"کوچکترین عدد: {min_num}")



#تمرين سوم بزرگترين مقسوم عليه مشترک بين دو عدد

# دریافت دو عدد از کاربر
#numone = int(input("Lotfan Addad Aval Ra Vared Kon: "))
#numtwo = int(input("Lotfan Addad Dovoom Ra Vared Kon: "))

# تبدیل اعداد به مقادیر مثبت
#a = abs(numone)
#b = abs(numtwo)

# پیدا کردن کوچک‌ترین عدد برای محدوده حلقه
#smaller = min(a, b)

#gcd = 1  # مقدار پیش‌فرض ب.م.م

# حلقه برای یافتن بزرگترین مقسوم‌علیه مشترک
#for i in range(1, smaller + 1):
    #if a % i == 0 and b % i == 0:
        #gcd = i

# نمایش نتیجه
#print(f"بزرگترین مقسوم‌علیه مشترک ({numone}, {numtwo}) برابر است با: {gcd}")



#name = ["ahmad", "Ali", "Reza"]
#myName = names[2]
#myNameone = "Hossein"
#names[0] = myName
#print(names)





#numbers = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]

#count = 0  

#for num in numbers:
    #if num % 2 == 0:
      #  count += 1

#print("آرایه:", numbers)
#print("تعداد اعداد زوج:", count)

    
    
#animals = ["cat", "dog", "bird", "cow"]
#outputs = [
    #animals[0], #'cat'
    #animals[-1], # 'cow'
    #animals[-2], # 'bird'
    #animals[-3:], # ['dog', 'bird', 'cow']
    #animals[-3:-1] # ['dog', 'bird']
#]
# چاپ معکوس خروجی‌ها با حلقه for
#for item in reversed(outputs):
    #print(item) 



#c =  0
#num = int(input("Enter your number:"))
#products = [2, 5, 2, 2, 3]
#for i in range(len(products)):
    #if num in products:
     #   c += 1
#print(c)



# دریافت دو عدد از کاربر
number1 = int(input("Addad Aval Ra Vared Konid: "))
number2 = int(input("Addad Dovoom Ra Vared Konid: "))

# تعیین عدد کوچک‌تر و بزرگ‌تر
start = min(number1, number2)
end = max(number1, number2)

total = 0  # متغیر برای ذخیره مجموع

print("اعداد زوج در محدوده:")

for number in range(start, end + 1):
    if number % 2 == 0:  # بررسی زوج بودن عدد
        if total + number > 200:  # اگر مجموع از 200 بیشتر شود
            print("\nمجموع از 200 گذشت! محاسبه متوقف شد.")
            break
        print(number, end=' ')  # نمایش عدد زوج
        total += number  # اضافه کردن به مجموع

print(f"\nمجموع اعداد زوج: {total}")
