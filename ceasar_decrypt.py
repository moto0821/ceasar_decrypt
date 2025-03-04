def main():
    message = input("暗号文を入力してください")
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'

    #すべての鍵(0～25)で処理を繰り返す
    for key in range(26):
        translated = ''
        for symbol in message:
            #大文字の場合
            if symbol in uppercase:
                index = uppercase.find(symbol)
                new_index = (index-key) % len(uppercase)
                translated += uppercase[new_index]
            #小文字の場合
            elif symbol in lowercase:
                index = lowercase.find(symbol)
                new_index = (index-key) % len(lowercase)
                translated += lowercase[new_index]
            #アルファベット以外はそのまま追加
            else:
                translated += symbol
        #鍵ごとに復号結果を表示する
        print('Key #%s: %s' % (key, translated))

main()
                
