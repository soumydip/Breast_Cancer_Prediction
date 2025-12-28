#  Breast Cancer Detection AI (Random Forest Model)

This repository contains a robust **Machine Learning Diagnostic Tool** designed to predict whether a breast tumor is **Malignant (Cancerous)** or **Benign (Non-cancerous)**. The model is built using the **Random Forest Classifier** and features a custom-built data validation layer.

##  Key Features

- **Algorithm:** Implemented with **Random Forest**, an ensemble learning method that combines multiple decision trees for superior accuracy.
- **Range Validation System:** A built-in safety layer that ensures all user inputs fall within the biological boundaries (Min/Max) of the Wisconsin Breast Cancer Dataset.
- **Accuracy:** Achieves an impressive testing accuracy of **~96% - 98%**.
- **Interactive CLI:** A user-friendly terminal interface allowing users to choose between **Sample Data Testing** or **Manual Diagnostic Entry**.
- **Confidence Scoring:** Outputs the probability of the prediction, providing transparency on how certain the AI is about the result.

## Feature Categories

The model analyzes 30 different features divided into three main groups:

1. **Mean Values:** The average measurements of cell nuclei.
2. **Standard Error (SE):** The variation/uncertainty in measurements.
3. **Worst Values:** The "worst" or largest measurements (crucial for detecting malignancy).

##  Tech Stack

- **Language:** Python 3.13+
- **Machine Learning:** Scikit-learn
- **Data Manipulation:** Pandas, NumPy
- **Development Environment:** VS Code

## Installation & Usage

### 1. Clone the Repository

```bash
git clone [https://github.com/soumydip/Breast_Cancer_Prediction.git](https://github.com/soumydip/Breast_Cancer_Prediction.git)
cd Breast_Cancer_Prediction
```

### 2. Install Dependencies

```bash
pip install pandas numpy scikit-learn
```
- Ensure you have Python 3.13 or higher installed.

### 3. Run the Application

```bash
python breast_cencer.py
```

### 4. Follow On-Screen Prompts

- Choose between **Sample Data Testing** or **Manual Diagnostic Entry**.
- For manual entry, input the required features within the specified ranges.

##  Model Performance

The Random Forest model achieves a high accuracy rate of approximately **96% - 98%** on the Wisconsin Breast Cancer Dataset, making it a reliable tool for breast cancer detection.
| Metric | Value |
| ------------- |:--------------:|
| Accuracy | 96.49% |
| Precision (M) | 95% |
| Recall (B)| 98% |

##  Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements or bug fixes.

##  License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Acknowledgements
- Thanks to the creators of the Wisconsin Breast Cancer Dataset for providing a valuable resource for this project.
## Disclaimer
This tool is intended for educational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
