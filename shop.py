import tkinter as tk
from tkinter import messagebox
import sys

class ExchangeShop:
    def __init__(self, points, root):
        self.root = root
        self.root.title("兌換商店")

        # 初始化點數
        self.points = points

        # 建立顯示點數的標籤
        self.points_label = tk.Label(root, text=f"現有點數: {self.points}", bg=universal_background_color)
        self.points_label.pack(pady=10)

        # 商品和價格資訊
        self.products = {
            "商品兌換券": 10,
            "超商禮券": 5,
            "水壺": 5,
            "電影票": 5
        }

        # 建立商品清單和兌換按鈕
        for product in self.products:
            product_info = f"{product} - {self.products[product]} 點"
            product_button = tk.Button(root, text=product_info, command=lambda p=product: self.exchange_product(p), bg=universal_button_background_color)
            product_button.pack(pady=5)

    def exchange_product(self, product_name):
        # 取得所選商品的價格
        product_price = self.products[product_name]

        # 檢查點數是否足夠
        if self.points >= product_price:
            # 扣除點數
            self.points -= product_price

            # 更新點數標籤
            self.points_label.config(text=f"現有點數: {self.points}")

            # 提示兌換成功
            messagebox.showinfo("兌換成功", f"成功兌換 {product_name}")
        else:
            messagebox.showwarning("點數不足", "您的點數不足以兌換此商品")

if __name__ == "__main__":

    # 列印傳遞給腳本的參數
    if len(sys.argv) > 1:
        points = sys.argv[1]
        universal_background_color = sys.argv[2]
        universal_button_background_color = sys.argv[3]
        print(points)
    else:
        print("沒有傳遞參數給腳本")

    # 建立主視窗
    root = tk.Tk()
    root.configure(bg=universal_background_color)
    exchange_shop = ExchangeShop(int(points), root)
    print(exchange_shop.points)

    # 設定視窗大小
    root.geometry("400x400")  # You can adjust the size as needed (width x height)

    # 運行主循環
    root.mainloop()
    print(exchange_shop.points)
    sys.exit(exchange_shop.points)