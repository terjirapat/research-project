# A-Modified-Logistic-Regression-for-Positive-and-Unlabeled-Learning-final-submission — Results

### Summary of the Result Section

#### 1. Main Performance Results of the Proposed Method:
- **Simulated Data:**
  - The modified logistic regression (MLR) algorithm was tested on 81 different simulated scenarios (3 data distributions × 3 data sizes × 9 values of c).
  - The MLR algorithm showed improved results in 78 out of 81 scenarios (96.3% of the time).

- **MNIST Data:**
  - The MLR algorithm was tested on the MNIST dataset for binary classification of easily confused digits (3 vs. 5, 3 vs. 8, and 5 vs. 8).
  - The MLR algorithm outperformed other tested algorithms by an average of over 17%.

#### 2. Comparison with Baseline Methods:
- **Simulated Data:**
  - The MLR algorithm was compared against:
    - Oracle (standard logistic regression with known true labels)
    - Standard logistic regression (SLR) on PU data
    - Three estimators from [3], specifically the 'Elkan and Noto' estimator.
  - The MLR algorithm demonstrated superior performance compared to these baseline methods.

- **MNIST Data:**
  - The MLR algorithm was compared against the same baseline methods used in the simulated data.
  - Again, the MLR algorithm showed significant performance improvements over the baseline methods.

#### 3. Key Quantitative Improvements:
- **Simulated Data:**
  - MLR algorithm improved results 96.3% of the time compared to baselines.
  
- **MNIST Data:**
  - MLR outperformed other algorithms by an average of over 17%.

#### 4. Any Ablation Studies or Additional Analyses:
- **Simulated Data:**
  - The study involved varying parameters such as data distribution, data size, and the percentage of known positives (c).
  - 50 Monte Carlo simulations were performed for each scenario to ensure robustness and reliability of the results.

- **MNIST Data:**
  - The study did not perform any additional ablation studies but relied on direct comparisons with baselines.
  
#### 5. Observations Highlighted by the Authors:
- The MLR algorithm demonstrated robust performance across a variety of simulated scenarios and real-world image classification tasks.
- The use of the F-score as an evaluation metric was highlighted as particularly useful for handling uneven class sizes, which is a common challenge in practical applications.
