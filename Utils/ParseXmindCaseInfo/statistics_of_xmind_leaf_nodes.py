# coding: UTF-8

"""
第一期：统计所有用例个数 + 列表返回未节点用例
第二期：组装用例，统计各用例各维度属性
第三期：一键转Excel用例文档
"""

import os

import requests
import sv_ttk
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import xmindparser


# from traceback


class SaveTestCaseParam(object):
    """
    保存Xmind节点解析后的个数
    """

    def __init__(self):
        self.case_count = 0
        self.case_text = []
        self.test_index = 0

    def parse_xmind_node(self, parse_node):
        """
        读取整个测试用例的根节点和对应的子节点
        :param parse_node:
        :return:
        """
        try:
            if isinstance(parse_node, dict):
                # global self.case_list
                parse_node_keys = parse_node.keys()
                if "title" in parse_node_keys:
                    if "topics" in parse_node_keys:
                        self.parse_xmind_node(parse_node["topics"])
                    elif "topic" in parse_node_keys:
                        self.parse_xmind_node(parse_node["topic"])
            elif isinstance(parse_node, list):
                for node_dict in parse_node:
                    node_dict_keys = node_dict.keys()
                    if "title" in node_dict_keys:
                        if "topics" in node_dict_keys:
                            self.parse_xmind_node(node_dict["topics"])
                        elif "topic" in node_dict_keys:
                            self.parse_xmind_node(node_dict["topic"])
                        elif "topics" not in node_dict_keys and "topic" not in node_dict_keys:
                            self.case_text.append(node_dict["title"])
                            self.case_count += 1
            elif isinstance(parse_node, str):
                self.case_count += 1
        except Exception as e:
            self.except_messagebox(str(e))

    @staticmethod
    def except_messagebox(exception_info):
        if exception_info:
            import tkinter.messagebox
            tk.messagebox.showwarning(
                title="Warning：",
                message=exception_info
            )

    def get_case_count_text(self):
        # 实例化tkinter
        window = tk.Tk()
        style = ttk.Style()
        sv_ttk.set_theme("dark")
        # style.configure("TButton", background="black", foreground="blue")
        window.title("Parse Xmind TestCase Count and Case.")
        window.geometry("650x400")

        label = tk.Label(
            window,
            text="Input Xmind Path: "
        )
        label.grid(column=0, row=1)
        txt = tk.Entry(window, width=30)
        # txt.pack(side = RIGHT)
        txt.grid(column=1, row=1)

        def clicked():
            self.case_count = 0
            self.case_text = []
            file_path = ""
            try:
                file_path = txt.get()
                file_path = file_path.strip('"')
                if not os.path.isfile(file_path):
                    self.exception_info = "File path not recognized, please re-enter."
            except Exception as e:
                self.except_messagebox("File path error：" + str(e))
            try:
                content_list = xmindparser.xmind_to_dict(file_path)
                self.parse_xmind_node(content_list)
            except Exception as e:
                self.except_messagebox("Xmind parsing error: " + str(e))

            # case_count = "测试用例数： {}".format(self.case_count)
            label_case_count_text = tk.Label(
                window,
                height=3,
                text=f"测试用例数：{self.case_count}",
            )
            label_case_count_text.grid(column=0, row=3, sticky="W")

            # case_text = "末端叶子节点用例：".format(self.case_text)
            label_case_text_info = tk.Label(
                window,
                text="末端叶子节点用例：",
            )
            label_case_text_info.grid(column=0, row=4, sticky="N")

            label_text = tk.Label(
                window,
                # text="具体用例",
                # bg="blue",
                width=90,
                height=40,
                wraplength=300,
                anchor='w',
                justify="left"
            )
            label_text.grid(column=1, row=4)

            label_case_text_info.configure()
            case_text_str = str(self.case_text).strip("[").strip("]")
            label_text.configure(text=case_text_str)

        try:
            btn = ttk.Button(window, text="Parse TestCase", command=clicked)
            btn.grid(column=0, row=2)
            # btn.pack()
            window.mainloop()
        except Exception as e:
            self.except_messagebox(f"GUI Error：{str(e)}")


if __name__ == '__main__':
    # file_path = r"C:\Users\Administrator\Desktop\店铺管理.xmind"
    test = SaveTestCaseParam()
    test.get_case_count_text()
