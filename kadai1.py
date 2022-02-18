# csvファイルからリストを読み込み
with open('source.csv',encoding='utf-8')as f:
    source= [s.strip() for s in f.readlines()]

print(source)
# 入力したキャラクターが存在するか否か
def search():
    word = input("鬼滅の登場人物の名前を入力してください >>>") 
    if word in source:
        print("{}がみつかりました".format(word))
    else:
        print("{}はみつかりませんでした".format(word))
        
# 存在しなかったキャラクターをリストに追加
        choice = input("登場人物のリストに{}を追加しますか？ 'yes' or 'no' [y/N]: ".format(word))
        if choice in ['y', 'ye', 'yes']:
            source.append(word)
            print("{}を登場人物のリストに追加しました".format(word))
        elif choice in ['n', 'no']:
            print("{}を登場人物のリストに追加しませんでした".format(word))

# キャラクターリストをcsvに保存            
    print(source)
    
    path_w = 'source.csv'
    
    with open(path_w, mode='w',encoding='utf-8') as f:
        f.write('\n'.join(source))
                
if __name__ == "__main__":
    search()
