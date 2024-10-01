import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

restaurants = pd.read_csv('/Users/olly/Downloads/foodwheel/restaurants.csv')
# print(restaurants.head())
# print(restaurants.describe(include='all'))
# print(restaurants.info())

cuisine_counts = restaurants.groupby(['cuisine']).name.count().reset_index()
# print(cuisine_counts)

cuisine_pie_count = cuisine_counts.name
# print(cuisine_pie_count)
cuisine_pie_label = cuisine_counts.cuisine

plt.figure(figsize=(8,10))
ax = plt.subplot(1, 1, 1)
ax.pie(cuisine_pie_count, labels=cuisine_pie_label)
plt.title('Cuisines Available')
# plt.savefig('/Users/olly/PycharmProjects/restaurant_analysis_project/cuisines_piechart.png')
# plt.show()
plt.clf()

orders = pd.read_csv('/Users/olly/Downloads/foodwheel/orders.csv')
print(orders.head())
# print(orders.describe(include='all'))
# print(orders.info())

orders['month'] = orders.date.apply(lambda x: x.split('-')[0])
print(orders.head())

avg_order = orders.groupby(['month']).price.mean().reset_index()
print(avg_order)

std_order = orders.groupby(['month']).price.std().reset_index()
print(std_order)

plt.figure(figsize=(8, 8))
ax = plt.subplot(1, 1, 1)
plt.bar(range(len(avg_order)), avg_order.price, yerr=std_order.price, capsize=5)
ax.set_xticks(range(len(avg_order)))
ax.set_xticklabels(['April', 'May', 'June', 'July', 'August', 'September'])
plt.ylabel('Average Order Price')
plt.title('Average Order Amount Over Time')
# plt.savefig('/Users/olly/PycharmProjects/restaurant_analysis_project/average_order_barchart.png')
# plt.show()
plt.clf()

customer_amount = orders.groupby(['customer_id']).price.sum().reset_index()
print(customer_amount.head())

plt.figure(figsize=(8, 8))
plt.subplot(1, 1, 1)
plt.hist(customer_amount.price.values, range=(0, 200), bins=(40))
plt.xlabel("Total Spent")
plt.ylabel("Number of Customers")
plt.title("Customer Spending")
# plt.savefig('/Users/olly/PycharmProjects/restaurant_analysis_project/Customer_Spending_histogram.png')
# plt.show()
plt.clf()
