import matplotlib.pyplot as plt

Country = ['Edge Detection', 'SVM Algorithm']
GDP_Per_Capita = [754, 482]

plt.bar(Country, GDP_Per_Capita)
plt.title('Time Analysis')
plt.xlabel('Algorithm')
plt.ylabel('Time in Milli Seconds')
plt.show()