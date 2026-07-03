import pandas as pd

df = pd.read_excel('23本计算机科学与技术（创新实验班）【1-2】班_统计一键导出.xlsx', skiprows=[0,1])

total_students = len(df)
avg_score = df['综合成绩'].mean()
max_score = df['综合成绩'].max()
min_score = df['综合成绩'].min()
pass_count = (df['综合成绩'] >= 60).sum()
pass_rate = pass_count / total_students * 100

print(f'Total students: {total_students}')
print(f'Average score: {avg_score:.2f}')
print(f'Max score: {max_score:.2f}')
print(f'Min score: {min_score:.2f}')
print(f'Pass count: {pass_count}')
print(f'Pass rate: {pass_rate:.1f}%')

print('\n---TOP 10 Students---')
top10 = df.nlargest(10, '综合成绩')
for idx, row in top10.iterrows():
    print(f"{row['序号']}\t{row['学生姓名']}\t{row['学号/工号']}\t{row['综合成绩']:.2f}")

print('\n---All Students Data---')
students_data = []
for idx, row in df.iterrows():
    students_data.append({
        'rank': int(row['序号']),
        'name': row['学生姓名'],
        'id': str(row['学号/工号']),
        'score': round(row['综合成绩'], 2),
        'discuss': round(row['讨论(20%)'], 2),
        'homework': round(row['作业(30%)'], 2),
        'attendance': round(row['签到(10%)'], 2),
        'course_points': round(row['课程积分(20%)'], 2),
        'group_task': round(row['分组任务（PBL）(20%)'], 2)
    })

import json
with open('students_data.json', 'w', encoding='utf-8') as f:
    json.dump(students_data, f, ensure_ascii=False, indent=2)

print('Data saved to students_data.json')