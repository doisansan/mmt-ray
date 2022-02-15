#１ 変数の使い方
from html.entities import name2codepoint
from types import MemberDescriptorType


name1 = "ねずこ"
name2 = "ぜんいつ"

print(f"「{name1}」と「{name2}」はなかまです")


#２ if文の使い方
if name2 == "むざん":
    print(f"「{name1}」と「{name2}」はなかまではありません")
else:
    print(f"「{name1}」と「{name2}」はなかまです")


#３ 配列の使い方
name=["たんじろう","ぎゆう","ねずこ","むざん"]
name.append("ぜんいつ")


#４ for文の使い方
for character in name:
    print(character)
    

#５ 関数の使い方
def kimetsu():
    people=["たんじろう","ぎゆう","ねずこ","むざん","ぜんいつ"]
    for person in people:
        if person == "むざん":
            print(f"「{person}」はなかまではありません")
        else:
            print(f"「{person}」はなかまです")

kimetsu()


#６ 引数を使う関数の使い方
def daemon_s(name):
   if "ぎゆう" in name:
       print("ぎゆうは含まれます") 

daemon_s(name)