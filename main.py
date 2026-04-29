
import time

from openai import OpenAI
import os

from wxauto4 import WeChat

class WeChatBot:
    def __init__(self):
        self.client = OpenAI(api_key= os.getenv("DeepSeek"), base_url="https://api.deepseek.com"  )
        self.wx = WeChat()
        print(dir(self.wx))

    def __ask(self, question):
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            stream=False
        )
        return response.choices[0].message.content.strip()
    


    def run(self):
        print("Running WeChatBot...")
        target = "文件传输助手"
        # print(self.__ask("python 和 c++ 哪个更好？"))
        target = "文件传输助手"
        self.wx.ChatWith(target)
        # 查看当前窗口信息
        chatinfo = self.wx.ChatInfo()
        print(f"当前窗口信息：{chatinfo}")

        # 发送消息
        if chatinfo.get('chat_name') == target:  # 先判断是否为要发送的人
            self.wx.SendMsg("你好")

        # 获取当前聊天窗口消息
        msgs = self.wx.GetAllMessage()

        # for msg in msgs:
        #     print(msg.raw)

        sessions = self.wx.GetSession()
        for session in sessions:
            print(session.info)


def main():
    print("Hello from wechatbot!")
    bot = WeChatBot()
    bot.run()


if __name__ == "__main__":
    main()
