# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define futaba_rg = Character(_("巨大的佐仓双叶"))
define futaba = Character(_("佐仓双叶"))
define akane = Character(_("长谷川茜"))

label futaba_01_title:
    return

label futaba_01:

    scene black
    with squares
    window hide
    pause 1.0
    show text "{size=64}佐仓双叶篇 // 第一部分{/size}\n{size=32}Chapter of Futaba Sakura // Part 1{/size}"
    with Dissolve(1.0)
    pause

    scene black
    with Dissolve(1.0)
    window show
    "我睁开眼睛。"
    scene f01-0001
    with dissolve
    "这是我第一次亲眼用另一个视角来看这个世界。"
    "在我眼前是两面墙——我的鞋子，"
    scene f01-0002
    with dissolve
    extend "而再抬头看，能够看到两根巨大的柱子——也就是我的腿——耸立在此处。"
    scene f01-0003
    with dissolve
    "最上面是我的脸。它现在仿佛在正对着我，而我此时已经把头抬到了最高。"
    "……"
    "以这种视角看自己总感觉怪怪的。"
    "而这时有一段声音响起："
    "？？？" "嗯，能听到我说话吗？你不用张嘴说话，你只需要想你要说的话就行。"
    "我在脑海里想了一句话："
    futaba "我能听到，说实话以这种方式交流很好的，就是一开始有那么一点不习惯而已。"
    "这是我对面前这个巨大的我的回应。"
    scene f01-0004
    with dissolve
    "然后她把手伸下来，并且给我放下一条绳子。"
    "……让我用这根绳子爬上她的手心吗……可以。"
    scene f01-0005
    with dissolve
    "我一点一点地爬上这条绳子，只是这条绳子对我而言实在太长。"
    "实际上巨大的我给我放下的绳子是一米长的，只不过对缩小的我，这绳子足足有一百米长。"

    scene black
    with dissolve
    scene f01-0006
    with dissolve
    "我最终还是爬上了她的手心，并且和她四目相对。"
    scene f01-0007
    with dissolve
    "巨大的我转身，在灯光下仔细地观摩着我。"
    futaba_rg "我真的没有想到，你照着你自己做出的这个身体，居然会和原本的身体一模一样，真是令我佩服。"
    "没想到自己居然会佩服自己。"
    scene f01-0008
    with dissolve
    futaba_rg "现在看着这么小的我自己，感觉……还很可爱的？"
    "可……可爱……"
    scene f01-0009
    with dissolve
    "我有些害羞。"
    scene f01-0010
    with dissolve
    "一根柱子——我的手指——被放在自己的头上。"
    "轻轻地安抚着我。"
    scene f01-0011
    with dissolve
    futaba_rg "不过话说回来，自己和自己玩巨大少女这件事可能很少有人会想到吧。"
    futaba_rg "而且还交换了意识……"
    futaba "也不一定，毕竟我可不能看到整个巨大少女圈的人们的想法。也许在某个我不知道的地方，也有人抱有同样的想法。"
    call futaba_01_tiny_reason

    scene black
    with dissolve
    scene f01-0012
    with dissolve
    futaba "那我们直入主题吧。"
    futaba "你先把我放在地上。"
    scene f01-0013
    with dissolve
    "巨大的我有些不解，但还是按照我的指示把我放在了地上。"
    scene f01-0014
    with dissolve
    "我躺好，并且把眼镜摘下收好，视野却并没有因此而变得模糊。"
    "因为我在做出这个身体的时候就设定的正常视力，以便摆脱对小人来说可能会很碍事的眼镜。"
    "而再把眼镜加回去只是为了一致性而已。"
    futaba "踩我。"
    scene f01-0015
    with dissolve
    futaba_rg "真，真的要踩你吗？我有点担心你会……"
    futaba "那倒没事，你不会踩碎我的。"
    "毕竟如果就这样被踩碎了，那整个过程就显得有些索然无味。"
    scene f01-0016
    with dissolve
    futaba_rg "嗯，那，好吧，如果这是你所希望的话。"
    scene f01-0017
    with dissolve
    "她抬起脚，并把脚放在我头上。因为她没有脱鞋所以我只能看到鞋底。"
    futaba_rg "准，准备好了吗，我要踩你了。"
    "从她的语气来看，她好像还是不忍心踩我。"
    scene f01-0018
    with dissolve
    extend "但是鞋底还是冲我而来，意味着她最后还是下定了决心。" with vpunch
    "鞋底落到我身上的一瞬间，我就感到全身都在被压迫，而且这种压迫感还在以特殊的方式变化着。" with vpunch
    "先是从脚开始，然后再逐渐往上，最后均匀地遍布全身。" with vpunch
    "我的鞋底对我来说已经不再显得那么柔软，而是变得如石头般坚硬。" with vpunch
    "巨大的我就这么一直用力踩我，再用力踩。" with vpunch
    "直到我的大脑无法处理她给我带来的压迫感时，我发出了指示让她停下来。" with vpunch
    scene f01-0019
    with dissolve
    "她的脚从我身上移开，放回地面。"

    scene black
    with dissolve
    scene f01-0020
    with dissolve
    "我起身把头抬起，看到巨大的我的脸，而且还在看向我的方向。"
    futaba_rg "你没事吧。说实话我还以为，我这么一脚下去你可能就……"
    futaba "我没事，我还活着。"
    futaba_rg "那太好了。"
    futaba "不过我也感觉到，你踩我很认真啊。"
    scene f01-0021
    with dissolve
    futaba_rg "因为你也想过这样被踩，所以我就满足了你一下下～"
    scene f01-0022
    with dissolve
    "我有点不好意思了。"
    futaba "被你发现了～"
    "她居然能了解我到这种地步，果然只有自己才会做到这一点吧。"
    scene f01-0023
    with dissolve
    futaba_rg "所以呢？接下来你要做什么？"
    scene f01-0024
    with dissolve
    futaba "嗯……"
    "我想了一下，"
    "除了踩踏之外，我见过的其他玩法有：被穿进鞋子 / 袜子、被吞、爬上巨人的身体、以及无意识迫害。"
    "当然也有其他的玩法，但这些是并不怎么过分的。"
    "嗯，就这么定了。"
    scene f01-0025
    with dissolve
    jump futaba_01_what_to_do

label futaba_01_what_to_do_pre:
    scene f01-0023
    with dissolve
    futaba_rg "你还想做什么呢？"
    scene f01-0025
    with dissolve
    jump futaba_01_what_to_do

default futaba_rt_done = set()
# 是否已经被穿进鞋子或袜子里
default futaba_01_beneath_flag = False

menu futaba_01_what_to_do:
    # 菜单集会过滤掉已选择的选项
    set futaba_rt_done

    futaba "我想……"
    "被你穿进鞋子里":
        futaba "被你穿进鞋子里。"
        if futaba_01_beneath_flag:
            call futaba_01_when_beneath
            jump futaba_01_what_to_do_pre
        scene f01-0026
        with dissolve
        futaba_rg "唉？真的吗？我真的应该这么残忍地对待你吗？"
        "虽然她说这么做很残忍，但是……"
        scene f01-0027
        with dissolve
        futaba "因为我想体验一下那种感觉啊。"
        "在看了一些描写这一方面的作品后，我对这种感觉充满了遐想。我很好奇，能够被这样踩在脚底下是一种什么样的感受。"
        scene f01-0028
        with dissolve
        futaba_rg "这……"
        "……"
        scene f01-0029
        with dissolve
        futaba_rg "好吧，我满足你。"

        scene black
        with dissolve
        "我闭上眼睛。"
        "听到巨大的我脱下她的鞋子后，我突然感觉自己被抓起来，然后一下子掉落下来。"
        scene f01-0030
        with dissolve
        "等我睁开眼睛后，我就置身于一个乍一看很陌生的世界。"
        "但是我很快就明白，这里正是我的鞋子里面。"
        "这样说来，接下来巨大的我就会把脚伸进来吧。"
        futaba_rg "你要是准备好了就让我穿鞋。穿上鞋之后，你保重吧，我真的没法确定你在我鞋里会怎么样。"
        "还是很担心我吗……不管了。"
        scene f01-0031
        with dissolve
        "我向鞋子的最前面走过去，但是不走到最尽头。"
        scene f01-0032
        with dissolve
        "然后转身。"
        futaba "准备好了。"
        futaba_rg "那，我要穿鞋了。"
        scene f01-0033
        with dissolve
        "随后一个巨大的黑色物体从上方伸了进来。毫无疑问那个黑色物体就是巨大的我被黑色丝袜包裹的脚。"
        futaba_rg "啊，忘了告诉你，你现在在我左脚的鞋子里呢。"
        scene f01-0034
        with dissolve
        "然后我的脚逐渐逼近我。"
        scene f01-0035
        with dissolve
        "我躺下并且调整了一下姿势。"
        scene f01-0036
        with dissolve
        "随后巨大的我脚尖落在我的身体上，卡住我自己。"

        scene black
        with dissolve
        scene f01-0037
        with dissolve
        futaba_rg "你准备好了吗。如果准备好了就叫我一声，然后我就开始走路。"
        "我再次微调了一下自己的姿势。"
        "然后深呼吸，做好迎接一场刺激体验的准备。"
        "巨大的重量压在我身上，让我有些动弹不得。"
        "放轻松，深呼吸，因为接下来的刺激才刚刚开始。"
        call futaba_01_beneath_shared(location='shoe')
        # 共用剧情返回后直接重新选择。
        jump futaba_01_what_to_do_pre
    "被你穿进袜子里":
        futaba "被你穿进袜子里。"
        if futaba_01_beneath_flag:
            call futaba_01_when_beneath
            jump futaba_01_what_to_do
        scene f01-0072
        with dissolve
        futaba_rg "什……"
        "这真是何等的惊讶……"
        futaba_rg "好怪啊……"
        "……"
        scene f01-0073
        with dissolve
        futaba_rg "我说啊，"
        futaba "唉？"
        futaba_rg "如果我真的把你放进我的袜子里，你一定会非常难受吧。"
        extend "即便如此，你也想被我穿进袜子里？"
        futaba "嗯，我想被这样对待了。"
        "……"
        futaba_rg "那么，祝你好运。"

        scene black
        with dissolve
        "我闭上眼睛。"
        "我突然感觉自己被抓起来，然后一下子掉落下来。" with vpunch
        "随后我闻到一股强烈的味道，这样说我现在确实是被放进了我的袜子里面。"
        scene f01-0074
        with dissolve
        "我睁开眼睛仔细观察，眼前地景象证实了我的猜想。"
        "接下来应该就是要把脚伸进来吧？"
        "不对，应该先是我和袜子一起被抬起来吧。"
        futaba_rg "真的可以吗？有点……不太愿意，但我还是得为你穿上袜子呢。"
        "有些犹豫吗……应该很正常的。"

        scene black
        with dissolve
        scene f01-0075
        with dissolve
        "就这样在袜子的最底部准备一下之后……"
        futaba "准备好了。"
        futaba_rg "那，我要把袜子穿上了。"
        scene f01-0076
        with dissolve
        "整个世界都在因为巨大的我把袜子随意地拿起来而晃动。" with vpunch
        scene black
        with dissolve
        "然后我的整个视野都被抹上了黑色，是因为我的裸足已经彻底覆盖了我的缘故吧。"
        futaba_rg "啊，忘了告诉你，你现在是被穿进我左脚的袜子里呢。"
        "我调整了一下姿势。"
        "整个世界随后迅速往下晃动，应该就是在给左脚穿鞋子。" with vpunch

        scene black
        with dissolve
        scene f01-0037
        with dissolve
        futaba_rg "你准备好了吗。如果准备好了就叫我一声，然后我就开始走路。"
        "……"
        "此刻巨大的重量压在我身上，让我有些动弹不得。"
        "放轻松，深呼吸，因为接下来的刺激才刚刚开始。"
        call futaba_01_beneath_shared(location='sock')
        # 共用剧情返回后直接重新选择。
        jump futaba_01_what_to_do_pre
    "被你吃掉":
        futaba "被你吃掉。"
        "……"
        scene f01-0028
        with dissolve
        futaba_rg "……"
        futaba_rg "你这是在想什么啊……"
        futaba_rg "我说啊，你想一想，要是真的被我整个吃掉的话，你的命运不是确定的吗？"
        futaba "那又怎么样，我可以直接传送出去，而且我还会活下来。"
        "这句话我是认真的。"
        futaba_rg "你要是这样的话，我也能满足你，就是……看你自己了。"
        scene f01-0027
        with dissolve
        futaba "既然你愿意的话，"
        if futaba_01_beneath_flag:
            scene f01-0029
            with dissolve
            futaba_rg "等等等等等等，你该不会忘了一件事情吧？"
            futaba "？"
            futaba_rg "你之前把你自己穿进我脚下之后，身上肯定很脏并且散发着脚臭味吧？"
            "这样一想还真是。"
            futaba_rg "你先把你自己洗干净再考虑被我吃掉吧。"
            futaba_rg "我可不想把散发着臭味的你整个吞掉，那样子让我有点无法忍受……"
            "行吧。"
            "我得先去把自己处理一下。"
        else:
            extend "那就开始了~"
        window hide
        scene black
        with dissolve
        scene f01-0080
        with dissolve
        window show
        "我现在站在自己的手指上。"
        if futaba_01_beneath_flag:
            "之前已经确认了一下，自己身上没有异味，应该是可以让她接受的状态。"
        scene f01-0081
        with dissolve
        "近距离观察自己的嘴还是很有意思的。"
        extend "尽管这里某种意义上算是非常恐怖的地方，但我自己其实是有很强的心理准备的。"
        scene f01-0082
        with dissolve
        "她把嘴张开了。"
        scene f01-0083
        with dissolve
        "我跳进她的大嘴巴里，随后她的嘴稍微合上，但还没完全闭紧。"
        scene f01-0084
        with dissolve
        "最后她的嘴合紧，随时准备把我吞下去。"
        scene f01-0085
        with dissolve
        futaba_rg "那么我马上把你吞下去了。"
        window hide
        scene f01-0086
        with dissolve
        window show
        "咕噜！"
        scene black
        with dissolve
        "我就这样在自己食道壁的不懈推动下，滑到了某个终点……"
        window hide
        jump futaba_01_inside_stomach
    "爬上你的身体（TODO/未确定）" if False: # TODO: 爬上你的身体？
        "(TBD)"
    "让你不知不觉地迫害我（TODO/未确定）" if False: # TODO: 让你不知不觉地迫害我？
        "(TBD)"
    "就到这里吧" if len(futaba_rt_done) > 0:
        jump futaba_01_post

# 已经被穿到了下面时的对话。
label futaba_01_when_beneath:
    scene f01-0029
    with dissolve
    futaba_rg "……"
    futaba_rg "我已经把你穿进我的脚底了，我不能让你再来一次了。"
    futaba "……"
    futaba "行吧，我提点别的想法吧。"

    scene f01-0025
    with dissolve
    return

# 胃里的对话。
label futaba_01_inside_stomach:
    pause 2.0
    $ renpy.notify(_("~> 佐仓双叶的胃里"))
    pause 1.0
    window show
    "……"
    "看起来我需要把自己的手电筒打开了。"
    scene f01-0087
    with dissolve
    "……{p}所以这里就是我的胃里吗……"
    "这里就是我的肉体每天消化食物的地方，不过现在看起来意外的还很空的？"
    """
    不过那也是当然的，毕竟为了整出另一个我，另一个意识，以及把自己缩小所花费的那些精力已经足以让我空腹了。
    {p}想到如果在我跑到自己胃里时，里面还有很多没消化的食物的话……
    """
    "算了我想多了，怎么能想到这么过分的事情上？"
    futaba_rg "看起来你到了呢。"
    "随着胃壁的轻微活动，整个空间里也环绕着细微的消化音。"
    "这种声音有着一种奇妙的柔和感，让我不但没有感到一丝恐惧，反倒还感到些许的安心。"
    "当然另一方面也是因为我也是早有准备，不会被自己的胃酸消化掉。"
    scene f01-0088
    with dissolve
    "我摸了摸自己的胃壁，手边传来了一股柔软的感觉。"
    "此时的我逐渐享受起了手边的这种感觉，一直在揉摸着自己的胃壁。"
    futaba_rg "我，我好像很享受这种感觉呢。"
    scene f01-0087
    with dissolve
    "然后，就在这期间……{nw}{w=1.0}"
    pause 0.0
    with vpunch
    "咕噜咕噜……"
    "……"
    "我本来以为这只不过是一个简单的消化音，"
    scene f01-0089
    with dissolve
    "但是这时整个空间突然开始翻滚起来。"
    "这是……这是怎么回事？"
    "难道说巨大的我……{w}在翻身吗？？"
    "我得重新稳定一下自己的位置。"

    window hide
    scene black
    with dissolve
    scene f01-0090
    with dissolve
    window show

    "在整个世界发生天翻地覆的旋转之后仅仅几秒，我就找好了自己的位置。"
    scene f01-0091
    with dissolve
    "结果找到新位置之后还不过几秒，整个胃壁开始逐渐地蠕动。" with vpunch
    scene f01-0092
    with dissolve
    "然后我注意到，在我所在的位置底部开始形成一个小水滩。"
    "这里面，如果我没猜错，应该是胃酸。"
    scene f01-0093
    with dissolve
    "胃酸水池的高度在逐渐上涨，出于本能我稍微向上移动了一点。"
    scene f01-0094
    with dissolve
    "但是这时整个空间又开始剧烈的翻滚，" with vpunch
    extend "我被这突如其来的翻滚推进了胃酸当中，就这么被泡在了里面。"
    scene f01-0095
    with dissolve
    "胃壁的蠕动在继续着。"
    "我本想尝试和巨大的我进行意识交流，但是我这时听到了轻微的呼吸声。"
    "我有种不太对劲的感觉，于是尝试接上她的视线。"
    scene black
    with squares
    "……"
    futaba "（……全黑？？）"
    "似乎事情有些不对劲，于是我决定用第三视点来观察巨大的我。"
    scene f01-0096
    with squares
    "我这才发现了问题所在。"
    "巨大的我，居然在……在午睡？{w}把我吃掉然后放着我不管就去午睡了？？"
    "这可真是意想不到啊……"
    "虽然我倒是很想就这样享受着她胃里逐渐的蠕动和消化音，然而就这么下去的话……"
    "……"
    "一想到我要是一直呆在这里会从哪个地方出来，我就感到有点恶心……"
    "……"
    scene f01-0095
    with dissolve
    jump futaba_01_inside_stomach_selection

menu futaba_01_inside_stomach_selection(timeout=10.0, timeout_label="futaba_01_inside_stomach_when_timeout"):
    futaba "（看来我得……）"
    "从进来的地方回去":
        futaba "（从进来的地方回去……）"
        scene f01-0097
        with dissolve
        "我转头看向另一边。"
        "那里吗……说不定……我可以从这个进来的贲门回去？"
        window hide
        scene black
        with dissolve
        window show
        "经过一段费力的进程之后……"
        window hide
        scene f01-0098
        with dissolve
        window show
        "我成功的钻进了自己进来时用的自己的食道，然后就这样一点一点地爬出去。"
        scene black
        with dissolve
        "然而接下来的事情却完全出乎我的预料之外。"
        "就在我几乎爬到喉咙的时候……"
        scene f01-0096
        with squares
        "巨大的我无意识地做了一个看似微不足道，但却在目前的情况下对我有着重大影响的小动作……"
        scene f01-0099
        with dissolve
        "……那就是把喉咙里的异物（也就是我）给吞了回去。"
        scene black
        with squares
        "但这也就意味着，我目前为止的一切努力似乎都没用了。"
        scene f01-0095
        with dissolve
        "我又被送回了这里。"
        "但是看起来，似乎再尝试一次的话，还会是一样的结果。"
        "恐怕，这意味着……"
        futaba "（我该不会，就这么被困在这里了吧……）"
        call badend_label("佐仓双叶篇", "无法原路返回的密室")
        return
    "尝试敲打胃壁":
        futaba "（试着敲打一下胃壁，看看能不能叫醒巨大的我……）"
        scene f01-0100
        with dissolve
        "我转到胃壁的一侧。"
        scene f01-0101
        with dissolve
        "然后尝试着对着这胃壁打上一拳。"
        "……" with hpunch
        "…………" with hpunch
        "………………" with hpunch
        "没有一点效果吗……"
        scene f01-0095
        with dissolve
        jump futaba_01_inside_stomach_selection
    "不停对巨大的我喊话":
        futaba "喂！！"
        futaba "你能听到吗！！"
        futaba "快点醒来啊！！"
        "然而就这样重复几次之后……"
        "……"
        "…………"
        "………………"
        "居然一点响应都没有的？？"
        "这可真是……"
        window hide
        window show
        jump futaba_01_inside_stomach_selection
    "立刻传送出去":
        futaba "（这种情况下，可能一般的手段也没有什么用。）"
        futaba "（既然这样的话……）"
        scene f01-0102
        with squares
        "我用第三视点确定了我应该传送到的地方，就在视野所见的那个纸箱子上。"
        scene f01-0095
        with squares
        "确认好位置之后，就可以准备传送了。"
        "……"
        futaba "Persona！"
        scene black
        with squares
        "……"
        scene f01-0103
        with squares
        "看起来我到地方了。"
        futaba "（Phew……好险……）"
        scene f01-0104
        with dissolve
        "我看向巨大的我自己。"
        "她现在还在睡觉。"
        "所以她根本就没意识到她差点就会把我困在她的胃里了……"
        "因为我非常清楚这件事情，我只要一睡就是几个小时的，这意味着我搞不好就会被困在她的胃里几个小时！"
        "不过算了，反正自己已经逃出来了，这种事情应该也没什么了。"
        "现在只剩下一个问题了，那就是……"
        window auto hide
        scene black
        with dissolve
        centered "我要什么时候才能和巨大的我建立联系？" (what_color="#FFFFFF")
        "这确实是一个值得考虑的问题。"
        "因为目前我和那个巨大的我的意识对话能力，是只有在双方都清醒的情况下才能实现的。"
        "而现在那个巨大的我睡着了，也就意味着她是不清醒状态，是没法建立对话的。"
        scene f01-0104
        with dissolve
        "……"
        "总之现在还是得做点什么。"
        scene f01-0105
        with dissolve
        "先传送到那边的电脑桌上吧。"
        "至于为什么不是一点点走过去是因为我真的感觉这样做太慢了。"
        scene black with squares
        scene f01-0106
        with squares
        "看起来那边巨大的我还没有醒来，就在这里等着吧。"
        "……"
        scene black
        with dissolve
        "我不知不觉地睡着了……"
        "然后……"
        ### [TODO]
        "……"
        "（轰隆！）" with vpunch
        futaba "（什么动静……）"
        "（轰隆轰隆！！{w=0.5}{nw}" with vpunch
        extend "轰隆轰隆！！）" with vpunch
        "……"
        "我这才反应过来刚才的声音怎么回事，那估计是巨大的我在走动。"
        "我想是因为她不知道我在哪里，感到很着急吧。"
        scene f01-0107
        with dissolve
        "她终于找到我的位置了。"
        scene f01-0108
        with dissolve
        "但我抬头看时，她的脸显现出一种担忧的表情。"
        futaba "你怎么了？"
        futaba_rg "你怎么也睡着了，你让我感到很担心……"
        futaba_rg "要不是我找到你了，你可能就得有危险了。"
        "我大概能想到我会遇到什么样的危险。"
        "比如说，被踩，被无意识玩弄，以及被……{w=0.5}我在想什么啊！！"
        "总之……"
        futaba "这次体验不错，希望下次还能有更好的体验。"
        futaba_rg "……"
        # 回到初始剧情
        scene black
        with dissolve
        scene f01-0023
        with dissolve
        futaba_rg "你还想做什么呢？"
        # 共用剧情返回后直接重新选择。
        jump futaba_01_what_to_do_pre

label futaba_01_inside_stomach_when_timeout:
    "……"
    "…………"
    "………………"
    "我这个时候，已经不知道该做什么好了。"
    "只能……就这样了吗……"
    "没想到居然会变成这个样子……"
    call badend_label("佐仓双叶篇", "不知所措地被困在自己的胃里")
    return

# 被穿到下面之后的共用对话。
label futaba_01_beneath_shared(location='shoe'):
    futaba "来吧。"
    scene f01-0038
    with dissolve
    "她踏出第一脚。" with vpunch
    scene black
    with dissolve
    "在这个只有短短 0.5 秒的动作里，"
    extend "我先是感受到超重，" with vpunch
    extend "然后再突然一停，被脚底板挡住，紧接着有突然如失重一般坠落。" with vpunch
    extend "最后“轰”的一声。强大的压迫感从上方和下方传来。" with vpunch
    extend "而后她抬脚的过程让我感受到的压迫感逐渐加强。"
    extend "最后我再度随着她的抬脚而超重……如此往复。" with vpunch
    "我几乎没有任何停下来的时候。整个过程没有一丝减慢的感觉，不像有人写过的先慢下来让小人缓冲一下那样。"
    "这么说她还是对我有很强的信心呀，不然怎会按正常步子来？"
    "总之先继续体验一下这种刺激的感觉，然后再听一下外面的事情吧。"

    window hide
    window show
    "剧烈的摇晃和震动突然停下，看来她停下了脚步。"
    "我接上她的视线。"
    scene f01-0039
    with squares
    "她正面对着一排一排的书。这么说这里应该是图书馆。"
    scene f01-0040
    with dissolve
    "然后她拿下一本书，"
    scene f01-0041
    with dissolve
    extend "再抬起一只脚。"
    scene black
    "随后突如其来的剧烈摇晃让我无法继续关注她的视线，视野再次回到脚下。" with vpunch
    "最后晃动停止，上方的压迫又逐渐增大，再度稳定。"
    "而她仅仅是拿起一本书，走到座位上坐下来阅读而已。"
    "说起来，我读书的时候是很老实的，脚也不会动任何一下。所以在她的脚底下的我并没有在她看书的过程中感到任何晃动。"
    "我的感觉仅仅只有压迫感，以及……"
    "闷热感。"
    "图书室的温度比外面的温度高，所以进图书室前的我还算处在一个适温的环境里。但她看书时就不同了。"

    window hide
    window show
    if location == 'shoe':
        "鞋内的空间逐渐开始升温，再过一会后，我感觉脸上的布料有些潮。"
        "她的脚出汗了呢。"
        "很快传来的是汗臭味，这味道弥漫整个空间。"
    elif location == 'sock':
        "贴近着自己的裸足的我，感受到自己脚底皮肤传来的热量。"
        "整个空间变得潮湿，是因为她的脚在冒出脚汗吧。"
        "不过这种感觉……还很有趣的？但是……"

    "一般的小人肯定是不能在这种环境下待多久的。"
    "而我不确定还能在这里待上多久，因为她可以决定怎样在此种条件下行动。"
    "先屏蔽一些体感。继续静候吧。"

    window hide
    window show
    "我感受到轻微的震动。好像有人走进图书室了。" with vpunch
    "？？？？" "请问你是？"
    "我听出来了，是长谷川茜的声音。"
    futaba_rg "我叫佐仓双叶。"
    "巨大的我做出了我会做的回答。"
    "其实如果巨大的我无法处理现状向我求救时，我可以选择再和她交换意识，替她处理现状。"
    "当然缺点也是有的，那就是在类似于我现在的处境下，她就得替我受罪。这一点她也明白。"
    "所以面对说话等小问题时，她会直接读取我的想法然后行动。"
    akane "我好像见过你吧？"
    futaba_rg "对啊，你不记得吗？"
    akane "啊，我想起来见到你的时候了。"
    scene f01-0042
    with squares
    "我接上巨大的我的视线后，看到长谷川茜也拿了一本书，并且走到了巨大的我旁边，然后坐了下来。"
    scene f01-0043
    with dissolve
    akane "我听三岛说你是心之怪盗团的一员？"
    scene f01-0044
    with dissolve
    futaba_rg "嗯……"
    "巨大的我有些惊讶。"
    "长谷川茜所说的三岛是指三岛由辉，「怪盗委托频道」（简称「怪盗ch」）的管理员。"
    futaba_rg "是的，不过三岛他，他怎么知道的？"
    scene f01-0045
    with dissolve
    akane "他说是一个不认识的人告诉他的，具体长什么样他没和我说。"
    futaba_rg "哦。那你是怎么认识三岛的？"
    akane "这是因为……"
    "她开始说自己的经历。"

    scene black with dissolve
    call akane_background_with_mishima
    scene black with dissolve

    scene f01-0046 with dissolve
    futaba_rg "原来是这样啊。"
    scene f01-0047
    with dissolve
    akane "那我们接着看书？"
    "长谷川茜这句话让我有些担忧，因为怕自己会不会待上很长的时间。"
    futaba_rg "你先看吧，我出去一下。"
    "所以。巨大的我决定让我出来了？"
    scene f01-0048
    with dissolve
    "然而她接下来告诉我的事情却让我大失所望。"
    futaba_rg "我想带你出去跑圈，八百米。"
    "这……这这这……"
    futaba "你这是要干什么？"
    futaba_rg "满足你曾经的妄想。"
    "这么说我之前还真有这种强烈的想法，可是……"
    "不对不对，我怎么可以就这么退缩？这合理吗？？"
    futaba "行，来吧。"
    akane "你要去哪儿？"
    "长谷川茜完全不知道我们两个的对话，哪怕是过程。因为我们的意识对话，无论多长都是瞬间完成的。"
    scene f01-0049
    with dissolve
    futaba_rg "出去跑圈，八百米。你也来吗？"
    scene f01-0050
    with dissolve
    akane "可以。"
    scene black
    "于是那种被自己的脚带起来又被踩下去的感觉再次出现。" with vpunch
    "不过想到接下来会有更剧烈的体感，这种感觉也显得微不足道。"

    window hide
    window show
    "巨大的我停了下来。"
    "不过我还不能松懈，接下来的我要体验比以前更加刺激的晃动与踩踏。"
    futaba_rg "小小的我，你要做好准备。以及……"
    futaba_rg "保重。"
    "我不知道长谷川茜如果听到这段对话会怎么想。"
    scene f01-0051
    with dissolve
    akane "预备——"
    "……"
    scene f01-0052
    with dissolve
    akane "跑！"
    scene black
    "随之而来是剧烈的摇晃和震动，以及更大的压迫感。" with vpunch
    "我就仿佛一下子被扔上天空，再被一下子带着前后乱扔，最后被重重一踩。整个过程大概只有 0.2 秒吧。" with vpunch
    "身体受得住，但我的脑袋可能会受不住。" with vpunch

    window hide
    window show
    if location == 'shoe':
        "鞋里的空间逐渐升温，丝袜也变得更加湿。"
        "再不一会，我感觉自己的脸很湿。"
        "她的脚汗已经透过丝袜直接浸泡我的脸。"
    elif location == 'sock':
        "整个空间差点就像泡水一样，潮湿的环境也在考验着我。"
        "她的脚汗直接接触到我的身体，浸泡着我的脸。"
    "……"
    "咕噜！"
    "……我刚才，是不是喝了她的脚汗？"
    "不管了不管了，还是尽力撑下去最重要。"

    window hide
    window show
    scene f01-0053
    with dissolve
    futaba_rg "三分钟。"
    akane "我是两分十五秒，我比你快！"
    scene f01-0054
    with dissolve
    futaba_rg "我去上厕所。"
    "巨大的我这次要把我拿出来了吧。"
    scene black
    with dissolve
    futaba_rg "小小的我，很快你就能出来了。"
    "果然。"
    "不过首先她还得去厕所，因为不能在长古川茜的面前把我拿出来。"
    "于是我在被拿出来之前还得被巨大的我带着走一会。"

    window hide
    window show

    "停下来了。"
    if location == 'shoe':
        scene f01-0055
        with dissolve
        "被丝袜包裹的脚从我的身上拿开。"
        scene f01-0056
        with dissolve
        "我走到鞋口下方。"
        scene f01-0057
        with dissolve
        "然后她的手从鞋口伸下来，抓住我。"
        scene f01-0058
        with dissolve
        "再被拿起来，放到手上。"
    elif location == 'sock':
        scene f01-0077
        with dissolve
        "她的脚从我的身上拿开。"
        scene f01-0078
        with dissolve
        "我走到袜子口的下方。"
        scene f01-0079
        with dissolve
        "然后她的手伸下来，抓住我。"
        scene f01-0058
        with dissolve
        "再被拿起来，放到手上。"
    futaba_rg "你没事吧，在脚底下的感觉怎么样？"
    scene f01-0059
    with dissolve
    futaba "嗯……有那么一点点的……刺激？"
    scene f01-0060
    with dissolve
    "她笑了。"
    futaba_rg "没想到呢。"
    futaba_rg "一般小人估计在这种情况下都说不出这种话的。"
    futaba "不过如果是我就不一样了。"
    scene f01-0061
    with dissolve
    "我也笑了。"
    scene f01-0062
    with dissolve
    futaba_rg "我要上厕所了，我先把你放在衣服口袋里了。回家就把你拿出来。"
    futaba "好的。"
    scene f01-0063
    with dissolve
    "随后她的手把我握住。"
    scene black
    with dissolve
    extend "我就这么进入了她的衣服口袋。"

    window hide
    window show

    scene f01-0064
    with dissolve
    "她上完厕所出来了。"
    scene f01-0065
    with dissolve
    akane "接下来我们去哪儿？"
    scene f01-0066
    with dissolve
    futaba_rg "回去看书，我们书还没看完呢。"
    akane "行。"
    "于是她和长古川茜又回到图书馆。"
    scene f01-0067
    with dissolve
    "我也接上她的视线，和她一起看书。"

    window hide
    scene black
    with dissolve
    window show

    scene f01-0068
    with dissolve
    futaba_rg "我看完了。"
    akane "我也看完了。"
    scene f01-0069
    with dissolve
    futaba_rg "那我回家了。"
    scene f01-0070
    with dissolve
    akane "我要和你一起回去吗？"
    futaba_rg "不用了。"
    akane "对了，别忘了把书放回去。"
    scene f01-0071
    with dissolve
    "她和长古川茜把书放回原处。"
    akane "我也回家了，再见！"
    futaba_rg "再见！"

    $ futaba_01_beneath_flag = True

    scene black
    with dissolve
    scene f01-0023
    with dissolve
    "我们回到了自己的家。"

    return

label futaba_01_tiny_reason:
    window hide
    scene black
    with dissolve
    window show
    """
    没错，现在在我的房间里，是有着两个我的。
    而且还是一个被缩小了一百倍的我和另一个我在一起。

    我创造一个缩小了一百倍的我自己的肉体，然后把自己的意识复制到那份身体里，并设定了一些思考参数。

    然后将自己的意识和那个我的意识交换一下，再让两个我都醒来。

    我的目的就是想要体验缩小时的视角。

    因为我有个特殊的爱好——{w}巨大少女。

    而这还是多亏了我们心之怪盗团的团长（雨宫莲）。

    当初我在他的手机里安装监听器之后，居然有了意外收获。

    我在他的手机里发现了大量含有一般人觉得离谱的大的少女的图片，还有带类似描写的文字和视频。

    纯粹的好奇让我也顺便进行了网络查阅，并最终导致了我踏入巨大少女的世界。

    不过因为当时还有很多任务要做，所以一直没有在意巨大少女相关的任何事情和情报。所以直到现在才有机会回顾那个爱好。

    今天就算是我的第一次实际体验吧。
    """

    return

# 所有选项清空后的后续剧情。
label futaba_01_post: # TODO: 所有选项清空后的后续剧情
    scene black
    with dissolve
    futaba "那么，今天就先到这里了。"
    futaba_rg "唉？"
    futaba_rg "你什么都不想玩了？"
    futaba "对啊，今天太累了。"
    futaba_rg "是……吗……"
    "就在这时……"
    window hide
    pause 2.0
    window show
    "我们家的门铃响了。"
    "？？？？" "你好，佐仓双叶，你有快递！"
    "快递到了？"
    "啊对，我记得我订了一样东西的。"
    futaba_rg "我去拿了。"
    "那个巨大的我开始走动。" with vpunch
    scene f01-0109
    with dissolve
    "然后将门打开。"
    scene black
    with dissolve
    scene f01-0110
    with dissolve
    "从那边拿过来一个盒子放了上去，而我也走到它的旁边。"
    "然后……"
    scene black
    with dissolve
    "她把盒子拿掉。"
    scene f01-0111
    with dissolve
    "在我眼前的是某个房间，我似乎一眼没认出来这是什么房间。"
    futaba_rg "这是你的房间呢。"
    "……"
    "哦，确实，我记得有这件事。"
    scene f01-0112
    with dissolve
    "我前往那个房间。"
    window auto
    scene f01-0113
    with dissolve
    pause 1.0
    scene f01-0114
    with dissolve
    pause 1.0
    scene black
    with dissolve
    "然后打开灯。"
    scene f01-0115
    with dissolve
    pause 1.0
    scene f01-0116
    with dissolve
    "这里真的很空啊。"
    "不过那也是当然的，因为我是通过 3D 打印做出的这个我的房间的。更精细一点的东西是做不出来的，不过还好灯光可以通过小型 LED 灯解决。"
    "这时我也感到有些困了。"
    "我准备去睡觉。"
    scene f01-0117
    with dissolve
    futaba_rg "那，晚安。"
    "她通过和我的感官共享了解了我要去睡觉的这件事。"
    "我在想，如果团长知道了我也踏入巨大少女的世界并且做了实际体验之后，他会是什么想法呢。"
    "我甚至可以考虑把团长也缩小……"
    "不过这些都是后话了。"
    scene black
    with dissolve
    "我把灯关掉。"
    "然后，沉沉地睡去……"
    ### 佐仓双叶篇 / 第一章：初做小人 结束点
    window hide
    # 阻止回滚。
    $ renpy.block_rollback()
    $ quick_menu = False
    $ _game_menu_screen = None
    show black
    with Dissolve(5.0)
    show text "{color=#FFFFFF}{b}TO BE CONTINUED......{/b}{/color}"
    with Dissolve(5.0)
    pause
    hide text
    with Dissolve(5.0)
    return
