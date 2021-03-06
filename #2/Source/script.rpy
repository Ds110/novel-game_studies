﻿#########################################
# Defines
# ゲーム中で使うオブジェクトやショートカットを定義します。
# init python でも定義できますが、define を使用した場合には
# navigate script に登録されます。

# ダイアログを呼び出すキャラクターオブジェクトを定義します。
#define e = Character('Eileen', color="#c8ffc8", image="eileen")
define senpai1 = Character('わがままな先輩', color="#c8ffc8")
define senpai2 = Character('おしとやかな先輩', color="#c8ffc8")
define kouhai = Character('後輩', color="#ffffff")

#########################################
# Labels
# 実際のストーリーはラベルに記述していきます。
# ラベル間の移動は基本的に jump で行いますが、
# 同じファイル内では連続するラベルは順番に実行されます。
# start はメインメニューから最初に実行されるラベルです。

label splashscreen:
    scene black
    with Pause(1)

    show text "Crystal.Originate Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:
    
    play music "17loop.ogg"
    scene bg classroom
    
    show senpai1 normal
    
    senpai1"「終わったね。」"
    kouhai"「ふぅーー。」"
    "その声で全身が弛緩する。"
    kouhai"「お疲れ様でした。」"
    senpai1"「ちょっと待ってて」"
    hide senpai1
    "そう言って出て行ってしまった。"
    "とりあえず書き終えた書類をファイルに順次に納める。"
    kouhai"「よっ。」"
    "紙で重くなったファイルを棚にしまう。"
    kouhai"「これで全部かな。」"
    kouhai"……先輩、どこに行ったんだ？"
    kouhai"先輩の書類は手つかずのまま、机に散らかっている。」"
    kouhai"どうしようか？"

#選択肢
menu:
    "ナイスガイになる。":
         jump select_one

    "帰り支度を始める。":
         jump select_two

label select_one:
    $ renpy.block_rollback()
    "ここはてきぱきとした腕前を見せつけてやるぜ。"
    kouhai"「てっ、誰にだよ！」"
    "教室の中で声が響く。"
    "イケる。
    \nナイスガイたるもの一人ツッコミくらいは自在に使えないとな。"
    kouhai"ふっ、ははっははは。"
    
    #//スクロール
    "ちゃっちゃっと、やれたぞ。
    \n経験値を取得した。"
    "体力が５へった。気力がみなぎった。
    \n状態は充実している。
    \n！！"
    "待った。経験って値にできるものなのか。
    \nそれもそうだが、何も上がってないぞ。
    効果音カモーンッ！"
    
    #play sound ""
    "カーン(缶がぶつかる音)"
    kouhai"「……。」"
    
    #//効果音、ビッチャ
    #play sound ""
    "ビッチャ"
    
    show senpai1 sadness
    senpai1"「ごめんね。だって教室に入ったら、盛り上がってるから……。」"
    senpai1"「わたしも楽しみたいなと思っていたら、効果音を要求されたから、買ってきた。飲み物を投げたんだよ。」"
    kouhai"・・・・・。"
    senpai1"「目が怖いよう。そんなに痛くなかったでしょ。スチール缶だし……。」"
    kouhai"（ユルサナイ）"
    "復讐の炎がますます大きくなる。"
    show senpai1 normal
    senpai1"「でも、ほら今日、暑かったしね。ちょうど水浴びもできて一石二鳥。」"
    "ぬけぬけと唇を動かし続ける。"
    senpai1"「ま、まあ、ねっ。買ったばかりで気の毒だったけど。\n君は無事なんだから、いいじゃない。」"
    kouhai"（もういいか、罵詈雑言をぶつけても）"
    senpai1"「今度、わたしも買い換えようと思ってて。」"
    kouhai"（苦しい言い訳だな先輩！）"
    senpai1"「一緒に携帯ショップいこうよ。持ってけば直るよきっと……も。」"
    kouhai"「いまナント？？」"
    senpai1"「だからスマホだよ。床で濡れてる。」"
    kouhai"「こないだ、自慢してたじゃない。」"
    "腕を組んでむっとする先輩。"
    kouhai"「…………。」"
    "だんだん、冷静になってくる。\nそう俺は効果音を鳴らそうと。\nポケットからスマホを出したときに。"
    "スマホになにかが当たって……。\nそしたら先輩が拝んでいて。"
    "床、ユカ、ゆか。"
    "スマホが飛んでいった方向を見る。\nガガガ。\n頭の中が軋んでる気がした。"
    "眼球から入ってきた、情報を脳が受け付けない。"
    kouhai"「オレノ……スマホ。」"
    senpai1"「しかたないよ……形あるものはいつかは壊れる。それが今日だっただけだよ。\n私だって……いつかは。君だってそうでしょ？
    \nそう考えると、きれいな最後だったよ。」"
    "先輩はやさしく肩を叩いてくれた。"
    senpai1"「叫びきったらね。きっとあきらめがつくよ。」"
    kouhai"「うぅぅ、うぉおおおおおおおおおおお！！」"
    kouhai"（さようなら俺のスマホ）"
    
    kouhai"「そうかもしれな……って、勝手に終わらせないでください。」"
    senpai1"「あちゃー、ごまかせなかったか。……残念。」"
    kouhai"「事実をごまかさないでください。」"
    kouhai"「どうしてくれるんですか？」"
    "先輩はポンポンと腹を叩いてきた。"
    kouhai"「何してるんですか？？　ゴミでもついてましたか。」"
    senpai1"「随分とご立派だね。」"
    kouhai"「な……別に。いいでしょっ！　そんなことは！」"
    senpai1"「にまにまし始める。それがよくないんだよ。」"
    senpai1"「太ることによって、もたらされること、最初は誰もが無視できてしまうけど、
    早めの対処が大切、太ることで血液の循環が悪くなり、
    さらには足下にかかる負担が増し、"
    senpai1"「それにより体のゆがみが生じその影響は臓器にまでおよび最終的には運動するのが嫌になり、
    その結果、さらに太りまくり、最後はお相撲さんもどっくりの状態に至ってしまう。」"
    senpai1"「まあ、なんでも未病のうちに手を打つのが大切だということがわかった？」"
    kouhai"「……」"
    senpai1"「もう一度、説明しようか？」"
    kouhai"「…う、もう……いいです。」"
    senpai1"「そう？　何回でも私は大丈夫なんだけどな。残念。」"
    "先輩は心底から、心配してるよって顔をした。"
    kouhai"「はぁ…もういいや。」"
    "俺は鞄を持ち上げて、教室の扉へと向かう。"
    senpai1"「あれ、帰っちゃうの？」"
    kouhai"「帰ります。お疲れ様でした。」"
    "先輩の二の句を待たずに教室を後にした。"

#;廊下
    show bg rouka
    with dissolve
    
    show senpai1 sadness
    senpai1"「待って！！」"
    "ドっと後ろから、重みが来る。"
    "うっ！　腰がピキってなったよ。"
    kouhai"「もう、なんですかっ！」"
    senpai1"「お詫びしたいの！！」"
    kouhai"「えっ……。先輩が……。」"
    "おかしいこれは幻覚かなにかか。
    \nそれをいうなら幻聴か。まあどちらでもいい。"
    kouhai"「せ、先輩。ってあれ？」"
    "いないのかと思いきや。もう、先に進んでいた。
    \nしかたがない。俺も男だ。それに先輩がお詫びなんて珍しいし。"
    
    #；選択肢　合流 (end.rpyへ)
    
    jump end

label select_two:
    $ renpy.block_rollback()
    "書類はとりあえず、先輩の机の上に置いて。
    \nよし、きれいになったな。自分の机の上は。"
    kouhai"「さて帰るか。」"
    "教室のドアを開けようとすると、溝に手を当てようとすると。"
    "ガラッ"
    "自動であいた！？"
    "うー、こんなハイテクなシステムがスクールに導入されるなんて！
    \nぐっと喜びを噛みしめる。"
    kouhai"「うーーーーー。」"
    show senpai1 normal
    senpai1"「どうかした？」"
    kouhai"「わっ！？」"
    "見ると先輩が目をぱちくりさせていた。"
    senpai1"「ああ、オドロイタ。腰が抜けるかとオモッタ。」"
    kouhai"「先輩、棒読みですね。」"
    senpai1"「ソウデスネ。」"
    kouhai"ふはは。"
    "可笑しくて、笑ってしまう。
    \nこの人は相変わらずヘンな人だな。
    \n優越感に浸る。"
    senpai1"「な、なにその目、まるで死んだホッケを見るような。」"
    kouhai"「ホッケ？魚のですか？」"
    senpai1"「そうそう。」"
    kouhai"「先輩、生で食べたことあるんですか？」"
    senpai1"「ない。」"
    kouhai"「じゃあ、食べに行きますか？」"
    show senpai1 yorokobi
    senpai1"「やったーー！」"
    kouhai"（初めて見たぞ、ホッケでこんなに喜ぶ人）"
    senpai1"「じゃあ、早速いこうか？ってあれ、私の机が片付いてナイヨ。」"
    kouhai"「さきに行ってますね。」"
    senpai1"「ちょっと待ってよ。片付けてくれたら、お礼に……」"
    "ちらちらとこちらを見る先輩。
    \n期待のまなざしで見続ける。
    \nしかたない。言い返すか。"
    kouhai"「先輩ーーーーーーーッ！」"
    "急に大きな声を出してみる。
    \n先輩は目を丸くする。"
    kouhai"「先輩はおねだりをする子供ですか？
    \n違いますよね。いまいくつですか？」"
    "さすがの先輩もあとずさりすると踏んだが……"
    show senpai1 normal
    senpai1"「はい、缶コーヒー。」"
    "そう言って、俺のほおにそれをピタと押しつける。"
    "あっーーーーーーつくない！！"
    senpai1"「ごめんね。慌ててから間違えて冷たいの買ったんだ。」"
    "まさか、先輩が謝ってくるとは……
    \nなぜかジーーンとする。"
    "思えば…"
    senpai1"「だからね。片付け手伝って！」"
    "……回想にふける暇がない。
    \nそれはきっと家で考えたらいいんだろう。"
    kouhai"「わかりました。手伝います。」"
    senpai1"「やっぱり頼りになる後輩だね。」"

    #end.rpyへ
    jump end
    

    return