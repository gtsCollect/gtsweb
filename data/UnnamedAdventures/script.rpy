# 初始化脚本区域
# 主控流程会从这里一路进行跳跃

default persistent.gamepad = "auto"

# 此处定义各种其他脚本文件中用到的函数
init python:
    def text_truncate(text):
        if len(text) > 30:
            return "{}...".format(text[:30])
        else:
            return text

    # 把摇杆的默认绑定全删了
    del config.pad_bindings["pad_leftx_neg"]
    del config.pad_bindings["pad_leftx_pos"]
    del config.pad_bindings["pad_rightx_neg"]
    del config.pad_bindings["pad_rightx_pos"]
    del config.pad_bindings["pad_lefty_neg"]
    del config.pad_bindings["pad_lefty_pos"]
    del config.pad_bindings["pad_righty_neg"]
    del config.pad_bindings["pad_righty_pos"]
    del config.pad_bindings["repeat_pad_leftx_neg"]
    del config.pad_bindings["repeat_pad_leftx_pos"]
    del config.pad_bindings["repeat_pad_rightx_neg"]
    del config.pad_bindings["repeat_pad_rightx_pos"]
    del config.pad_bindings["repeat_pad_lefty_neg"]
    del config.pad_bindings["repeat_pad_lefty_pos"]
    del config.pad_bindings["repeat_pad_righty_neg"]
    del config.pad_bindings["repeat_pad_righty_pos"]
    del config.pad_bindings["pad_righttrigger_pos"]
    del config.pad_bindings["pad_lefttrigger_pos"]
    del config.pad_bindings["repeat_pad_lefttrigger_pos"]
    del config.pad_bindings["pad_back_press"]
    del config.pad_bindings["repeat_pad_back_press"]

    def current_text_callback(d):
        d["current_text"] = _last_say_what

    config.save_json_callbacks.append(current_text_callback)

label start:

    show screen _gamepad_extras
    ### 佐仓双叶篇 / 第一章：初做小人
    jump futaba_01
    return
