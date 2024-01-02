import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import sys

class Alarm:
    def __init__(self, name="", hour="", minute="", message="", status="Work"):
        self.name = name
        self.hour = hour
        self.minute = minute
        self.message = message
        self.status = status
    def is_working(self):
        return self.status == "Work"
class AlarmApp:
    def __init__(self, points, root):
        self.root = root
        self.points = points
        self.alarms = []
        self.alarm_id = 1
        self.double_click = False
        self.trigger_count = 0  # 新增一個屬性來記錄觸發次數

        self.current_time_label = tk.Label(root, text="Current Time: ", bg=universal_background_color)
        self.current_time_label.pack()

        self.update_current_time()

        self.buttons_frame = tk.Frame(root, bg=universal_background_color, padx=10, pady=10)  # 藍色框起來的按鈕區域
        self.buttons_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.buttons_frame.pack_propagate(0)  # 禁止自動調整大小


        self.add_button = tk.Button(self.buttons_frame, text="Add Alarm", command=self.add_alarm, bg=universal_button_background_color)
        self.add_button.pack()

        
        
        self.delete_button = tk.Button(self.buttons_frame, text="Delete Alarm", command=self.delete_alarm, bg=universal_button_background_color)
        self.delete_button.pack()
        
        self.add_Sleep_alarm_button = tk.Button(self.buttons_frame, text="Add Sleep Alarm", command=self.add_sleep_alarm, bg=universal_button_background_color)
        self.add_Sleep_alarm_button.pack()
        
        self.add_Wakeup_alarm_button = tk.Button(self.buttons_frame, text="Add Wakeup Alarm", command=self.add_Wakeup_alarm, bg=universal_button_background_color)
        self.add_Wakeup_alarm_button.pack()


        self.trigger_count_label = tk.Label(self.buttons_frame, text="Trigger Count: 0", bg=universal_background_color)#計數器
        self.trigger_count_label.pack()

        self.trigger_label = tk.Label(self.buttons_frame, text="your performance: none", font=("Arial", 12), bg=universal_background_color)#計數器回應
        self.trigger_label.pack()
        
        self.alarms_frame = tk.Frame(root, bg=universal_background_color, padx=10, pady=10)  # 紅色框起來的顯示鬧鐘區域
        self.alarms_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.alarms_frame.pack_propagate(0)

        self.alarms_title_label = tk.Label(self.alarms_frame, bg=universal_background_color, text="clock list", font=("Arial", 12, "bold"))
        self.alarms_title_label.pack()

        self.alarms_listbox = tk.Listbox(self.alarms_frame)
        self.alarms_listbox.pack(fill=tk.BOTH, expand=True)

        self.alarms_listbox.bind("<ButtonRelease-1>", self.on_single_click)
        self.alarms_listbox.bind("<Double-Button-1>", self.on_double_click)

        self.selected_alarm_info_label = tk.Label(self.alarms_frame, bg=universal_button_background_color)  # 用來顯示所選擇鬧鐘的時間和留言
        self.selected_alarm_info_label.pack(fill=tk.BOTH, expand=True)

    def add_alarm(self):
        new_alarm = Alarm(name=f"ALERM{self.alarm_id}")
        self.alarm_id += 1
        self.alarms.append(new_alarm)
        self.update_alarm_list()

    def delete_alarm(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Alarm")
        delete_window.configure(bg=universal_background_color)

        delete_label = tk.Label(delete_window, text="Select alarm to delete:", bg=universal_background_color)
        delete_label.pack()

        alarms_listbox = tk.Listbox(delete_window)
        for alarm in self.alarms:
            alarms_listbox.insert(tk.END, alarm.name)
        alarms_listbox.pack()

        confirm_button = tk.Button(delete_window, text="Confirm", bg=universal_background_color, command=lambda: self.confirm_delete(alarms_listbox.get(tk.ACTIVE), delete_window))
        confirm_button.pack()

    def confirm_delete(self, selected_alarm_name, delete_window):
        for alarm in self.alarms:
            if alarm.name == selected_alarm_name:
                self.alarms.remove(alarm)
                break
        
        self.update_alarm_list()
        delete_window.destroy()
        self.selected_alarm_info_label.config(text="")  # 清空紅色區域下方的資訊

    def update_alarm_list(self):
        self.alarms_listbox.delete(0, tk.END)
        for idx, alarm in enumerate(self.alarms):
            self.alarms_listbox.insert(tk.END, f"{alarm.name} - Hour: {alarm.hour}, Minute: {alarm.minute}, Message: {alarm.message},status: {alarm.status}")

    def on_single_click(self, event):
        self.root.after(300, self.check_double_click)  # 檢查雙擊事件
        self.single_click_action(event)

    def check_double_click(self):
        if not self.double_click:
            # 如果不是雙擊，執行單擊操作
            self.single_click_action(None)

    def single_click_action(self, event):
        selected_idx = self.alarms_listbox.curselection()
        if selected_idx:
            alarm_idx = selected_idx[0]
            selected_alarm = self.alarms[alarm_idx]
            self.update_selected_alarm_frame(selected_alarm)

    def on_double_click(self, event):
        self.double_click = True
        selected_idx = self.alarms_listbox.curselection()
        if selected_idx:
            alarm_idx = selected_idx[0]
            selected_alarm = self.alarms[alarm_idx]
            self.view_alarm(selected_alarm, alarm_idx)

    def view_alarm(self, selected_alarm, alarm_idx):
        view_alarm_window = tk.Toplevel(self.root, bg=universal_background_color)
        view_alarm_window.title(f"View Alarm {selected_alarm.name}")

        name_label = tk.Label(view_alarm_window, text="Name: ", bg=universal_background_color)
        name_label.pack()

        name_var = tk.StringVar(value=selected_alarm.name)
        name_entry = tk.Entry(view_alarm_window, textvariable=name_var)
        name_entry.pack()

        hour_label = tk.Label(view_alarm_window, text="Select hour: ", bg=universal_background_color)
        hour_label.pack()

        hours = [str(h).zfill(2) for h in range(24)]
        hour_var = tk.StringVar(view_alarm_window, value=selected_alarm.hour)
        hour_dropdown = tk.OptionMenu(view_alarm_window, hour_var, *hours)
        hour_dropdown.pack()

        minute_label = tk.Label(view_alarm_window, text="Select minute: ", bg=universal_background_color)
        minute_label.pack()

        minutes = [str(m).zfill(2) for m in range(60)]
        minute_var = tk.StringVar(view_alarm_window, value=selected_alarm.minute)
        minute_dropdown = tk.OptionMenu(view_alarm_window, minute_var, *minutes)
        minute_dropdown.pack()

        message_label = tk.Label(view_alarm_window, text="Enter message: ", bg=universal_background_color)
        message_label.pack()

        message_var = tk.StringVar(value=selected_alarm.message)
        message_entry = tk.Entry(view_alarm_window, textvariable=message_var)
        message_entry.pack()
        status_label = tk.Label(view_alarm_window, text="Select status: ", bg=universal_background_color)
        status_label.pack()

        status_options = ["Work", "Rest"]  # 選項：工作狀態和休息狀態
        status_var = tk.StringVar(view_alarm_window, value=selected_alarm.status)
        status_dropdown = tk.OptionMenu(view_alarm_window, status_var, *status_options)
        status_dropdown.pack()

        #confirm_button = confirm_button = tk.Button(view_alarm_window, text="Confirm", command=lambda window=view_alarm_window: self.confirm_alarm(alarm_idx, name_var.get(), hour_var.get(), minute_var.get(), message_var.get(), status_var.get()))
        confirm_button = tk.Button(view_alarm_window, text="Confirm", command=lambda window=view_alarm_window: self.confirm_alarm(alarm_idx, name_var.get(), hour_var.get(), minute_var.get(), message_var.get(), status_var.get(), window))
        confirm_button.pack()

    def confirm_alarm(self, idx, new_name, new_hour, new_minute, new_message, new_status, view_alarm_window):
        self.alarms[idx].name = new_name
        self.alarms[idx].hour = new_hour
        self.alarms[idx].minute = new_minute
        self.alarms[idx].message = new_message
        self.alarms[idx].status = new_status
        self.update_alarm_list()
        view_alarm_window.destroy()  # 確保這一行註解掉，否則會出現相同錯誤
        self.update_selected_alarm_frame(self.alarms[idx])

    def update_selected_alarm_frame(self, selected_alarm):
        # 更新所選擇鬧鐘的時間和留言
        self.selected_alarm_info_label.config(text=f"Selected Alarm Info:\nName: {selected_alarm.name}, Hour: {selected_alarm.hour}, Minute: {selected_alarm.minute}, Message: {selected_alarm.message},status: {selected_alarm.status}")

    def check_alarm(self):
        current_time = datetime.now().strftime("%H:%M")
        for alarm in self.alarms:
            alarm_time = f"{alarm.hour.zfill(2)}:{alarm.minute.zfill(2)}"
            if current_time == alarm_time and alarm.is_working():
                confirm = messagebox.askquestion("Alarm Alert", f"Alarm triggered for: {alarm.name}\nMessage: {alarm.message}\nSet to Rest?")
                if confirm == 'yes':
                    alarm.status = "Rest"
                    self.trigger()
                    self.update_alarm_list()  # 更新显示区域
                    self.selected_alarm_info_label.config(text="")  # 清空红色区域下方的信息
                    self.trigger_count_label.config(text=f"Trigger Count: {self.trigger_count}")  # 更新觸發次數的標籤
                #    return  # 停止进一步处理，如果确认了鬧鐘

    def update_current_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.current_time_label.config(text=f"Current Time: {current_time}")
        self.check_alarm()  # 檢查是否有鬧鐘觸發
        self.root.after(1000, self.update_current_time)  # 每秒更新一次時間
    
    def trigger(self):
        self.trigger_count += 1  # 每次触发鬧鐘时增加触发次数
        trigger_text = self.get_trigger_text()
        self.trigger_label.config(text=f"your performance: {trigger_text}")
    
    def get_trigger_text(self):
        # 根据触发次数返回不同的文本
        if self.trigger_count == 0:
            self.points += 0
            return "none"
        if self.trigger_count == 1:
            self.points += 10
            return "good"
        elif self.trigger_count == 2:
            self.points += 20
            return "great"
        elif self.trigger_count >= 3:
            self.points += 30
            return "Perfect"
    
    def add_sleep_alarm(self):
        # 添加預設鬧鐘的內容
        default_alarm = Alarm(name="SleepAlerm", hour="22", minute="00", message="Sleep!", status="Work")
        self.alarms.append(default_alarm)
        self.update_alarm_list()

    def add_Wakeup_alarm(self):
        default_alarm = Alarm(name="WakeupAlerm", hour="08", minute="00", message="Wakeup!", status="Work")
        self.alarms.append(default_alarm)
        self.update_alarm_list()

    def open_alarm_interface(content):
        root.title("Alarm Application")
        root.geometry("600x400")

        app = AlarmApp(root)
        # 以下代碼確保紅色和藍色區域會隨著窗口的縮放而改變大小
        root.pack_propagate(False)
        app.buttons_frame.pack_propagate(False)
        app.alarms_frame.pack_propagate(False)

        root.mainloop()

if __name__ == "__main__":

    # 打印传递给脚本的参数
    if len(sys.argv) > 1:
        points = sys.argv[1]
        universal_background_color = sys.argv[2]
        universal_button_background_color = sys.argv[3]
        print(points)
    else:
        print("没有传递参数给脚本")

    root = tk.Tk()
    root.configure(bg=universal_background_color)
    root.title("Alarm Application")
    root.geometry("600x400")

    app = AlarmApp(int(points), root)
    # 以下代碼確保紅色和藍色區域會隨著窗口的縮放而改變大小
    root.pack_propagate(False)
    app.buttons_frame.pack_propagate(False)
    app.alarms_frame.pack_propagate(False)

    root.mainloop()
    print(app.trigger_count)
    sys.exit(app.points)