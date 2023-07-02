str="The quick brown fox jumps over the lazy dog"
#print(str)
#print(len(str))
#print(str.upper())
#print(str.lower())
#print(str.title())
#reverse_str = str[::-1]
#print(reverse_str)
#count_str=str.lower().count("the")
#print(count_str)
#print(str.lower().replace("the", "a"))
#count={}
#for items in str:
   # count[items]=count.get(items,0)+1
#print(count)

people = ['Jane', 'John', 'Jack', 'Janet']
sex = ['Female', 'Male', 'Male', 'Female']
age = [23, 34, 16, 28]
for people,sex, age in zip(people,sex,age):
    print(f"{people} the {sex} is {age} years old.")

