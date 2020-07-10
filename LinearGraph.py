x_low = 85
y_max = 130
plot_chart(X_2, y_2, y_2_pred, x_low, 94, 0, y_max, c)
plt.text(92, 20, 'Forward', color = 'red')
plt.text(92, 17, 'Midfielder', color = 'blue')
plt.text(92, 14, 'Defender', color = 'green')
plt.text(92, 11, 'Goalkeeper', color = 'purple')
ax = plt.gca()
for index, row in df_2.iterrows():
    if row['Overall'] > x_low and row['Value (M)'] < y_max:
        ax.text(row['Overall'], row['Value (M)'], '{}, {}'.format(row['Name'],row['Age']))