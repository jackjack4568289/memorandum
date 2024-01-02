import tkinter as tk
import json
import sys

class MemoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("備忘錄")

        # 建立表格
        self.create_table()

        # 載入已儲存的數據
        self.load_schedule()

        # 初始點數
        self.points = 0

    def save_schedule(self):
        # 儲存行程
        schedule = []
        for i, row in enumerate(self.entries):
            day_schedule = []
            for j, entry in enumerate(row):
                day_schedule.append(entry.get())
            schedule.append(day_schedule)

        # 在實際應用中，你可以將 schedule 儲存到檔案或資料庫中
        print("保存成功:")
        for i, row_schedule in enumerate(schedule):
            print(f"{self.rows[i]}: {row_schedule}")

        # 儲存到文件
        with open('schedule.json', 'w') as file:
            json.dump(schedule, file)

        # 設定為不可編輯
        self.set_editable(False)

    def update_schedule(self):
        # 更新表格内容
        for i, row_schedule in enumerate(self.saved_schedule):
            for j, entry in enumerate(self.entries[i]):
                entry.delete(0, tk.END)  # 清空原有内容
                entry.insert(0, row_schedule[j])  # 插入已儲存的內容

        # 設定為可編輯
        self.set_editable(True)

    def set_editable(self, editable):
        for row in self.entries:
            for entry in row:
                entry.config(state=tk.NORMAL if editable else tk.DISABLED)

    def load_schedule(self):
        # 嘗試從文件加載數據
        try:
            with open('schedule.json', 'r') as file:
                schedule = json.load(file)

            # 更新表格内容
            for i, row_schedule in enumerate(schedule):
                for j, entry in enumerate(self.entries[i]):
                    entry.delete(0, tk.END)  # 清空原有内容
                    entry.insert(0, row_schedule[j])  # 插入已儲存的內容

            # 設定為不可編輯
            self.set_editable(False)

        except FileNotFoundError:
            print("找不到已儲存的資料文件")

    def initialize_schedule(self):
        # 清空表格內容
        for row in self.entries:
            for entry in row:
                entry.delete(0, tk.END)

        # 儲存初始表格內容
        self.saved_schedule = [[entry.get() for entry in row] for row in self.entries]

    def create_table(self):
        # 建立表格框架
        self.table_frame = tk.Frame(self.master, bg=universal_background_color)
        self.table_frame.pack()

        # 表格數據
        self.rows = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
        cols = ["早", "中", "晚"]

        # 建立表格
        self.entries = [[None for _ in range(len(cols))] for _ in range(len(self.rows))]

        # 標題行
        for j, col in enumerate(cols):
            label = tk.Label(self.table_frame, text=col, padx=10, pady=5, font=("Helvetica", 12, "bold"), bg=universal_background_color)
            label.grid(row=0, column=j+1)

        # 表格内容
        for i, row in enumerate(self.rows):
            label = tk.Label(self.table_frame, text=row, padx=10, pady=5, font=("Helvetica", 12, "bold"), bg=universal_background_color)
            label.grid(row=i+1, column=0)

            for j, col in enumerate(cols):
                entry = tk.Entry(self.table_frame, width=15, font=("Helvetica", 12))
                entry.grid(row=i+1, column=j+1)
                self.entries[i][j] = entry

        # 新增按鈕框架
        button_frame = tk.Frame(self.master, bg=universal_background_color)
        button_frame.pack()

        # 新增儲存按鈕
        save_button = tk.Button(button_frame, text="保存", command=self.save_schedule, bg=universal_button_background_color)
        save_button.pack(side=tk.LEFT, padx=10)

        # 新增修改按鈕
        modify_button = tk.Button(button_frame, text="修改", command=self.update_schedule, bg=universal_button_background_color)
        modify_button.pack(side=tk.LEFT, padx=10)

        # 新增初始化按鈕
        initialize_button = tk.Button(button_frame, text="清空", command=self.initialize_schedule, bg=universal_button_background_color)
        initialize_button.pack(side=tk.LEFT, padx=10)

        # 儲存初始表格內容
        self.saved_schedule = [[entry.get() for entry in row] for row in self.entries]


if __name__ == "__main__":

    # 列印傳遞給腳本的參數
    if len(sys.argv) > 1:
        universal_background_color = sys.argv[1]
        universal_button_background_color = sys.argv[2]
    else:
        print("沒有傳遞參數給腳本")

    root = tk.Tk()
    root.configure(bg=universal_background_color)
    app = MemoApp(root)
    root.mainloop()
