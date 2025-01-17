from openai import OpenAI
import requests
from bs4 import BeautifulSoup

client = OpenAI(api_key="sk-034f691470e54faa967975a88c7e1fd1", base_url="https://api.deepseek.com")

# # Summary Part:
# summaryContent = ''
# for chapter in range(1, 11):
#     file = open(f'XYJ_Chapter{chapter}.html', 'r', encoding='utf-8')
#     text = file.read()
#     file.close()
#     soup = BeautifulSoup(text, 'html.parser')
    
#     div_text = soup.find("div", class_ = "text p_pad")
#     paragraphs = div_text.find_all('p')
#     content = ""
#     for p in paragraphs:
#         print(p.text)
#         content += p.text + '\n'
    
#     response = client.chat.completions.create(
#         model="deepseek-chat",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {
#                 "role": "user",
#                 "content": f"{content}\n这是西游记的第{chapter}章, 请你生成一段100字的概括。"
#             },
#         ],
#     )
#     print(response.choices[0].message.content)
#     summaryContent += f"第{chapter}章总结如下:\n" + response.choices[0].message.content + '\n'
    

# file = open('summary.txt', 'w', encoding='utf-8')
# file.write(summaryContent)
# file.close()

# Reading Response Part:
file = open(f'XYJ_Chapter1.html', 'r', encoding='utf-8')
text = file.read()
file.close()
soup = BeautifulSoup(text, 'html.parser')

div_text = soup.find("div", class_ = "text p_pad")
paragraphs = div_text.find_all('p')
content = ""
for p in paragraphs:
    print(p.text)
    content += p.text + '\n'
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "system",
            "content": "你是一个优秀的文学助手，擅长生成高质量的读后感。用户会给你提供一章内容，你需要通过多轮对话逐步生成读后感，从整体结构到具体内容逐步完善。"
        },
        {
            "role": "user",
            "content": f"《西游记》第一章主要内容如下：\n{content}。请帮我生成一篇读后感。"
        },
        {
            "role": "assistant",
            "content": "好的！我们可以分以下几个步骤来生成读后感：\n1. 确定读后感的整体结构（如开头、主体、结尾）。\n2. 为每个部分提供具体的内容大纲。\n3. 针对大纲扩充细节，生成完整内容。\n\n首先，请让我为您生成一个读后感的大纲。"
        },
        {
            "role": "user",
            "content": "好的，请生成读后感的大纲。"
        },
        {
            "role": "assistant",
            "content": "以下是针对《西游记》第一章的读后感大纲：\n\n**1. 开头：引入主题**\n- 简要介绍《西游记》的背景及第一章的主要内容。\n- 强调孙悟空从诞生到成为猴王的成长历程及其象征意义。\n\n**2. 主体：深入分析**\n- **（1）孙悟空形象分析**：他是一个勇敢无畏、追求自由的象征。\n- **（2）猴王成长的启示**：花果山群猴的团结与孙悟空的领导力体现。\n- **（3）对长生不老的追求**：孙悟空执着追求的精神与人类对生命意义的探索。\n\n**3. 结尾：总结与感悟**\n- 总结孙悟空形象的象征意义。\n- 从现代视角看第一章的启发，如个人成长和对理想的追求。\n\n接下来，是否需要扩展每一部分内容？"
        },
        {
            "role": "user",
            "content": "是的，请扩展每一部分内容，详细一些。"
        },
        {
            "role": "assistant",
            "content": "**1. 开头：引入主题**\n- 《西游记》是中国四大名著之一，其故事充满了奇幻、哲理和深厚的文化内涵。第一章讲述了石猴孙悟空从花果山诞生到成为猴王的过程，为整部小说奠定了基础。\n- 孙悟空的诞生充满了神秘色彩，他从花果山一块灵石中诞生，象征着生命的奇迹和自然的灵性。\n- 第一章中，孙悟空从石猴成长为猴王，不仅展现了他的个人魅力，也暗示了他未来的非凡命运。\n\n**2. 主体：深入分析**\n- **（1）孙悟空形象分析**：\n  - 孙悟空是一个勇敢无畏、智慧过人的角色。他面对水帘洞的考验毫不畏惧，展现了敢于冒险的精神。\n  - 他对自由的追求体现在领导群猴建立家园的过程中，花果山的欢乐生活象征了乌托邦式的理想。\n- **（2）猴王成长的启示**：\n  - 孙悟空能够成为猴王，不仅因为他的勇气，更因为他的领导能力和团结精神。他与群猴分享胜利的喜悦，体现了集体意识的重要性。\n  - 这一段故事告诉我们，真正的领导者需要关心他人，带领团队共同追求幸福。\n- **（3）对长生不老的追求**：\n  - 孙悟空后来追求长生不老的执着反映了人类对生命意义的探索。他对生命长度和质量的关注，与我们今天的哲学思考和科技探索有异曲同工之妙。\n\n**3. 结尾：总结与感悟**\n- 孙悟空的形象象征了勇敢、智慧和对自由的无限渴望。他从石猴到猴王的蜕变过程，揭示了成长的意义。\n- 从现代视角看，第一章让我们反思个人成长的重要性，以及对理想和自由的追求如何塑造我们的生活。\n- 孙悟空敢于挑战命运的精神，激励我们在面对人生的困境时，依然保持希望和斗志。\n\n如果需要，我可以进一步润色或改写其中的某一部分内容。"
        },
        {
            "role": "user",
            "content": "请用以上内容生成完整的读后感。"
        },
        ],
)

print(response.choices[0].message.content)
file = open("readingResponse.txt", "w", encoding="utf-8")
file.write(response.choices[0].message.content)
file.close()