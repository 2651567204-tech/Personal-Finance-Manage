import json
import os
from datetime import datetime

class FinanceManager:
    def __init__(self, filename='data.json'):
        self.filename = filename
        self.expenses = self.load_data()

    # 核心功能1：数据持久化 (加载数据)
    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    # 核心功能2：数据持久化 (保存数据)
    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    # 核心功能3：增加数据 (Create)
    def add_expense(self, category, amount, description):
        expense = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "category": category,
            "amount": float(amount),
            "description": description
        }
        self.expenses.append(expense)
        self.save_data()
        print(f"✅ 成功记录: {category} - ${amount}")

    # 核心功能4：读取与分析数据 (Read & Analysis)
    def show_summary(self):
        if not self.expenses:
            print("📭 目前没有记录。")
            return

        print("\n--- 消费报表 ---")
        total = 0
        # 使用字典来分类汇总
        category_total = {}

        for item in self.expenses:
            print(f"[{item['date']}] {item['category']}: ${item['amount']} ({item['description']})")
            total += item['amount']
            
            # 分类统计逻辑
            if item['category'] in category_total:
                category_total[item['category']] += item['amount']
            else:
                category_total[item['category']] = item['amount']

        print("-" * 30)
        print(f"💰 总支出: ${total:.2f}")
        print("📊 分类统计:")
        for cat, amt in category_total.items():
            print(f"   - {cat}: ${amt:.2f}")
        print("-" * 30)

# 简单的交互界面 (CLI)
def main():
    manager = FinanceManager()
    
    while True:
        print("\n=== 💰 个人财务管家 ===")
        print("1. 记一笔 (Add Expense)")
        print("2. 看报表 (View Summary)")
        print("3. 退出 (Exit)")
        
        choice = input("请选择 (1/2/3): ")

        if choice == '1':
            cat = input("类别 (如: 食物/交通): ")
            amt = input("金额: ")
            desc = input("备注: ")
            try:
                manager.add_expense(cat, amt, desc)
            except ValueError:
                print("❌ 错误: 金额必须是数字！")
        elif choice == '2':
            manager.show_summary()
        elif choice == '3':
            print("👋 再见！")
            break
        else:
            print("输入无效，请重试。")

if __name__ == "__main__":
    main()