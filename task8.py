from typing import Optional
import os
from task7 import TextProcessor

class Role:
    def __init__(self, user_name: str, access: str, name: str):
        self.user_name = user_name
        self.access = access
        self.name = name
    def get_user_name(self):
        return self.user_name
    def get_access(self):
        return self.access
    def get_name(self):
        return self.name

class RoleBasedVocabSys:
    def __init__(
        self,
        users_info,
        stopwords_filepath="data/stop_words_english.txt",
        corpus_filepath="data/ag_news_test.csv",
        idx2label_filepath="data/idx2label.json"
    ):
        self.users_info = users_info
        self.current_user: Optional[Role] = None
        self.text_processor = TextProcessor(stopwords_filepath, corpus_filepath, idx2label_filepath)
    def start(self):
        while True:
            menu = self.generate_menu()
            print(menu)
            choice = self.get_user_choice()
            if not self.verify_user_choice(choice):
                print("无效选择，请重试。")
                continue
            if self.current_user is None:
                if choice == "1":
                    self.login()
                elif choice == "0":
                    print("系统已退出。")
                    break
            elif self.current_user.get_access() == "reader":
                if choice == "1":
                    print("词汇表：", self.text_processor.word_freq)
                elif choice == "2":
                    top10 = sorted(self.text_processor.word_freq.items(), key=lambda x: -x[1])[:10]
                    print("前10高频词：", top10)
                elif choice == "3":
                    bottom10 = sorted(self.text_processor.word_freq.items(), key=lambda x: x[1])[:10]
                    print("后10低频词：", bottom10)
                elif choice == "4":
                    print("已登出。")
                    self.current_user = None
                elif choice == "0":
                    print("系统已退出。")
                    break
            elif self.current_user.get_access() == "admin":
                if choice == "1":
                    print("词汇表：", self.text_processor.word_freq)
                elif choice == "2":
                    top10 = sorted(self.text_processor.word_freq.items(), key=lambda x: -x[1])[:10]
                    print("前10高频词：", top10)
                elif choice == "3":
                    bottom10 = sorted(self.text_processor.word_freq.items(), key=lambda x: x[1])[:10]
                    print("后10低频词：", bottom10)
                elif choice == "4":
                    # 路径固定为 data/for_admin/excluded.csv
                    file_path = "data/add.csv"
                    self.text_processor.add_file(file_path)
                    print("添加完成。")
                elif choice == "5":
                    file_path = "data/add.csv"
                    self.text_processor.delete_file(file_path)
                    print("移除完成。")
                elif choice == "6":
                    print("已登出。")
                    self.current_user = None
                elif choice == "0":
                    print("系统已退出。")
                    break
    def generate_menu(self) -> str:
        if self.current_user is None:
            return "\n1. 登录\n0. 退出"
        elif self.current_user.get_access() == "reader":
            return "\n1. 查看词汇表\n2. 查看前10高频词\n3. 查看后10低频词\n4. 登出\n0. 退出"
        elif self.current_user.get_access() == "admin":
            return "\n1. 查看词汇表\n2. 查看前10高频词\n3. 查看后10低频词\n4. 添加文件\n5. 移除文件\n6. 登出\n0. 退出"
    def verify_user_choice(self, user_choice) -> bool:
        valid_choices = ["1", "0"] if self.current_user is None else (
            ["1", "2", "3", "4", "0"] if self.current_user.get_access() == "reader" else ["1", "2", "3", "4", "5", "6", "0"]
        )
        return user_choice in valid_choices
    def get_user_choice(self):
        print("请选择操作：")
        return input().strip()
    def login(self):
        print("请输入用户名：")
        username = input().strip()
        if username not in self.users_info:
            print("用户名不存在。")
            return False
        print("请输入密码：")
        password = input().strip()
        if password != self.users_info[username]["password"]:
            print("密码错误。")
            return False
        info = self.users_info[username]
        self.current_user = Role(username, info["role"], info["name"])
        print(f"欢迎，{info['name']}！您的角色是：{info['role']}")
        return True

if __name__ == "__main__":
    users_info = {
        "Jueqing": {
            "role": "reader",
            "password": "jueqing123",
            "name": "Jueqing Lu"
        },
        "Trang": {
            "role": "admin",
            "password": "trang123",
            "name": "Trang Vu"
        },
        "land": {
            "role": "admin",
            "password": "landu123",
            "name": "Lan Du"
        }
    }
    a_sys = RoleBasedVocabSys(users_info)
    a_sys.start()