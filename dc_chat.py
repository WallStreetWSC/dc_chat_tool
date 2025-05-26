import requests
import json
import random
import time
import pyautogui
import pyperclip

authorization = "authorization" #换成自己的
channel_list = ["频道ID"]  #可以多个频道
# # X：https://x.com/WallStreet_WSC（感谢支持，多多点赞关注）

ascii_banner = r'''
                                                                                                                                                         
                                                                                                                                                         
           .---.             ,--,    ,--,     .--.--.       ___                                   ___                       .---.  .--.--.     ,----..   
          /. ./|           ,--.'|  ,--.'|    /  /    '.   ,--.'|_                               ,--.'|_                    /. ./| /  /    '.  /   /   \  
      .--'.  ' ;           |  | :  |  | :   |  :  /`. /   |  | :,'   __  ,-.                    |  | :,'               .--'.  ' ;|  :  /`. / |   :     : 
     /__./ \ : |           :  : '  :  : '   ;  |  |--`    :  : ' : ,' ,'/ /|                    :  : ' :              /__./ \ : |;  |  |--`  .   |  ;. / 
 .--'.  '   \' .  ,--.--.  |  ' |  |  ' |   |  :  ;_    .;__,'  /  '  | |' | ,---.     ,---.  .;__,'  /           .--'.  '   \' .|  :  ;_    .   ; /--`  
/___/ \ |    ' ' /       \ '  | |  '  | |    \  \    `. |  |   |   |  |   ,'/     \   /     \ |  |   |           /___/ \ |    ' ' \  \    `. ;   | ;     
;   \  \;      :.--.  .-. ||  | :  |  | :     `----.   \:__,'| :   '  :  / /    /  | /    /  |:__,'| :           ;   \  \;      :  `----.   \|   : |     
 \   ;  `      | \__\/: . .'  : |__'  : |__   __ \  \  |  '  : |__ |  | ' .    ' / |.    ' / |  '  : |__          \   ;  `      |  __ \  \  |.   | '___  
  .   \    .\  ; ," .--.; ||  | '.'|  | '.'| /  /`--'  /  |  | '.'|;  : | '   ;   /|'   ;   /|  |  | '.'|       ___.   \    .\  ; /  /`--'  /'   ; : .'| 
   \   \   ' \ |/  /  ,.  |;  :    ;  :    ;'--'.     /   ;  :    ;|  , ; '   |  / |'   |  / |  ;  :    ;    .'  .`|\   \   ' \ |'--'.     / '   | '/  : 
    :   '  |--";  :   .'   \  ,   /|  ,   /   `--'---'    |  ,   /  ---'  |   :    ||   :    |  |  ,   /  .'  .'   : :   '  |--"   `--'---'  |   :    /  
     \   \ ;   |  ,     .-./---`-'  ---`-'                 ---`-'          \   \  /  \   \  /    ---`-',---, '   .'   \   \ ;                 \   \ .'   
      '---"     `--`---'                                                    `----'    `----'           ;   |  .'       '---"                   `---`     
'''

# 获取频道内容
def get_context(auth, chanel_id):
    headers = {
        "Authorization": auth,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    url = f"https://discord.com/api/v9/channels/{chanel_id}/messages?limit=100"
    res = requests.get(url, headers=headers)
    result = res.json()
    result_list = []
    for context in result:
        if all(k not in context['content'] for k in ['<', '@', 'http', '?']):
            result_list.append(context['content'])
    return random.choice(result_list) if result_list else None

# GUI模拟输入消息
def simulate_typing_message(message):
    pyautogui.click()  # 点击输入框（请事先手动聚焦在Discord输入框）
    time.sleep(random.uniform(0.3, 0.6))LFG，Spark no1

    pyperclip.copy(message)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(random.uniform(0.2, 0.5))
    pyautogui.press('enter')

# 主控制流程
def auto_send(channels, auth, sleep_time=(120, 121)): #这里间隔时间控制在2分钟
    print("准备发送，请10秒内切到 Discord 输入框（并聚焦好）...")
    time.sleep(10)
    count = 0
    while True:
        ch_id = random.choice(channels)
        msg = get_context(auth, ch_id)
        if msg:
            simulate_typing_message(msg)
            count += 1
            print(f"[{count}] 发送成功：{msg}")
        else:
            print("无有效内容，跳过...")
        time.sleep(random.randint(*sleep_time))  # 控制间隔

# 运行
if __name__ == "__main__":
    print(ascii_banner)
    print("✨ 华尔街之狼")
    print("💬 X:https://x.com/WallStreet_WSC")
    print("💬 可以根据聊天慢速模式自行调节sleep时间")
    print("💬 功能简单单一，只能用在大量有机器人的频道，可以自行迭代AI功能")
    print("🚀 脚本运行中，请保持窗口开启...\n")
    auto_send(channel_list, authorization)
