class Draft:
    def comment(self):
        """
        # 导出用例数据
        label_dir = tk.Label(
            window,
            text="Test Case Save directory: "
        )
        label_dir.grid(column=0, row=2)
        txt_dir = tk.Entry(window, width=30)
        # txt.pack(side = RIGHT)
        txt_dir.grid(column=1, row=2, sticky="W")
        text = tk.Text(window)

        text.insert(tk.END, "这是一个文本控件")
        text.grid(row=0, column=0)

        scrollbar = tk.Scrollbar(window)
        scrollbar.grid(row=0, column=1, sticky='ns')

        text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text.yview)


        label_text = tk.Text(
            window,
            # text="具体用例",
            # bg="blue",
            width=60,
            height=40
        )

        label_text.grid(
            column=1,
            row=4,
            sticky=tk.S + tk.W + tk.E + tk.N
        )
        # 使用滚动条
        scroll_bar_y = tk.Scrollbar(orient=tk.HORIZONTAL, command=label_text.yview)
        label_text.config(
            yscrollcommand=scroll_bar_y.set
        )
        scroll_bar_y.grid(
            row=4,
            column=1,
            sticky=tk.S + tk.W + tk.E + tk.N
        )
        # scroll_bar_x = tk.Scrollbar(window, orient=tk.VERTICAL)
        # scroll_bar_y.pack(side=tk.RIGHT, fill=tk.Y)
        # scroll_bar_x.pack(side=tk.BOTTOM, fill=tk.X)
        """
