# 📊 Model Performance Comparison — Online Shoppers Purchasing Intent

### 🏆 Executive Summary
| Model | Accuracy | Precision (Class 1) | Recall (Class 1) | F1-Score | Status |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression** *(Baseline)* | 89.17% | **74.46%** | 38.38% | 0.5065 | Baseline Reference |
| **Random Forest** | 89.46% | 67.51% | 52.38% | 0.5899 | Medium Recall |
| **Gradient Boosting** ⭐ | **89.94%** | 68.11% | **57.42%** | **0.6231** | **Top Performer** |

---

### 🔍 Detailed Model Breakdown

#### 1. Logistic Regression (Baseline)
* **Performance Summary**: High precision, but misses 61.6% of actual buyers due to linear decision boundaries.
* **Confusion Matrix**:
  * **True Negatives (TN)**: `2,062` | **False Positives (FP)**: `47`
  * **False Negatives (FN)**: `220` | **True Positives (TP)**: `137`

#### 2. Random Forest
* **Performance Summary**: Significant jump in recall (+14%) and F1-score compared to the baseline.
* **Confusion Matrix**:
  * **True Negatives (TN)**: `2,019` | **False Positives (FP)**: `90`
  * **False Negatives (FN)**: `170` | **True Positives (TP)**: `187`

#### 3. Gradient Boosting Classifier ⭐
* **Performance Summary**: Strongest overall model. Captures **57.42%** of converting visitors while maintaining high overall accuracy (**89.94%**).
* **Confusion Matrix**:
  * **True Negatives (TN)**: `2,013` | **False Positives (FP)**: `96`
  * **False Negatives (FN)**: `152` | **True Positives (TP)**: `205`
