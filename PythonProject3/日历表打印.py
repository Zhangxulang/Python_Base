# 作者: 大数据 浪哥
# 2025年07月22日04时05分58秒
# 1054074422@qq.com

import datetime
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment

def generate_calendar_weeks(years=3):
    today = datetime.date.today()
    start_year = today.year
    end_year = start_year + years - 1

    start_date = datetime.date(start_year, 1, 1)
    end_date = datetime.date(end_year, 12, 31)

    current_date = start_date
    calendar_data = []

    while current_date <= end_date:
        iso_year, iso_week, iso_weekday = current_date.isocalendar()
        calendar_data.append([
            current_date.strftime('%Y-%m-%d'),    # 日期
            iso_year,                              # 所属ISO年
            iso_week,                              # 第几周
            f"第{iso_week}周",                     # 中文周数
            current_date.strftime('%A')            # 星期几（英文）
        ])
        current_date += datetime.timedelta(days=1)

    return calendar_data

def save_to_excel(data, filename='近三年日历周数.xlsx'):
    wb = Workbook()
    ws = wb.active
    ws.title = "日历周信息"

    # 表头（含中文）
    headers = ['日期', '所属年份（ISO标准）', '第几周（数字）', '中文周数', '星期（英文）']
    ws.append(headers)

    # 样式设置
    for col in ws.iter_cols(min_row=1, max_row=1, min_col=1, max_col=len(headers)):
        for cell in col:
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal='center')

    for row in data:
        ws.append(row)

    # 自动列宽
    for col in ws.columns:
        max_length = max(len(str(cell.value)) for cell in col)
        ws.column_dimensions[col[0].column_letter].width = max_length + 2

    wb.save(filename)
    print(f"✅ 已保存到 Excel 文件：{filename}")

if __name__ == '__main__':
    calendar = generate_calendar_weeks(years=3)
    save_to_excel(calendar)