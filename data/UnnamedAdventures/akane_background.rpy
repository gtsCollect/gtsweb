# 长古川茜的背景剧情（暂定草稿）

define mishima = Character(_("三岛由辉"))

# NVL 模式的角色
# 此处的 NVL 模式用于渲染成聊天对话框
# 对话框 UI 待完成
define mishima_nvl = Character(_("三岛由辉"), kind=nvl)
define akane_nvl = Character(_("长古川茜"), kind=nvl)

# 第一次遇见三岛由辉
label akane_background_with_mishima:
    """
    长古川茜第一次遇见三岛由辉是在她自己运营的怪盗直播间里。

    那天三岛由辉在直播间的评论区里对她说：
    """
    mishima "那个……我很喜欢心之怪盗团，可以宣传一下我的委托频道吗？"
    "长古川茜在底下回复道："
    akane "嗯……我不太建议你这么做，可能会被当成发广告的被踢出去。"
    extend "你要是有想法可以私聊我。"

    "三岛由辉后来在私聊里向长古川茜介绍了一下自己："

    # 进入 NVL
    window hide
    nvl show dissolve

    mishima_nvl "我的名字叫三岛由辉，{p}我这次来是想宣传一下怪盗委托频道的。"
    akane_nvl "怪盗委托频道是？"
    mishima_nvl """
    那是我开设的一个支援频道，

    以前那里还支持发起委托，现在因为怪盗团的活动已经结束了，所以不需要了。

    说起来你也喜欢心之怪盗团？
    """
    akane_nvl "嗯是的，至于为什么呢，{p}我不告诉你～"

    nvl clear

    mishima_nvl "对了，咱们要不要见面？{p}我们正好也可以交换情报。"
    akane_nvl "嗯……"
    extend "可以。"

    # 退出 NVL
    nvl hide dissolve
    window show

    scene akane_meeting_mishima
    with dissolve
    """
    二人就这么见了面并且交换了情报。

    长古川茜也借此机会了解了心之怪盗团的真实身份。
    """

    return
