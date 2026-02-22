import datetime

# 模拟从 API 获取的数据（未来你可以接入真正的 yfinance 或新闻 API）
# 这里的逻辑是基于你对非线性增长的关注
def get_market_insights():
    today = datetime.date.today().strftime("%Y-%m-%d")
    return [
        {
            "title": "AI & SEMICONDUCTORS",
            "type": "persistent",
            "color": "#3b82f6",
            "content": f"截止 {today}：半导体板块（SOXX）展现出极强的韧性。NVIDIA 领衔的算力链条在资金结构上呈现典型的‘高位换手’，非线性增长预期依然稳固。"
        },
        {
            "title": "AEROSPACE / 航天",
            "type": "emerging",
            "color": "#ec4899",
            "content": "新观察：商业航天领域小市值标的出现异动。随着发射成本进一步下探，该板块可能处于估值重构的前夜，建议关注底部放量标的。"
        }
    ]

def update_html():
    insights = get_market_insights()
    # 格式化成 JS 数组字符串
    insights_js = f"const marketInsights = {insights};"
    
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    # 替换锚点之间的内容
    start_marker = "/* START_INSIGHTS */"
    end_marker = "/* END_INSIGHTS */"
    
    start_idx = content.find(start_marker) + len(start_marker)
    end_idx = content.find(end_marker)
    
    new_content = content[:start_idx] + "\n" + insights_js + "\n" + content[end_idx:]

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_html()
