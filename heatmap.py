import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Use the existing confusion matrix
cm = np.array([[203, 19],
               [22, 259]])

# Normalize the confusion matrix by total
cm_normalized = cm / cm.sum()

# Plot heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(cm_normalized, annot=True, fmt='.2%', cmap='Blues',
            xticklabels=['Predicted 0', 'Predicted 1'],
            yticklabels=['Actual 0', 'Actual 1'])

plt.title('Confusion Matrix (Normalized)')
plt.xlabel('Predicted Label')
plt.ylabel('Actual Label')
plt.tight_layout()
plt.savefig('confusion_matrix_heatmap.png')  # Optional: saves image
plt.show()
