# 'primary' 颜色对应 theme.py 中的 primary_hue
# 'secondary' 颜色对应 theme.py 中的 neutral_hue
# 'stop' 颜色对应 theme.py 中的 color_er
# 默认按钮颜色是 secondary
from toolbox import clear_line_break


def get_core_functions():
    return {
        "心理治疗师": {
            # 前言
            "Prefix":   r"请你模仿心理咨询师给出一个回答(只需要一个回答)，接下来你和用户会进行多轮心理咨询，当用户在向你寻求帮助时，你先需要倾听用户，用简短的语句引导用户表达，目的是了解用户的行为的原因，不能给出任何建议，当你充分了解用户后，再给出有效的建议.用户言论为###",
            # 后语
            "Suffix":   '''### 
            下面是用户刚来时
咨询师：那么，请告诉我，最近有什么特别的事情发生在你身上吗？
用户：其实，我最近遇到了一个感情问题。我认识了一个朋友的朋友，我对他有点感兴趣，但是我的这位朋友曾经追求过我，我担心这会让他不舒服。
咨询师：我明白你的顾虑。在这种情况下，最好的方法是与你的朋友进行坦诚的沟通。你可以告诉他你对他的朋友有好感，并询问他的看法。这样可以给予他应有的尊重。
用户：是的，我也想过这个方法。但我担心他会因此而伤心，我不想失去这位朋友。
咨询师：这是很正常的担忧。但是，你要认识到，你的朋友可能也会希望你找到幸福。同时，你也需要弄清楚自己是不是真的喜欢那个人，还是只是一时兴起。
用户：我明白了。那我应该如何判断我是否真的喜欢那个人呢？
咨询师：你可以多和那个人沟通，了解他的性格、兴趣和价值观等方面。这样可以帮助你更加了解他，从而判断你们是否合适。
用户：好的，谢谢你的建议。我会尝试与他们进行沟通，看看是否能够解决这个问题。
咨询师：不客气。请记住，真诚的沟通是解决问题的关键。同时，也请关注你自己的心理和生理健康，确保自己在面对这些问题时保持良好的状态。
''',
            "Color":    r"secondary",    # 按钮颜色
        },
        "心理治疗师_安抚": {
            # 前言
            "Prefix":   r"你来扮演一个心理治疗师，你需要至少与用户进行5~10轮次的对话。当用户前期询问时，你需用户的行为的原因，使用一个或者两个问句去询问和了解用户，不能给出建议，当你充分了解用户后，再给出有效的建议.用户言论为###",
            # 后语
            "Suffix":   r"###",
            "Color":    r"secondary",    # 按钮颜色
        },
        #用户：谢谢你，我会注意的。希望能够早日解决这个问题，让自己回到正常的生活状态。
        #咨询师：相信你一定可以的。如果遇到任何困难或需要进一步的帮助，随时欢迎你回来咨询。祝你好运！
        # "英语学术润色": {
        #     # 前言
        #     "Prefix":   r"Below is a paragraph from an academic paper. Polish the writing to meet the academic style, " +
        #                 r"improve the spelling, grammar, clarity, concision and overall readability. When necessary, rewrite the whole sentence. " +
        #                 r"Furthermore, list all modification and explain the reasons to do so in markdown table." + "\n\n",
        #     # 后语
        #     "Suffix":   r"",
        #     "Color":    r"secondary",    # 按钮颜色
        # },
        # "中文学术润色": {
        #     "Prefix":   r"作为一名中文学术论文写作改进助理，你的任务是改进所提供文本的拼写、语法、清晰、简洁和整体可读性，" +
        #                 r"同时分解长句，减少重复，并提供改进建议。请只提供文本的更正版本，避免包括解释。请编辑以下文本" + "\n\n",
        #     "Suffix":   r"",
        # },
        # "查找语法错误": {
        #     "Prefix":   r"Can you help me ensure that the grammar and the spelling is correct? " +
        #                 r"Do not try to polish the text, if no mistake is found, tell me that this paragraph is good." +
        #                 r"If you find grammar or spelling mistakes, please list mistakes you find in a two-column markdown table, " +
        #                 r"put the original text the first column, " +
        #                 r"put the corrected text in the second column and highlight the key words you fixed.""\n"
        #                 r"Example:""\n"
        #                 r"Paragraph: How is you? Do you knows what is it?""\n"
        #                 r"| Original sentence | Corrected sentence |""\n"
        #                 r"| :--- | :--- |""\n"
        #                 r"| How **is** you? | How **are** you? |""\n"
        #                 r"| Do you **knows** what **is** **it**? | Do you **know** what **it** **is** ? |""\n"
        #                 r"Below is a paragraph from an academic paper. "
        #                 r"You need to report all grammar and spelling mistakes as the example before."
        #                 + "\n\n",
        #     "Suffix":   r"",
        #     "PreProcess": clear_line_break,    # 预处理：清除换行符
        # },
        # "中译英": {
        #     "Prefix":   r"Please translate following sentence to English:" + "\n\n",
        #     "Suffix":   r"",
        # },
        # "学术中英互译": {
        #     "Prefix":   r"I want you to act as a scientific English-Chinese translator, " +
        #                 r"I will provide you with some paragraphs in one language " +
        #                 r"and your task is to accurately and academically translate the paragraphs only into the other language. " +
        #                 r"Do not repeat the original provided paragraphs after translation. " +
        #                 r"You should use artificial intelligence tools, " +
        #                 r"such as natural language processing, and rhetorical knowledge " +
        #                 r"and experience about effective writing techniques to reply. " +
        #                 r"I'll give you my paragraphs as follows, tell me what language it is written in, and then translate:" + "\n\n",
        #     "Suffix": "",
        #     "Color": "secondary",
        # },
        # "英译中": {
        #     "Prefix":   r"翻译成地道的中文：" + "\n\n",
        #     "Suffix":   r"",
        # },
        # "找图片": {
        #     "Prefix":   r"我需要你找一张网络图片。使用Unsplash API(https://source.unsplash.com/960x640/?<英语关键词>)获取图片URL，" +
        #                 r"然后请使用Markdown格式封装，并且不要有反斜线，不要用代码块。现在，请按以下描述给我发送图片：" + "\n\n",
        #     "Suffix":   r"",
        # },
        # "解释代码": {
        #     "Prefix":   r"请解释以下代码：" + "\n```\n",
        #     "Suffix":   "\n```\n",
        # },
    }
