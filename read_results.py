import json, collections
results = json.load(open('results.json'))
d = collections.Counter()
for idi, r in results.items():
    d[(r['topic'].replace('nucleaire','nucléaire'),r['stance'])] += 1
    """
    if r['topic'] != 'viande':
        continue
    print('*****************************************')
    print('id: ',idi)
    print(r['topic'],':',r['stance'],':',r['text'])
    #print(idi, r['text'])
    """

print(d)

import matplotlib.pyplot as plt
import numpy as np


labels = list(set([ t for (t,s) in d.keys()]))
labels.remove('other')
stances = 'positive', 'negative', 'other'
for l in labels:
  for s in stances:
    if (l,s) not in d:
      d[(l,s)] = 0
pos_means = [d[(t,'positive')] for t in labels]
neg_means = [d[(t,'negative')] for t in labels ]
neut_means = [d[(t,'other')] for t in labels ]
x = np.arange(len(labels))  # the label locations
width = 0.2 # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, pos_means, width, label='positive')
rects2 = ax.bar(x, neg_means, width, label='negative')
rects3 = ax.bar(x + width, neut_means, width, label='neutral')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('number of tweets')
ax.set_title('Topics and stance')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)

fig.tight_layout()

plt.show()
