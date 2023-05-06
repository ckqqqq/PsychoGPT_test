from toolbox import HotReload  # HotReload 的意思是热更新，修改函数插件后，不需要重启程序，代码直接生效


def get_crazy_functions():
    from crazy_functions.询问多个大语言模型 import 同时问询_指定模型
    function_plugins={
        "询问多个GPT模型（手动指定询问哪些模型）": {
            "Color": "stop",
            "AsButton": False,
            "AdvancedArgs": True, # 调用时，唤起高级参数输入区（默认False）
            "ArgsReminder": "支持任意数量的llm接口，用&符号分隔。例如chatglm&gpt-3.5-turbo&api2d-gpt-4", # 高级参数输入区的显示提示
            "Function": HotReload(同时问询_指定模型)
        },
    }
    from crazy_functions.联网的ChatGPT import 连接网络回答问题
    function_plugins.update({
        "连接网络回答问题（先输入问题，再点击按钮，需要访问谷歌）": {
            "Color": "stop",
            "AsButton": False,  # 加入下拉菜单中
            "Function": HotReload(连接网络回答问题)
        }
    })
    ###################### 第n组插件 ###########################
    return function_plugins
