#########################################
# Defines
# ゲーム中で使うオブジェクトやショートカットを定義します。
# init python でも定義できますが、define を使用した場合には
# navigate script に登録されます。

# ダイアログを呼び出すキャラクターオブジェクトを定義します。
#define e = Character('Eileen', color="#c8ffc8", image="eileen")

# ノベルモードのキャラクタの定義
define s = Character('A', kind=nvl, color="#c8ffc8")
define m = Character('B', kind=nvl, color="#c8c8ff")
define narrator = Character(None, kind=nvl)

#########################################
# Labels
# 実際のストーリーはラベルに記述していきます。
# ラベル間の移動は基本的に jump で行いますが、
# 同じファイル内では連続するラベルは順番に実行されます。
# start はメインメニューから最初に実行されるラベルです。

#ノベルゲームモードを使用するための設定
init python:
    menu = nvl_menu
    
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve

# メインのラベル。シナリオはこのラベル以下に記載する
label start:
    window hide
    # フェイル名 bg michi を表示する。
    show bg michi
    window show
    s"「テスト」"
    narrator"物語です"
    
    # 画面の文字を消す。これを、しないと文字で画面が埋まってしまう。
    nvl clear
    
    m"テスト2"
    nvl clear
    menu:
        "one or two"

        "one":
            jump one
            
        "two":
            jump two
label one:
    nvl clear
    "one"
    jump end

label two:
    nvl clear
    "two"
    jump end

label end:
    nvl clear
    "end"
    return
