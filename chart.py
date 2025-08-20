import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports & Outdoors', 'Books', 'Beauty', 'Groceries']
n_scores = 100
means = {
    'Electronics': 7.8,
    'Clothing': 8.3,
    'Home & Kitchen': 8.1,
    'Sports & Outdoors': 7.6,
    'Books': 8.7,
    'Beauty': 7.9,
    'Groceries': 8.4
}
stddev = 0.4

scores = []
cats = []
for cat in categories:
    scores.extend(np.clip(np.random.normal(means[cat], stddev, n_scores), 6.0, 9.0))
    cats.extend([cat]*n_scores)
data = pd.DataFrame({'Category': cats, 'Satisfaction': scores})

sns.set_style('whitegrid')
sns.set_context('talk')
plt.figure(figsize=(8,8))  # 512x512px at dpi=64

bar = sns.barplot(x='Category', y='Satisfaction', data=data, palette='Set2', ci='sd', edgecolor='black')
bar.set_title('Average Customer Satisfaction by Product Category', fontsize=18, fontweight='bold')
bar.set_xlabel('Product Category', fontsize=14)
bar.set_ylabel('Avg Satisfaction Score', fontsize=14)
bar.tick_params(labelsize=12)
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
