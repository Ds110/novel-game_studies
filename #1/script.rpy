#########################################
# Defines
# ゲーム中で使うオブジェクトやショートカットを定義します。
# init python でも定義できますが、define を使用した場合には
# navigate script に登録されます。

# ダイアログを呼び出すキャラクターオブジェクトを定義します。
# define e = Character('Eileen', color="#c8ffc8", image="eileen")

define h = Character('ヒロイン', color="#c8ffc8")
define h2 = Character('ヒロイン2', color="#c8ffc8")
define s = Character('主人公', color="#c8ffc8")

#########################################
# Labels
# 実際のストーリーはラベルに記述していきます。
# ラベル間の移動は基本的に jump で行いますが、
# 同じファイル内では連続するラベルは順番に実行されます。
# start はメインメニューから最初に実行されるラベルです。

label start:
    # ファイル名 ***.mp3を再生する
    play music"***.mp3"
    
    # ファイル名 bg michi を表示する。(imagesフォルダに保存されたファイル)
    show bg michi
    
    # 立ち絵の表示 ファイル名 h naki を表示する。
    show h naki
    
    h"遅刻ー。遅刻ー。"
    
    play music"****2.mp3" fadeout  1.0
    show bg rouka
    show h warai
    h2"あいうえお"
    
    
    "選択"
menu:
    "選択1":
        jump a
    
    "選択2":
        jump b

label a:
    #巻き戻し禁止
    $ renpy.block_rollback()
    hide h
    "a"
    jump end


label b:
    $ renpy.block_rollback()
    "b"
    jump end
    
label end:    
    
    return
    