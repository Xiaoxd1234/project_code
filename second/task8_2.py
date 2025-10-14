from typing import Optional
import os
from task7_2 import TextProcessor

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
    def __init__(self, users_info, 
                 stopwords_filepath="data/stop_words_english.txt",
                 corpus_filepath="data/ag_news_test.csv",
                 idx2label_filepath="data/idx2label.json"):
        self.users_info = users_info
        self.current_user: Optional[Role] = None
        self.text_processor = TextProcessor(stopwords_filepath, corpus_filepath, idx2label_filepath)

    def start(self):
        # 开场两行（与示例一致）
        print("Welcome to the Mark system v0.0!")
        print("Please Login:")

        while True:
            if self.current_user is None:
                # 未登录时：只打印菜单“1.Exit\n2.Login”（示例里就是这样）
                print(self.generate_menu())
                # 未登录阶段，示例里没有 “Enter your choice: ” 这一行
                choice = self.get_user_choice(show_enter_prompt=False)

                if not self.verify_user_choice(choice):
                    continue

                if choice == "1":
                    break
                elif choice == "2":
                    ok = self.login()
                    # 登录成功后，立刻打印“欢迎姓名”，然后打印“Please choice one option below:”+管理员/读者菜单，再给“Enter your choice: ”
                    if ok:
                        print(f"Welcome {self.current_user.get_name()}")
                        print("Please choice one option below:")
                        print(self.generate_menu())
                        choice = self.get_user_choice(show_enter_prompt=True)
                        if not self.verify_user_choice(choice):
                            continue
                        # 下面直接走一次分支（避免需要再回到循环顶部才显示一次）
                        if self.current_user.get_access() == "reader":
                            if choice == "1":
                                break
                            elif choice == "2":
                                self.login()
                            elif choice == "3":
                                top10 = sorted(self.text_processor.word_freq.items(), key=lambda x: -x[1])[:10]
                            elif choice == "4":
                                bottom10 = sorted(self.text_processor.word_freq.items(), key=lambda x: x[1])[:10]
                        elif self.current_user.get_access() == "admin":
                            if choice == "1":
                                break
                            elif choice == "2":
                                self.login()
                            elif choice == "3":
                                top10 = sorted(self.text_processor.word_freq.items(), key=lambda x: -x[1])[:10]
                            elif choice == "4":
                                bottom10 = sorted(self.text_processor.word_freq.items(), key=lambda x: x[1])[:10]
                            elif choice == "5":
                                file_path = "data/add.csv"
                                self.text_processor.add_file(file_path)
                            elif choice == "6":
                                file_path = "data/delete.csv"
                                self.text_processor.delete_file(file_path)
                    # 登录失败则回到循环顶部，继续显示未登录菜单
                    continue

            else:
                # 已登录状态：先打印“Please choice one option below:”，再打印对应菜单，再提示“Enter your choice: ”
                print("Please choice one option below:")
                print(self.generate_menu())
                choice = self.get_user_choice(show_enter_prompt=True)

                if not self.verify_user_choice(choice):
                    continue

                if self.current_user.get_access() == "reader":
                    if choice == "1":
                        break
                    elif choice == "2":
                        self.login()
                    elif choice == "3":
                        top10 = sorted(self.text_processor.word_freq.items(), key=lambda x: -x[1])[:10]
                    elif choice == "4":
                        bottom10 = sorted(self.text_processor.word_freq.items(), key=lambda x: x[1])[:10]

                elif self.current_user.get_access() == "admin":
                    if choice == "1":
                        break
                    elif choice == "2":
                        self.login()
                    elif choice == "3":
                        top10 = sorted(self.text_processor.word_freq.items(), key=lambda x: -x[1])[:10]
                    elif choice == "4":
                        bottom10 = sorted(self.text_processor.word_freq.items(), key=lambda x: x[1])[:10]
                    elif choice == "5":
                        file_path = "data/add.csv"
                        self.text_processor.add_file(file_path)
                    elif choice == "6":
                        file_path = "data/delete.csv"
                        self.text_processor.delete_file(file_path)

    def generate_menu(self) -> str:
        if self.current_user is None:
            # 未登录菜单：与示例一致（无前导换行）
            return "1.Exit\n2.Login"

        elif self.current_user.get_access() == "reader":
            # 与你原示例风格一致（不加前导换行）
            return "1.Exit\n2.Logout/Re-Login\n3.Show top 10 frequency vocabularies\n4.Show last 10 frequency vocabularies"

        elif self.current_user.get_access() == "admin":
            return "1.Exit\n2.Logout/Re-Login\n3.Show top 10 frequency vocabularies\n4.Show last 10 frequency vocabularies\n5.Updating Vobulary for adding\n6.Updating Vobulary for excluding"

    def verify_user_choice(self, user_choice) -> bool:
        if self.current_user is None:
            return user_choice in ["1", "2"]
        elif self.current_user.get_access() == "reader":
            return user_choice in ["1", "2", "3", "4"]
        elif self.current_user.get_access() == "admin":
            return user_choice in ["1", "2", "3", "4", "5", "6"]

    def get_user_choice(self, show_enter_prompt: bool = True):
        if show_enter_prompt:
            print("Enter your choice: ", end="")
        return input().strip()

    def login(self):
        # 精确到冒号与后面空格
        print("Please key your account name: ", end="")
        typed = input().strip()

        # 支持用户名或姓名登录（大小写不敏感）
        username = None
        for k in self.users_info.keys():
            if typed.lower() == k.lower():
                username = k
                break
        if username is None:
            for k, info in self.users_info.items():
                if typed.lower() == info.get("name", "").lower():
                    username = k
                    break
        if username is None:
            return False

        print("Please key your password: ", end="")
        password = input().strip()
        if password != self.users_info[username]["password"]:
            return False

        info = self.users_info[username]
        self.current_user = Role(username, info["role"], info["name"])

        # 注意：示例里登录成功后先打印 Welcome 姓名，菜单与提示在外层处理
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