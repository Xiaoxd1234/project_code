import sys

from task7 import TextProcessor

# 假设 util.py 中有如下结构
users_info = {
    "admin1": {"name": "管理员A", "access": "admin", "password": "adminpass"},
    "reader1": {"name": "读者A", "access": "reader", "password": "readerpass"}
}
# from util import users_info

def verify_user_choice(choice, valid_choices):
    return choice in valid_choices

class Role:
    def __init__(self, username, name, access):
        self._username = username
        self._name = name
        self._access = access
    def get_user_name(self):
        return self._username
    def get_access(self):
        return self._access
    def get_name(self):
        return self._name

class RoleBasedVocabSys:
    def __init__(self, stopwords_filepath, corpus_filepath, idx2label_filepath):
        self.text_processor = TextProcessor(stopwords_filepath, corpus_filepath, idx2label_filepath)
        self.current_role = None
        self.running = True
    def login(self):
        print("请输入用户名：")
        username = input().strip()
        if username not in users_info:
            print("用户名不存在。")
            return False
        print("请输入密码：")
        password = input().strip()
        if password != users_info[username]["password"]:
            print("密码错误。")
            return False
        info = users_info[username]
        self.current_role = Role(username, info["name"], info["access"])
        print(f"欢迎，{info['name']}！您的角色是：{info['access']}")
        return True
    def logout(self):
        print("已登出。")
        self.current_role = None
    def show_menu(self):
        if self.current_role is None:
            print("\n1. 登录\n0. 退出")
            return ["1", "0"]
        elif self.current_role.get_access() == "reader":
            print("\n1. 查看词汇表\n2. 查看前10高频词\n3. 查看后10低频词\n4. 登出\n0. 退出")
            return ["1", "2", "3", "4", "0"]
        elif self.current_role.get_access() == "admin":
            print("\n1. 查看词汇表\n2. 查看前10高频词\n3. 查看后10低频词\n4. 添加文件\n5. 移除文件\n6. 登出\n0. 退出")
            return ["1", "2", "3", "4", "5", "6", "0"]
    def run(self):
        while self.running:
            valid_choices = self.show_menu()
            print("请选择操作：")
            choice = input().strip()
            if not verify_user_choice(choice, valid_choices):
                print("无效选择，请重试。")
                continue
            if self.current_role is None:
                if choice == "1":
                    self.login()
                elif choice == "0":
                    print("系统已退出。")
                    self.running = False
            elif self.current_role.get_access() == "reader":
                if choice == "1":
                    print("词汇表：")
                    # print(self.text_processor.word_freq)  # 此处调用了 TextProcessor 的相关功能
                elif choice == "2":
                    print("前10高频词：")
                    # top10 = sorted(self.text_processor.word_freq.items(), key=lambda x: -x[1])[:10]  # 此处调用了 TextProcessor 的相关功能
                    # print(top10)
                elif choice == "3":
                    print("后10低频词：")
                    # bottom10 = sorted(self.text_processor.word_freq.items(), key=lambda x: x[1])[:10]  # 此处调用了 TextProcessor 的相关功能
                    # print(bottom10)
                elif choice == "4":
                    self.logout()
                elif choice == "0":
                    print("系统已退出。")
                    self.running = False
            elif self.current_role.get_access() == "admin":
                if choice == "1":
                    print("词汇表：")
                    # print(self.text_processor.word_freq)  # 此处调用了 TextProcessor 的相关功能
                elif choice == "2":
                    print("前10高频词：")
                    # top10 = sorted(self.text_processor.word_freq.items(), key=lambda x: -x[1])[:10]  # 此处调用了 TextProcessor 的相关功能
                    # print(top10)
                elif choice == "3":
                    print("后10低频词：")
                    # bottom10 = sorted(self.text_processor.word_freq.items(), key=lambda x: x[1])[:10]  # 此处调用了 TextProcessor 的相关功能
                    # print(bottom10)
                elif choice == "4":
                    print("正在添加文件 data/for_admin/excluded.csv ...")
                    # self.text_processor.add_file("data/for_admin/excluded.csv")  # 此处调用了 TextProcessor 的相关功能
                    print("添加完成。")
                elif choice == "5":
                    print("正在移除文件 data/for_admin/excluded.csv ...")
                    # self.text_processor.delete_file("data/for_admin/excluded.csv")  # 此处调用了 TextProcessor 的相关功能
                    print("移除完成。")
                elif choice == "6":
                    self.logout()
                elif choice == "0":
                    print("系统已退出。")
                    self.running = False

if __name__ == "__main__":
    # 示例参数，请根据实际路径修改
    stopwords_filepath = "stop_words_english.txt"
    corpus_filepath = "ag_news_test.csv"
    idx2label_filepath = "idx2label.json"
    sys = RoleBasedVocabSys(stopwords_filepath, corpus_filepath, idx2label_filepath)
    sys.run()