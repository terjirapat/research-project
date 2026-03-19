# A-Modified-Logistic-Regression-for-Positive-and-Unlabeled-Learning-final-submission

## Global Summary

This paper tackles the Positive and Unlabeled (PU) learning problem in semi-supervised binary classification, where only a subset of positive samples is known, and the rest are unlabeled. Previous approaches often require negative samples, which may not be feasible. To address this, the authors propose a modified logistic regression model with a variable upper bound to improve theoretical solutions for PU learning. They test their method on simulated data and the MNIST dataset. The modified logistic regression model shows significant improvements, outperforming existing methods by an average of over 17% on the MNIST dataset. Key contributions include a new probabilistic algorithm for PU learning, theoretical justification for the modification, and improved performance over benchmark algorithms. The research provides a practical and effective solution for scenarios with limited labeled data, paving the way for broader applications in image classification and beyond.

## Abstract

**1. Research problem:**  
The paper addresses the positive and unlabeled (PU) learning problem in semi-supervised binary classification, where only a subset of positive samples is known, and both positive and negative samples are otherwise unlabeled.

**2. Proposed approach:**  
The authors develop a modified logistic regression learner with a variable upper bound, building on an existing probabilistic PU learning algorithm, aiming to provide a better theoretical solution for the problem.

**3. Experimental setup:**  
The proposed method is tested on both simulated data and a real-world image classification problem using the MNIST dataset.

**4. Key results:**  
The modified logistic regression learner shows significantly improved results on the MNIST dataset compared to existing methods.

**5. Main contribution:**  
The paper introduces a new modified logistic regression learner with a variable upper bound, which provides a better theoretical solution for the PU learning problem, demonstrating improved performance on both simulated data and the MNIST dataset.

## Introduction

### Summarization of the Introduction Section

**1. Background Context of the Research Area:**
The research area focuses on classification problems within machine learning and signal processing. These problems encompass a wide range of applications, including image object identification, video activity categorization, audio signal classification, text and document classification, fraud detection, and disease gene identification.

**2. The Main Problem Being Addressed:**
The primary issue addressed in this paper is the Positive and Unlabeled learning (PU Learning) problem, which arises when training data consists only of a small set of positive samples and a large set of unlabeled samples, with no negative samples available.

**3. Limitations of Previous Approaches:**
Previous methods for handling the PU Learning problem often require a small set of negative training data, which may not always be feasible or cost-effective to acquire. Additionally, existing algorithms for PU Learning may not fully leverage the available unlabeled data or may not be sufficiently accurate in real-world applications.

**4. The Research Gap This Paper Identifies:**
There is a need for more effective algorithms that can accurately solve the PU Learning problem using only positive and unlabeled data. Existing solutions may not sufficiently address the limitations and practical challenges of real-world applications that require minimal labeled data.

**5. The Core Idea or Hypothesis of the Paper:**
The paper proposes a probabilistic algorithm based on a modified logistic regression to address the PU Learning problem. This approach aims to improve upon existing methods by better utilizing the available positive and unlabeled data to train the classification model.

**6. The Key Contributions Claimed by the Authors:**
- Introduction of a modified logistic regression algorithm specifically designed for the PU Learning problem.
- Theoretical justification for the proposed modification.
- Application of the algorithm to simulated data and the MNIST image dataset to demonstrate its effectiveness.
- Comparison and potential improvement over existing benchmark algorithms for the PU Learning problem, as referenced in [3], [2], and [4].

## Methodology

### Summary of Methodology

#### 1. Core Idea of the Proposed Method
The paper proposes a method to estimate the class prior \( p(y = 1) \) from positive and unlabeled data. The core idea hinges on addressing the challenges of distinguishing between well-separated and poorly-separated positive and negative classes without expert domain knowledge. This is achieved through the introduction of a modified logistic regression model that accommodates the SCAR (Selected Completely At Random) assumption and the positive subdomain assumption.

#### 2. Model or Algorithm Structure
The proposed method involves a two-step process:
1. **Learning a Non-Traditional Classifier**: This step involves using a modified logistic regression model to estimate the probability that a sample is labeled positive.
2. **Constructing the Final Classifier**: Using the results from the first step, the method then estimates the class prior \( p(y = 1) \).

#### 3. Key Components or Modules of the System
- **Non-Traditional Classifier**: A modified logistic regression model \( g_{MLR}(x) \) that outputs probabilities in the range [0, \( c \)] instead of [0, 1].
- **Traditional Classifier**: The final model \( f(x) = p(y = 1 | x) \) derived from the non-traditional classifier and an estimate of the constant \( c \).

#### 4. Important Mathematical Formulations
- **Positive and Unlabeled Problem Formulation**:
  \[
  p(x, s) = p(x | s, y)p(s | y)p(y)
  \]
- **SCAR Assumption**:
  \[
  p(s = 1 | y = 1) = c
  \]
- **Relationship between Classifiers**:
  \[
  p(y = 1 | x) = \frac{p(s = 1 | x)}{c}
  \]
- **Modified Logistic Regression**:
  \[
  g_{MLR}(x) = \frac{1}{1 + \exp(-w̅^T x / b^2)}
  \]
  The upper bound of this function \( ĉ \) is estimated as:
  \[
  ĉ = \frac{1}{1 + b^2}
  \]

#### 5. Training Procedure or Optimization Approach
- **Step 1**: Learn the non-traditional classifier by training the modified logistic regression model. This involves maximizing the likelihood of the data by tuning the weight vectors \( w̅ \) and the variable \( b \) over a set number of epochs \( \epsilon \) with an adaptive learning rate \( \lambda \).
- **Step 2**: Use the learned value of \( b \) to estimate \( ĉ \) and then construct the traditional classifier using the estimated \( ĉ \).

#### 6. Assumptions Made by the Method
- **Positive Subdomain Assumption**: The region of highest density of labeled positive samples consists entirely of positive samples.
- **SCAR Assumption**: Positive labeled samples are selected completely at random from the set of all positive samples.

### Conceptual Explanation
The proposed method leverages the concept of a modified logistic regression to address the limitations of standard logistic regression when dealing with positive and unlabeled data. By introducing a variable upper bound less than 1 for the logistic function, the method can more accurately model the probability that a sample is labeled positive. This, in turn, allows for a more precise estimation of the class prior \( p(y = 1) \), which is crucial for tasks involving positive and unlabeled data. The method's robustness and effectiveness stem from its ability to account for the inherent biases and overlaps between positive and negative classes, ultimately improving performance in such scenarios.

## Results

### Summary of Results

#### 1. Main Performance Results of the Proposed Method
The paper evaluated the proposed modified logistic regression (MLR) algorithm using both simulated data and the MNIST dataset. The main performance results demonstrated that the MLR algorithm performed effectively under various conditions:

- **Simulated Data:** 
  - The MLR algorithm was tested on 81 different scenarios combining three data distributions, three data sizes, and nine values of 𝑐 (percentage of known positives).
  - Each scenario was subjected to 50 Monte Carlo simulations.
  - The MLR algorithm showed improved results in 78 out of 81 scenarios (96.3%).

- **MNIST Dataset:** 
  - The MLR algorithm was tested on the MNIST handwritten digit classification problem.
  - Binary classification was performed for the digit pairs 3 and 5, 3 and 8, and 5 and 8.
  - The MLR algorithm outperformed other algorithms by an average of over 17%.

#### 2. Comparison with Baseline Methods
The MLR algorithm was compared against several baseline methods:
- **Oracle (Standard Logistic Regression):** A baseline where all true labels are known.
- **Standard Logistic Regression (SLR):** Applied on Positive-Unlabeled (PU) data.
- **Three Estimators from [3]:** Specifically, the best estimator from [3] was used for comparison, referred to as the 'Elkan and Noto' method.

#### 3. Key Quantitative Improvements
- **Simulated Data:**
  - The MLR algorithm improved results over the Elkan and Noto estimator in 78 out of 81 scenarios.
- **MNIST Data:**
  - The MLR algorithm achieved an average performance improvement of over 17% compared to the other tested algorithms.

#### 4. Any Ablation Studies or Additional Analyses
- The paper does not explicitly mention any ablation studies or additional analyses beyond the comparisons with baseline methods.

#### 5. Observations Highlighted by the Authors
- **Effectiveness in Uneven Class Sizes:** The F-score was used as the evaluation metric due to the uneven class sizes in the datasets, highlighting the robustness of the MLR algorithm in such scenarios.
- **Robustness:** The MLR algorithm demonstrated consistent performance improvements across a wide range of simulated scenarios and real-world digit classification tasks.

### Evidence Supporting the Claims
The claims of the paper are supported by extensive simulation and empirical testing:
- **Monte Carlo Simulations:** The 50 simulations for each scenario in the simulated data provided a robust evaluation of the MLR algorithm.
- **Real-world Dataset:** The MNIST dataset, with its binary classification of easily confusable digits, provided a practical benchmark for validating the algorithm's effectiveness.

## Conclusion

### Final Takeaways

#### 1. Main Achievements of the Research
The research successfully addresses the positive unlabeled (PU) learning problem, which is crucial in scenarios where labeled data is scarce and true negative data is either difficult or impractical to obtain. The proposed modified logistic regression model has demonstrated exceptional effectiveness, outperforming current state-of-the-art algorithms. This effectiveness was validated through both simulated data and real-world application using the MNIST dataset for image classification.

#### 2. Key Contributions to the Field
The key contributions of this research include:
- A novel approach to the PU learning problem, providing a solution that is both effective and practical.
- A modified logistic regression model that significantly improves upon existing methods, as evidenced by its superior performance on both simulated and real-world datasets.
- Initial evidence that the proposed method can be a valuable tool in real-world applications, particularly in scenarios involving image classification.

#### 3. Limitations Acknowledged by the Authors
The authors acknowledge that while their model shows promising results, it has only been tested against a limited number of algorithms and datasets. They recognize the need for further comparison with a broader range of algorithms and additional datasets to fully validate the robustness and generalizability of their approach.

#### 4. Future Research Directions Suggested
The authors propose several directions for future research:
- Conducting further comparisons of their modified logistic regression model with a wider array of existing algorithms.
- Testing the model on a more diverse set of datasets to ensure its effectiveness and reliability across different applications.
- Exploring potential improvements and extensions to the proposed model to enhance its performance and applicability.
