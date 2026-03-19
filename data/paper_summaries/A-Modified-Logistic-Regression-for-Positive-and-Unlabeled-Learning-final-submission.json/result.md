# A-Modified-Logistic-Regression-for-Positive-and-Unlabeled-Learning-final-submission — Results

### Summary of Results

#### 1. Main Performance Results of the Proposed Method
- **Simulated Data**: The proposed modified logistic regression (MLR) algorithm was evaluated on 81 different scenarios combining three simulated data distributions, three different data sizes, and nine values of \( c \) (ranging from 0.1 to 0.9). MLR was found to provide improved results in 78 out of 81 simulations (96.3% of the time).
- **MNIST Data**: The MLR algorithm was tested on the MNIST dataset for binary classification of commonly mis-classified digit pairs (3 and 5, 3 and 8, 5 and 8) using unrolled pixel values. MLR outperformed other tested algorithms by an average of over 17%.

#### 2. Comparison with Baseline Methods
- **Simulated Data**: MLR was compared against an Oracle (standard logistic regression with all true labels known), standard logistic regression (SLR) on PU data, three estimators from [3] (specifically, 'Elkan and Noto'), and the proposed MLR algorithm. MLR demonstrated superior performance in 78 out of 81 simulations.
- **MNIST Data**: MLR outperformed the Oracle, SLR, and other baseline methods by an average of over 17% in classification accuracy for the binary classification tasks on the MNIST dataset.

#### 3. Key Quantitative Improvements
- **Simulated Data**: MLR improved results in 78 out of 81 scenarios.
- **MNIST Data**: MLR achieved an average improvement of over 17% in classification accuracy compared to other tested algorithms.

#### 4. Any Ablation Studies or Additional Analyses
- The paper does not explicitly mention ablation studies or additional analyses beyond the main comparisons outlined.

#### 5. Observations Highlighted by the Authors
- The authors highlight that the F-score was chosen as the evaluation metric due to the potential for uneven class sizes, making accuracy and error rate metrics less informative.
- MLR consistently showed robustness and effectiveness across different data sizes, distributions, and values of \( c \) in both simulated and MNIST datasets.
- The performance improvements in MNIST were particularly notable for the binary classification of digits 3 and 8, where MLR achieved superior results with a low \( c \) value (e.g., \( c = 0.1 \)).

### Supporting Evidence
- The robust performance of the proposed MLR algorithm is supported by extensive Monte Carlo simulations and real-world application to the MNIST dataset, demonstrating significant improvements over standard and other PU learning methods.
