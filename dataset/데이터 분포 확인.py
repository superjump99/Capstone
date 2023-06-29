import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('MergeDate.csv')
y = df['Quantity']


keys = list(df.keys())[1:]
for key in keys:
    plt.hist(df[key])
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title(f'{key}')
    plt.show()

    plt.scatter(df['Order Date'],df[key])
    # 그래프 제목과 축 레이블 설정
    plt.title('Scatter Plot')
    plt.xlabel('Time')
    plt.ylabel('Y-axis')

    # 그래프 보이기
    plt.show()
