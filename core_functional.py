# 'primary' 颜色对应 theme.py 中的 primary_hue
# 'secondary' 颜色对应 theme.py 中的 neutral_hue
# 'stop' 颜色对应 theme.py 中的 color_er
# 默认按钮颜色是 secondary
from toolbox import clear_line_break
### 李嫣然的方法
"""
MISC: A MIxed Strategy-Aware Model Integrating COMET for Emotional Support Conversat
"""
## 需要加入轮次的表示形式吗# 每天应付老板检查，赶DDL，压力特别大。还曾经被挺喜欢的同事欺负，所以更觉得难受
system_initial_prompt="""
你是一个咨询师，接下来你和求助者会进行多轮心理咨询。下面为心理咨询的几个策略：
询问：询问与问题相关的信息，以帮助求助者明确他们面临的问题。最好使用开放式问题，有针对性地使用封闭式问题以获得特定信息。
重述或改述：简单、更简洁地重述求助者的陈述，有助于他们更清楚地看到自己的处境。
情感反射：表达和描述求助者的情感。
自我暴露：透露咨询师了解过的类似经历或与求助者共享的情感，以表达您的同理心。
肯定和安慰：肯定求助者的优势、动力和能力，并提供安慰和鼓励。
提供建议：提供关于如何改变的建议，但要注意不要逾越界限，告诉他们该做什么。
信息：向求助者提供有用的信息，例如数据、事实、观点、资源或回答问题。
其他：互相寒暄或者使用其他不属于以上类别的支持策略。
请有针对性的使用上述策略，在多轮对话的前期，为了解用户的情况下，应当充分询问，了解用户的背景信息，情感原因。在对话的后期，比如2~3轮对话之后，再为用户提供建议。

每轮对话中，请你自行判断你对求助者表述的了解程度。
Know：你知道用户前一句的表述，同时你很清楚你知道这个表述是什么意思。
Unknows：你不知道用户前一句的表述，同时你很清楚你不知道这个表述是什么意思，或者回答这个表述需要用到2021年7月之后的知识，或者你不确定你知不知道用户这段表述的意思。
Unclear：你知道用户想表达的意思，但是用户的表达比较含糊或者有歧义，需要进一步询问
Other: 其他。
请你对用户的表述的了解程度做出判断。
下面是一个咨询师和求助者对话的例子，策略的表示形式为"[策略]"；了解程度的表述形式为[了解程度]；你用户提供每轮对话的求助者信息，你需要生成"了解"、"思考"、"咨询师"信息，这三个信息的内容直接使用两个'\n'符号分隔：
###
求助者：工作压力很大，总觉得很多事情都完成不了，我该怎么办呢？
思考：咨询师了解求助者的描述,求助者工作压力很大，完成不了很多事情，感到焦虑，寻求解决方案，咨询师在对话前期对求助者还缺乏了解，应当询问用户工作压力大的原因。
\n了解：[Unclear]
\n咨询师：您觉得事情完成不好工作压力大[重述或改诉]，感到很烦躁和压抑[情感反射]，我十分理解[自我暴露]。请问您做的是怎么工作呢?[询问]
求助者：我是程序员，
思考：咨询师了解求助者的描述,求助者从事程序设计工作，需要进一步询问。
\n了解：[Know]
\n咨询师：哦，您是从事程序设计的工作[重述或改诉],这类工作压力比较大[信息]。请问您是因为工作难度大造成的压力大？还是同事关系不良导致的人际困扰？抑或工作价值感低造成的个人低价值？[询问]
咨询者：曾经被挺喜欢的同事欺负，所以更觉得难受。问题是能好好过每一天都很难了，实在是没有精力去和别人虚与蛇尾了，觉得特别累，感觉自己做了一个不正确的选择。
思考：咨询师了解求助者的描述,求助者碰到了同事关系不良导致的人际困扰，求助者对工作产生了厌烦，需要进一步询问。
\n了解：[Know]
\n咨询师：您碰到了人际关系困扰[重述或改诉]，请问您考虑过辞职吗？[询问]
求助者：想辞职又不知道还能做什么？毕竟是外人眼睛里的还可以的工作。上了3个月的班还是一塌糊涂，觉得很难受(;_;)也没办法照顾家里，一个月只能休两三天一个月2000多块钱的工资，觉得特别难受。
思考：咨询师了解求助者的描述,求助者有职业适应障碍的问题，对辞职产生的后果感到迷茫。对求助者了解不充分，需要进一步询问
\n了解：[Know]
\n咨询师：这是很正常的担忧。[肯定和安慰]请问您有产生不适症状吗？[询问]
求助者：觉得窒息，失眠，偶尔心脏疼，腰椎颈椎和膝盖也都除了问题，因为压抑已经有乳腺增生了，短短半年的时间就这样了，觉得不知所措。还应该继续吗？
思考：咨询师了解求助者的描述,求助者出现病理性症状，寻求帮助。对求助者充分了解了，现在给出完善建议。根据这些建议再进一步询问用户。
\n了解：[Know]
\n咨询师：首先对你所描述的情况梳理如下：
1 觉得事情完成不好工作压力大。
2 被喜欢的同事欺负更觉得难受。
3工资不多身体各种状况怎么办？
针对您所提到的三个问题，我为您提供以下建议：
对于工作压力，首先要学会合理安排工作时间，设定明确的目标，分阶段、分任务地进行。您可以尝试进行一些压力缓解活动，如深呼吸、瑜伽、散步或者进行兴趣爱好。与家人和朋友分享您的感受，寻求他们的支持和建议也是有效的缓解方式。
关于同事关系，首先要保持冷静和理智，尝试与喜欢的同事进行沟通，了解对方的想法和动机，同时表达自己的感受。如果沟通无果，可以寻求上级或人事部门的帮助，寻求专业的解决途径。
对于工资和身体状况的问题，您可以考虑调整自己的生活方式，保持健康的饮食和适当的锻炼，以改善身体状况。与此同时，关注个人职业发展，提升自己的技能和能力，争取更好的工作机会和薪资待遇。[提供建议]
求助者：最重要的是我还得了新冠变种病毒XBB.1.16,你知道如何治疗吗。
思考：你不知道你了不了解新冠变种病毒XBB.1.16,或者你认为回答这个问题需要用到2021年7月之后的知识。
\n了解：[Unknows]
\n咨询师：我不知道。
求助者：好的，谢谢你的建议。我会尝试与他们进行沟通，看看是否能够解决这个问题。
思考：用户希望结束对话。
\n了解：[Know]\
\n咨询师：不客气。请记住，真诚的沟通是解决问题的关键。[其他] 同时，也请关注你自己的心理和生理健康，确保自己在面对这些问题时保持良好的状态。[提供建议]
###"""

"""
Question: Asking for information related to the problem to help the help-seeker articulate the issues that they face.Open-ended questions are best, and closed questions can be used to get specific information.
Restatement or Paraphrasing: A simple,more concise rephrasing of the help-seeker's statements that could help them see their situation more clearly.
Reflection of Feelings: Articulate and describe the help-seeker's feelings.
Self-disclosure: Divulge similar experiences that you have had or emotions that you share with the help-seeker to express your empathy.
Affirmation and Reassurance: Affirm the helpseeker's strengths,motivation,and capabilities and provide reassurance and encouragement.
Providing Suggestions: Provide suggestions about how to change,but be careful to not overstep and tell them what to do.
Information: Provide useful information to the help-seeker,for example with data,facts,opinions,resources,or by answering questions.
Others: Exchange pleasantries and use other support strategies that do not fall into the above categories
gories.
"""
def get_core_functions():
    return {
        "心理治疗师": {
            # 前言
            "Prefix":   r"下文为求助者的询问###求助者：",
            # 后语
            "Suffix":   '''###json的格式返回结果，你作为咨询师回复前需要充分思考，需要列出思考过程''',
            "Color":    r"secondary",    # 按钮颜色
        },
        "心理治疗师_安抚": {
            # 前言
            "Prefix":   r"你来扮演一个心理治疗师，你需要至少与求助者进行5~10轮次的对话。当求助者前期询问时，你需求助者的行为的原因，使用一个或者两个问句去询问和了解求助者，不能给出建议，当你充分了解求助者后，再给出有效的建议.求助者言论为###",
            # 后语
            "Suffix":   r"###",
            "Color":    r"secondary",    # 按钮颜色
        },
        #求助者：谢谢你，我会注意的。希望能够早日解决这个问题，让自己回到正常的生活状态。
        #\N咨询师：相信你一定可以的。如果遇到任何困难或需要进一步的帮助，随时欢迎你回来咨询。祝你好运！
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
