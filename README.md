# Comparative Analysis of SVM Performance on Colored vs. Grayscale CIFAR-10 Datasets
<div style="text-align: right">Uday Kiran Dasari <br> </div>

## Objective

The primary objective of this project is to evaluate the performance of Support Vector Machine (SVM) classifiers on the CIFAR-10 dataset by comparing the effectiveness of models trained on colored images versus those trained on grayscale images. The goal is to determine which version of the dataset yields better classification results and to analyze the underlying reasons for any observed differences in performance.

**Steps Involved:**

**1. Data Preparation:**
- Load the CIFAR-10 dataset, which consists of 60,000 32x32 color images in 10 classes.
- Split the dataset into training and testing sets for both colored and grayscale images.


**2.Model Training and Hyperparameter Tuning:**
- Use GridSearchCV to find the optimal hyperparameters for the SVM model. The parameters grid includes values for C and gamma.
- Train the SVM model on the colored CIFAR-10 dataset using the best parameters identified.
- Repeat the training process for the grayscale version of the CIFAR-10 dataset.


**3.Evaluation and Comparison:**
- Evaluate the trained SVM models on the respective test sets.
- Generate classification reports to assess the precision, recall, F1-score, and overall accuracy for both colored and grayscale datasets.
- Compare the performance metrics between the two versions of the dataset.


**4.Theoretical Considerations:**
- Discuss the potential impact of converting colored images to grayscale on the model's ability to differentiate between classes.
- Analyze the importance of color information in object recognition tasks.

## Comparative Analysis: Color CIFAR vs. Grayscale CIFAR
1. **Overall F1 Score:**
Colored CIFAR: 51%
Grayscale CIFAR: 43%
The SVM model performs better on the colored dataset.


2. **Class-wise F1 Score:**
The F1 scores for individual classes are higher in the colored dataset compared to the grayscale dataset, indicating that color information aids in better class differentiation.


3. **Precision and Recall:**
Higher precision and recall in the colored dataset demonstrate improved performance in identifying relevant instances with fewer false positives and negatives.


**Theoretical Considerations:**


1. **Information Loss in Grayscale Conversion:**
    Converting images to grayscale results in the loss of color information, which is crucial for distinguishing between certain objects.


2. **Texture and Shape Recognition:**
    While grayscale images can suffice for tasks relying on texture and shape, the diverse objects in CIFAR-10 (e.g., vehicles and animals) benefit significantly from color information.


3. **Hyperparameters:**
    The optimal parameters (svc__C: 5, svc__gamma: 0.005) were consistent across both datasets, indicating stable model tuning. Expanding the parameter grid could potentially enhance the model further.

## Conclusion
The analysis demonstrates that the SVM classifier achieves higher F1 scores when trained on the colored CIFAR-10 dataset compared to the grayscale version. This underscores the importance of color information in image classification tasks, enhancing the model's ability to distinguish between different objects. The reduction in classification performance with grayscale images highlights the loss of crucial features that color provides. This comparative study emphasizes the value of preserving color information for effective image classification using SVMs.
