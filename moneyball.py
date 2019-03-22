import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn import metrics

df = pd.read_csv("baseball.csv")

print(df.head())

# mean of all Wins
print(df['W'].mean())

#
def apply_win_bins(W):
    if W < 50:
        return 1
    if W >= 50 and W <= 69:
        return 2
    if W >= 70 and W <= 89:
        return 3
    if W >= 90 and W <= 109:
        return 4
    if W >= 110:
        return 5
df['win_bins'] = df['W'].apply(apply_win_bins)

f = plt.figure(1)
plt.hist(df['W'])
plt.xlabel('Wins')
plt.title('Distribution of Wins')
f.show()

g = plt.figure(2)
plt.scatter(df['Year'], df['W'], c=df['win_bins'])
plt.title('Wins scatter Plot')
plt.xlabel('Year')
plt.ylabel('Wins')

g.show()
s_score_dict ={}
for i in range(2,11):
    km = KMeans(n_clusters=i, random_state=1)
    l = km.fit_predict(data_attributes)
    s_s = metrics.silhouette_score(data_attributes, 1)
    s_score_dict[i] = [s_s]

print(s_score_dict)

kmeans_model = Kmeans(n_clusters=6, random_state=1)
distances = kmeans_model.fit_transform(data_attributes)

labels = kmeans_model.labels_

h = plt.figure(3)
plt.scatter(distances[:,0], distances[:,1], c=labels)
plt.title('Kmeans Clusters')
h.show()

input()
