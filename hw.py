'''Homework'''
import pandas as pd
import matplotlib.pyplot as plt

SIZE = 7
TOP = 10

def format_students(row):
    '''Форматирует числа с приставками СИ'''
    if row[-1] == 'k':
        return float(row.rstrip('k')) * 1000
    if row[-1] == 'm':
        return float(row.rstrip('m')) * 1000
    return float(row)

data = pd.read_csv('coursera_data.csv')
organizations = data.groupby(['course_organization'])['id'].count().reset_index(
  name='cnt').sort_values(['cnt'],ascending=False)['course_organization'].head(TOP)
fig, ax = plt.subplots(2,len(organizations),figsize=(SIZE*len(organizations),SIZE))
for j,el in enumerate(organizations):
    res = data[data['course_organization'] == el]
    difficulties = res['course_difficulty'].unique()
    nums1 = []
    cols1 = []
    for i in difficulties:
        difficulty = res[res['course_difficulty'] == i]
        nums1.append(len(difficulty['id']))
        cols1.append(i)
    cols2 = ['max enrolled','min enrolled', 'average enrolled']
    res['course_students_enrolled'] = res['course_students_enrolled'].apply(format_students)
    nums2 = [res['course_students_enrolled'].max(),
            res['course_students_enrolled'].min(),
            res['course_students_enrolled'].sum()/len(res['course_students_enrolled'])]
    ax[0][j].pie(nums1,labels=cols1, autopct='%.0f%%')
    ax[1][j].bar(cols2, nums2,log=True)
    ax[0][j].set_title(el)
fig.tight_layout()
plt.show()
