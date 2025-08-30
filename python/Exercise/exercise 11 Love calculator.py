name1=input("Enter your name : ")
name2=input("Enter his/her name : ")

combine_string = name1 + name2
print(combine_string)

lower_case_string = combine_string.lower()

t=lower_case_string.count('t')
r=lower_case_string.count('r')
u=lower_case_string.count('u')
e=lower_case_string.count('e')

true = t + r + u + e

l=lower_case_string.count('l')
o=lower_case_string.count('o')
v=lower_case_string.count('v')
e=lower_case_string.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score == 100:
    print(f"Your Love score is {love_score} and You are soulmates! 💞💍")
elif love_score >= 90:
    print(f"Your Love score is {love_score} and A perfect love story! ❤🔥")
elif love_score >= 80:
    print(f"Your Love score is {love_score} and You're deeply in love! 💖")
elif love_score >= 70:
    print(f"Your Love score is {love_score} and Great chemistry between you two! 😊")
elif love_score >= 60:
    print(f"Your Love score is {love_score} and You have strong feelings! 🥰")
elif love_score >= 50:
    print(f"Your Love score is {love_score} and There's potential! Keep working on it! 💕")
elif love_score >= 40:
    print(f"Your Love score is {love_score} and You're more than friends but need effort! 🤔")
elif love_score >= 30:
    print(f"Your Love score is {love_score} and Friendship is strong, but love needs time! 😅")
elif love_score >= 20:
    print(f"Your Love score is {love_score} and Just casual friends for now! 😆")
else:
    print(f"Your Love score is {love_score} and Uh-oh! Maybe just acquaintances? 😬")