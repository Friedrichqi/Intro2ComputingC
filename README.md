# 计算概论C大作业——西游记

# 2024.12.12

# 西游记

Part 1：使用requests库和BeautifulSoup库爬取西游记的前十章，并写入XYJ\.txt

Part 2：使用openai库调用deepseek的大模型，对XYJ\.txt中的前十章的内容每章进行概括写入summary\.txt中，并对第一章（或者自己喜欢的一个章节）生成一篇读后感写入readingResponse\.txt

Part 3：根据模板完成实验报告，分析机器生成的摘要和读后感文本的优缺点

# Part 1：爬虫部分——requests库

__requests __  __是一个用于发送 __  __HTTP __  __请求的 __  __Python __  __库__

__常用于与网络资源交互，如获取网页内容、提交表单、上传文件等。__

__网页内容可以是文本文件，如__  __HTML__  __网页，文本文件，__  __JSON__  __数据。__

__也可以是二进制资源，如图片，音频，视频，压缩包等__

__安装：__  __pip install requests__

__导入 __  __import requests__

[Python requests ](https://www.runoob.com/python3/python-requests.html)[模块 ](https://www.runoob.com/python3/python-requests.html)[| ](https://www.runoob.com/python3/python-requests.html)[菜鸟教程](https://www.runoob.com/python3/python-requests.html)

确定需要爬取的网页网址

通过requests\.get\(\)函数爬取网页内容

可以将网页内容保存到本地文件中，以便后续使用BeautifulSoup库进行解析

![](img%5Cslides_0.png)

![](img%5Cslides_1.png)

深蓝色的是标签名，如head、script、div、a、ul、li

浅蓝色的是属性，如lang、src、class

等号后面的是该属性的具体取值

# Part 1：爬虫部分——BeautifulSoup库

__BeautifulSoup__  __ __  __是一个可以从__  __HTML__  __或__  __XML__  __文件中提取数据的__  __Python__  __库__  __\, __  __它能够通过你喜欢的转换器实现惯用的文档导航__  __\,__  __查找__  __\,__  __修改文档的方式__

__安装方式 __

__pip install beautifulsoup4__  __（注意最后有个__  __4__  __）__

__安装解析器  __

__pip install __  __lxml__  __ html5lib__

在通过requests库爬取得到网页内容后，使用BeautifulSoup库对网页内容进行解析，提取出我们需要的章节标题和内容

可以在之前保存在本地的XYJ\.html文件中定位我们要爬取的内容

![](img%5Cslides_2.png)

也可以使用Edge或者Chrome浏览器，按F12直接定位我们要爬取的内容

![](img%5Cslides_3.png)

用BeautifulSoup\(\)函数对之前爬取的r\.text进行解析

假如我们想要爬取菜单栏里的所有类别，通过之前的定位方法进行定位得知他在一个标签名为ul，属性class的值为nav的元素里

![](img%5Cslides_4.png)

![](img%5Cslides_5.png)

![](img%5Cslides_6.png)

用soup\.find\(\)函数进行查找，返回满足该条件的第一个元素

![](img%5Cslides_7.png)

![](img%5Cslides_8.png)

当有多个满足条件的元素时，用soup\.find\_all\(\)函数进行查找，返回满足该条件的元素列表

\.text可以直接返回该元素文本内容

![](img%5Cslides_9.png)

![](img%5Cslides_10.png)

我们需要爬取的是章节标题和章节内容

![](img%5Cslides_11.png)

爬取完成后，将每一章的标题和内容写入“XYJ\.txt”中，该部分需要提交 <span style="color:#ff0000"> __爬虫代码__ </span>  <span style="color:#ff0000"> __crawler\.py__ </span>  <span style="color:#ff0000"> __和结果文件__ </span>  <span style="color:#ff0000"> __XYJ\.txt__ </span> ，我们将抽取部分同学的代码运行。

![](img%5Cslides_12.png)

# Part 2：大模型部分——openai库

使用openai库调用deepseek的大模型，对XYJ\.txt中的前十章的内容每章进行概括，并对第一章（或者自己喜欢的一个章节）生成一篇读后感写入reading\_ response\.txt

__OpenAI__  __库有__  __OpenAI__  __公司开发，是一个用于与__  __OpenAI__  __提供的服务（如__  __GPT__  __模型和__  __DALL·E__  __）进行交互的__  __Python__  __客户端工具包。通过该库，开发者可以方便地将__  __OpenAI__  __的自然语言处理、图像生成等功能集成到自己的项目中。__

__国内的大模型公司__  __Deepseek__  __对__  __OpenAI__  __库做了兼容，我们可以直接用__  __OpenAI__  __库调用__  __Deepseek__  __的大模型服务__

__安装：__

__pip install __  __openai__

__前往__  __Deepseek__  __开放平台注册账号，获取__  __API Key__  __，将其保存起来__

__网址：__  __https://platform\.deepseek\.com__

![](img%5Cslides_13.png)

<span style="color:#ff0000"> __剩余总__ </span>  <span style="color:#ff0000"> __token__ </span>  <span style="color:#ff0000"> __数，由余额计算而来__ </span>

<span style="color:#ff0000"> __余额，__ </span>  <span style="color:#ff0000"> __Deepseek__ </span>  <span style="color:#ff0000"> __注册会赠送￥__ </span>  <span style="color:#ff0000"> __10__ </span>  <span style="color:#ff0000"> __，一个月后过期，可以自行充值__ </span>

![](img%5Cslides_14.png)

<span style="color:#ff0000"> __已有的__ </span>  <span style="color:#ff0000"> __API Key__ </span>  <span style="color:#ff0000"> __，你可以删除它们，但是不能查看内容__ </span>

![](img%5Cslides_15.png)

<span style="color:#ff0000"> __已有的__ </span>  <span style="color:#ff0000"> __API Key__ </span>  <span style="color:#ff0000"> __，你可以删除它们，但是不能查看内容__ </span>

![](img%5Cslides_16.png)

![](img%5Cslides_17.png)

<span style="color:#ff0000"> __在这个界面，把__ </span>  <span style="color:#ff0000"> __API Key__ </span>  <span style="color:#ff0000"> __复制下来，否则后续无法查看__ </span>

<span style="color:#ff0000"> __如果你忘记复制了，你可以删除再重新创建一次__ </span>

<span style="color:#008000">\# </span>  <span style="color:#008000">需要先安装 </span>  <span style="color:#008000">openai</span>  <span style="color:#008000"> </span>  <span style="color:#008000">包，</span>  <span style="color:#008000">pip install </span>  <span style="color:#008000">openai</span>

<span style="color:#008000">\# </span>  <span style="color:#008000">导入 </span>  <span style="color:#008000">OpenAI</span>  <span style="color:#008000"> </span>  <span style="color:#008000">类</span>

<span style="color:#0000ff">from</span>  <span style="color:#000000"> </span>  <span style="color:#000000">openai</span>  <span style="color:#000000"> </span>  <span style="color:#0000ff">import</span>  <span style="color:#000000"> </span>  <span style="color:#2b91af">OpenAI</span>

<span style="color:#008000">\# </span>  <span style="color:#008000">创建客户端（整个程序只需要写一次），使用您的 </span>  <span style="color:#008000">API </span>  <span style="color:#008000">密钥</span>

<span style="color:#008000">\#</span>  <span style="color:#008000">如果您使用的是 </span>  <span style="color:#008000">DeepSeek</span>  <span style="color:#008000"> </span>  <span style="color:#008000">的 </span>  <span style="color:#008000">API</span>  <span style="color:#008000">，</span>  <span style="color:#008000">base\_url</span>  <span style="color:#008000"> </span>  <span style="color:#008000">参数请设置为 </span>  <span style="color:#008000">"https://api\.deepseek\.com"</span>

<span style="color:#000000">client = </span>  <span style="color:#2b91af">OpenAI</span>  <span style="color:#000000">\(</span>  <span style="color:#808080">api\_key</span>  <span style="color:#000000">=</span>  <span style="color:#a31515">"</span>  <span style="color:#a31515">sk\-xxxxxxxxxxxxxxxxxxxxxxx</span>  <span style="color:#a31515">"</span>  <span style="color:#000000">\, </span>  <span style="color:#808080">base\_url</span>  <span style="color:#000000">=</span>  <span style="color:#a31515">"https://api\.deepseek\.com"</span>  <span style="color:#000000">\)</span>

<span style="color:#008000">\# </span>  <span style="color:#008000">调用对话接口</span>

<span style="color:#000000">response = </span>  <span style="color:#000000">client\.chat\.completions\.create</span>  <span style="color:#000000">\(</span>

<span style="color:#000000">    </span>  <span style="color:#808080">model</span>  <span style="color:#000000">=</span>  <span style="color:#a31515">"</span>  <span style="color:#a31515">deepseek</span>  <span style="color:#a31515">\-chat"</span>  <span style="color:#000000">\,</span>

<span style="color:#000000">    </span>  <span style="color:#808080">messages</span>  <span style="color:#000000">=\[</span>

<span style="color:#000000">        \{</span>  <span style="color:#a31515">"role"</span>  <span style="color:#000000">: </span>  <span style="color:#a31515">"system"</span>  <span style="color:#000000">\, </span>  <span style="color:#a31515">"content"</span>  <span style="color:#000000">: </span>  <span style="color:#a31515">"You are a helpful assistant\."</span>  <span style="color:#000000">\}\,</span>

<span style="color:#000000">        \{</span>  <span style="color:#a31515">"role"</span>  <span style="color:#000000">: </span>  <span style="color:#a31515">"user"</span>  <span style="color:#000000">\, </span>  <span style="color:#a31515">"content"</span>  <span style="color:#000000">: </span>  <span style="color:#a31515">"</span>  <span style="color:#a31515">如何做一个蛋糕</span>  <span style="color:#a31515">"</span>  <span style="color:#000000">\}</span>

<span style="color:#000000">    \]\,</span>

<span style="color:#000000">\)</span>

<span style="color:#000000">print\(</span>  <span style="color:#000000">response\.choices</span>  <span style="color:#000000">\[</span>  <span style="color:#098658">0</span>  <span style="color:#000000">\]\.</span>  <span style="color:#000000">message\.content</span>  <span style="color:#000000">\)</span>

![](img%5Cslides_18.png)



* __api\_key__  __: __  __填写你获取到的__  __API Key__
* __base\_url__  __: __  __大模型__  __API__  __的网址，此处我们使用的是__  __deepseek__  __的__  __API__  __网址__
  * __OpenAI__  __的__  __API__  __与__  __DeepSeek__  __的__  __API__  __是兼容的，如果你有__  __OpenAI__  __的开发平台账号，你可以填写__  <span style="color:#0563c1"> __[https://api\.openai\.com/v1](https://api.openai.com/v1来使用GPT-4)__ </span>  <span style="color:#0563c1"> __[来使用](https://api.openai.com/v1来使用GPT-4)__ </span>  __[GPT\-4](https://api.openai.com/v1来使用GPT-4)__


![](img%5Cslides_19.png)

__model: __  __你是用的模型名称，__  __deepseek__  __目前只提供__  __deepseek__  __\-chat__

__	__  __如果你使用__  __openai__  __的服务，则你有很多模型可选，如__  __gpt\-4o__  __，__  __gpt\-4o\-mini__  __，__  __gpt\-3\.5__  __之类的__

![](img%5Cslides_20.png)

__messages__  __（重点）：__

__messages__  __是一个列表，列表中的每一项是一个字典，列表的项数必须是偶数__

__每个字典必须有两项内容__

__	__  __一个字典项的键必须是__  __role\, __  __值必须是__  __system\, user\, assistant__  __中的一个，如果是列表中的第__  __0__  __项，则必须是__  __system__  __，如果是列表中的第奇数项，必须是__  __user__  __，如果是列表中的第偶数项，必须是__  __assistant__

__	__  __另一个字典项的键必须是__  __content__  __，值代表角色说的内容，不能是空__

![](img%5Cslides_21.png)

![](img%5Cslides_22.png)

__system__  __：你是一个人工智能助手。__

__user__  __：如何做一个蛋糕？__

<span style="color:#ff0000">messages=\[</span>

<span style="color:#ff0000">    \{"role": "system"\, "content": "</span>  <span style="color:#ff0000">你是一个人工智能助手。</span>  <span style="color:#ff0000">"\}\,</span>

<span style="color:#ff0000">    \{"role": "user"\, "content": "</span>  <span style="color:#ff0000">如何做一个蛋糕？ </span>  <span style="color:#ff0000">"\}</span>

<span style="color:#ff0000">\]</span>

<span style="color:#0070c0"> __运行结果：__ </span>

<span style="color:#0070c0"> __	__ </span>  <span style="color:#0070c0"> __制作蛋糕的过程可以分为几个主要步骤，包括准备材料、混合、烘焙和装饰。以下是一个基础的蛋糕制作指南：__ </span>  <span style="color:#0070c0"> __……__ </span>

__system__  __：你是一个人工智能助手。__

__user__  __：请你记住，我喜欢的颜色是红色。__

__assistant__  __：好的，我会记住你喜欢的颜色是红色。__

__user__  __：我喜欢什么颜色？__

<span style="color:#ff0000">messages=\[</span>

<span style="color:#ff0000">    \{"role": "system"\, "content": "</span>  <span style="color:#ff0000">你是一个人工智能助手。</span>  <span style="color:#ff0000">"\}\,</span>

<span style="color:#ff0000">    \{"role": "user"\, "content": "</span>  <span style="color:#ff0000">请你记住，我喜欢的颜色是红色。</span>  <span style="color:#ff0000">"\}\,</span>

<span style="color:#ff0000">    \{"role": "assistant"\, "content": "</span>  <span style="color:#ff0000">好的，我会记住你喜欢的颜色是红色。</span>  <span style="color:#ff0000">"\}\,</span>

<span style="color:#ff0000">    \{"role": "user"\, "content": "</span>  <span style="color:#ff0000">我喜欢什么颜色？</span>  <span style="color:#ff0000">"\}\,</span>

<span style="color:#ff0000">\]</span>

<span style="color:#0070c0"> __运行结果：__ </span>

<span style="color:#0070c0"> __	__ </span>  <span style="color:#0070c0"> __你喜欢的颜色是红色。__ </span>

__system__  __：你是一个人工智能助手。__

__user__  __：请你记住，我喜欢的颜色是红色。__

__assistant__  __：好的，我会记住你喜欢的颜色是红色。__

__user__  __：我喜欢什么颜色？__

<span style="color:#0070c0"> __为什么之前的__ </span>  <span style="color:#0070c0"> __assistant__ </span>  <span style="color:#0070c0"> __也需要我写，不是大模型生成的吗？__ </span>

<span style="color:#0070c0"> __对话调用__ </span>  <span style="color:#0070c0"> __API__ </span>  <span style="color:#0070c0"> __是无状态的。__ </span>

<span style="color:#0070c0"> __也就是说服务器不会记之前的对话是什么，你必须把之前的对话的内容也告诉他。既包括你问他的，也包括他回答给你的。让大模型把之前的对话内容再看一遍，然后生成最后一个问题的回复。__ </span>

<span style="color:#0070c0"> __这也就意味着，你可以随便瞎写__ </span>  <span style="color:#0070c0"> __assistant__ </span>  <span style="color:#0070c0"> __的回复，让他以为自己之前说了这些东西。__ </span>

<span style="color:#0000ff">from</span>  <span style="color:#000000"> </span>  <span style="color:#000000">openai</span>  <span style="color:#000000"> </span>  <span style="color:#0000ff">import</span>  <span style="color:#000000"> </span>  <span style="color:#2b91af">OpenAI</span>

<span style="color:#000000">client = </span>  <span style="color:#2b91af">OpenAI</span>  <span style="color:#000000">\(</span>  <span style="color:#808080">api\_key</span>  <span style="color:#000000">=</span>  <span style="color:#a31515">"sk\-a78ce9f85ce84c41aa1f9cfa10bdf57b"</span>  <span style="color:#000000">\, </span>  <span style="color:#808080">base\_url</span>  <span style="color:#000000">=</span>  <span style="color:#a31515">"https://api\.deepseek\.com"</span>  <span style="color:#000000">\)</span>

<span style="color:#000000">response = </span>  <span style="color:#000000">client\.chat\.completions\.create</span>  <span style="color:#000000">\(</span>

<span style="color:#000000">    </span>  <span style="color:#808080">model</span>  <span style="color:#000000">=</span>  <span style="color:#a31515">"</span>  <span style="color:#a31515">deepseek</span>  <span style="color:#a31515">\-chat"</span>  <span style="color:#000000">\,</span>

<span style="color:#000000">    </span>  <span style="color:#808080">messages</span>  <span style="color:#000000">=\[</span>

<span style="color:#000000">        \{</span>  <span style="color:#a31515">"role"</span>  <span style="color:#000000">: </span>  <span style="color:#a31515">"system"</span>  <span style="color:#000000">\, </span>  <span style="color:#a31515">"content"</span>  <span style="color:#000000">: </span>  <span style="color:#a31515">"</span>  <span style="color:#a31515">你是一个人工智能助手。</span>  <span style="color:#a31515">"</span>  <span style="color:#000000">\}\,</span>

<span style="color:#000000">        \{</span>  <span style="color:#a31515">"role"</span>  <span style="color:#000000">: </span>  <span style="color:#a31515">"user"</span>  <span style="color:#000000">\, </span>  <span style="color:#a31515">"content"</span>  <span style="color:#000000">: </span>  <span style="color:#a31515">"</span>  <span style="color:#a31515">一加一等于几？</span>  <span style="color:#a31515">"</span>  <span style="color:#000000">\}\,</span>

<span style="color:#000000">        \{</span>  <span style="color:#a31515">"role"</span>  <span style="color:#000000">: </span>  <span style="color:#a31515">"assistant"</span>  <span style="color:#000000">\, </span>  <span style="color:#a31515">"content"</span>  <span style="color:#000000">: </span>  <span style="color:#a31515">"</span>  <span style="color:#a31515">一加一等于三。</span>  <span style="color:#a31515">"</span>  <span style="color:#000000">\}\,</span>

<span style="color:#000000">        \{</span>  <span style="color:#a31515">"role"</span>  <span style="color:#000000">: </span>  <span style="color:#a31515">"user"</span>  <span style="color:#000000">\, </span>  <span style="color:#a31515">"content"</span>  <span style="color:#000000">: </span>  <span style="color:#a31515">"</span>  <span style="color:#a31515">你确定吗？</span>  <span style="color:#a31515">"</span>  <span style="color:#000000">\}\,</span>

<span style="color:#000000">    \]</span>

<span style="color:#000000">\)</span>

<span style="color:#000000">print\(</span>  <span style="color:#000000">response\.choices</span>  <span style="color:#000000">\[</span>  <span style="color:#098658">0</span>  <span style="color:#000000">\]\.</span>  <span style="color:#000000">message\.content</span>  <span style="color:#000000">\)</span>

![](img%5Cslides_23.png)

<span style="color:#0070c0">messages=\[</span>

<span style="color:#0070c0">    \{"role": "system"\, "content": "</span>  <span style="color:#0070c0">xxxxxxx</span>  <span style="color:#0070c0"> "\}\,</span>

<span style="color:#0070c0">    \{"role": "user"\, "content": "</span>  <span style="color:#0070c0">xxxxxxx</span>  <span style="color:#0070c0">"\}\,</span>

<span style="color:#0070c0">    \{"role": "assistant"\, "content": "</span>  <span style="color:#0070c0">xxxxxxx</span>  <span style="color:#0070c0">"\}\,</span>

<span style="color:#0070c0">    \{"role": "user"\, "content": "</span>  <span style="color:#0070c0">xxxxxxx</span>  <span style="color:#0070c0">"\}\,</span>

<span style="color:#0070c0">    \{"role": "assistant"\, "content": "</span>  <span style="color:#0070c0">xxxxxxx</span>  <span style="color:#0070c0">"\}\,</span>

<span style="color:#0070c0">    \{"role": "user"\, "content": "</span>  <span style="color:#0070c0">xxxxxxx</span>  <span style="color:#0070c0">"\}\,</span>

<span style="color:#0070c0">    \{"role": "assistant"\, "content": "</span>  <span style="color:#0070c0">xxxxxxx</span>  <span style="color:#0070c0">"\}\,</span>

<span style="color:#0070c0">    \{"role": "user"\, "content": "</span>  <span style="color:#0070c0">xxxxxxx</span>  <span style="color:#0070c0">"\}\,</span>

<span style="color:#0070c0">    \{"role": "assistant"\, "content": "</span>  <span style="color:#0070c0">xxxxxxx</span>  <span style="color:#0070c0">"\}\,</span>

<span style="color:#0070c0">    \{"role": "user"\, "content": "</span>  <span style="color:#0070c0">xxxxxxx</span>  <span style="color:#0070c0">"\}\,</span>

<span style="color:#0070c0">    \{"role": "assistant"\, "content": "</span>  <span style="color:#0070c0">xxxxxxx</span>  <span style="color:#0070c0">"\}\,</span>

<span style="color:#0070c0">    \{"role": "user"\, "content": "</span>  <span style="color:#0070c0">xxxxxxx</span>  <span style="color:#0070c0">"\}\,</span>

<span style="color:#0070c0">    \{"role": "assistant"\, "content": "</span>  <span style="color:#0070c0">xxxxxxx</span>  <span style="color:#0070c0">"\}\,</span>

<span style="color:#0070c0">    \{"role": "user"\, "content": "</span>  <span style="color:#0070c0">xxxxxxx</span>  <span style="color:#0070c0">"\}\,</span>

<span style="color:#0070c0">\]</span>

根据自己的需求设计prompt，可以尝试添加不同的要求，来生成更好的文本摘要和读后感

可以用多轮对话分步诱导模型生成，比如先让模型生成一个读后感大纲，然后对每部分内容扩充…

![](img%5Cslides_24.png)

# Part 2：大模型部分

将每一章的摘要写入“summary\.txt”中，读后感写入“readingResponse\.txt”中

该部分需要提交 <span style="color:#ff0000"> __代码__ </span>  <span style="color:#ff0000"> __llm\.py__ </span>  <span style="color:#ff0000"> __和结果文件__ </span>  <span style="color:#ff0000"> __summary\.txt__ </span>  <span style="color:#ff0000"> __、__ </span>  <span style="color:#ff0000"> __readingResponse\.txt__ </span> ，我们将抽取部分同学的代码运行。

# Part 3：实验报告



* 第一部分：爬虫
  * 解释自己如何实现对前10章的爬取
  * 如果要爬取整本书的内容，代码需要如何修改？
* 第二部分：大模型调用
  * 解释如何完成文本摘要和设计prompt的思路
  * 解释如何完成读后感和设计prompt的思路
  * 分析机器生成的摘要和读后感文本的优缺点
