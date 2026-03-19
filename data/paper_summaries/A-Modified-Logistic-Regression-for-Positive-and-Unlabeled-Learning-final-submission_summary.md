# A-Modified-Logistic-Regression-for-Positive-and-Unlabeled-Learning-final-submission

## Global Summary

The paper tackles the Positive and Unlabeled (PU) learning problem, which is a semi-supervised binary classification scenario where only a fraction of positive samples are known, and the status of the remaining samples is unknown. Existing methods often require negative labeled samples, which are costly or impractical to obtain. To address this, the authors propose a novel modified logistic regression learner with a variable upper bound, which they argue offers a superior theoretical approach to PU learning.

The proposed methodology involves a two-step process: learning a nontraditional classifier to estimate the probability of a sample being labeled positive and then constructing a traditional classifier to estimate the actual positive probability. The key component of this method is a modified logistic regression (MLR) that learns an adaptive upper bound during training, enhancing its ability to handle the inherent labeling biases in PU data.

Experiments were conducted on both simulated data and the MNIST dataset. The MLR algorithm outperformed existing methods in 96.3% of the simulated data scenarios and showed a consistent improvement of over 17% in classifying confusable digit pairs on MNIST compared to baselines. These results highlight the robustness and generalizability of the MLR algorithm.

The main contribution of the paper is the introduction of a modified logistic regression technique that effectively addresses the challenges of PU learning without requiring negative labeled samples. This approach significantly improves classification performance in both simulated and real-world image classification tasks. The authors acknowledge the need for further validation across additional datasets and suggest future research will focus on broader comparative analyses to further solidify the method's applicability in diverse scenarios.

## Abstract

1. **Research problem**: The paper addresses the positive and unlabeled (PU) learning problem, a type of semi-supervised binary classification where only a fraction of positive samples is known, while the status of the remaining samples (both positive and negative) is unknown.

2. **Proposed approach**: The authors build upon an existing probabilistic PU learning algorithm by introducing a new modified logistic regression learner with a variable upper bound, which they argue offers a superior theoretical approach to the PU learning problem.

3. **Experimental setup**: The proposed method was tested on both simulated data and a simple image classification task using the MNIST dataset.

4. **Key results**: The new logistic regression learner achieved significantly improved results in both experimental settings.

5. **Main contribution**: The main contribution is the introduction of a modified logistic regression learner with a variable upper bound, which provides a better theoretical solution for the PU learning problem compared to existing methods.

## Introduction

### Summary of the Introduction Section

#### 1. Background Context
The introduction begins by highlighting the importance of classification tasks in machine learning and signal processing. It mentions various applications such as image object identification, video activity categorization, and disease gene identification, underscoring the broad relevance of classification in diverse fields.

#### 2. The Main Problem
The primary focus is on the Positive and Unlabeled (PU) learning problem, a variant of supervised classification where only a small subset of data samples is labeled as positive, while the remaining samples are unlabeled. This scenario arises when it is costly or impractical to obtain sufficient labeled data.

#### 3. Limitations of Previous Approaches
Previous approaches to PU learning often require a set of negative labeled samples to effectively distinguish between positive and unlabeled data. However, in many practical scenarios, obtaining even a small set of negative labels is challenging or prohibitively expensive. 

#### 4. The Research Gap
The paper identifies a gap in existing methods that do not adequately address the PU learning problem without requiring any negative labeled samples. Current algorithms often fail to generalize well when only positive and unlabeled samples are available, necessitating new approaches that can leverage unlabeled data more effectively.

#### 5. Core Idea or Hypothesis
The core idea of this paper is to propose a probabilistic algorithm based on modified logistic regression to tackle the PU learning problem. The approach modifies the existing benchmark algorithm proposed by Elkan and Noto to enhance its performance when only positive and unlabeled samples are available.

#### 6. Key Contributions
The authors claim several key contributions:
- A novel probabilistic algorithm that uses modified logistic regression to solve the PU learning problem.
- A theoretical justification for the modifications made to the existing algorithm.
- Application of the proposed algorithm to both simulated data and real-world images from the MNIST dataset to demonstrate its effectiveness.

This research is crucial as it aims to address a significant limitation in existing PU learning methods, offering a practical solution for scenarios where only positive and unlabeled data are available.

## Methodology

### Summary of Methodology

#### Core Idea of the Proposed Method
The core idea of the proposed method is to tackle the problem of estimating the class prior, 𝑝(𝑦 = 1), from positive and unlabeled (PU) data. This involves inferring the likelihood of a sample being positive even when only some samples are labeled and the rest are unlabeled.

#### Model or Algorithm Structure
The proposed method leverages a modified logistic regression algorithm to address the challenge of PU learning. The algorithm consists of two main steps:

1. **Learning a nontraditional classifier**: The algorithm first learns a nontraditional classifier to estimate the probability that a given sample is labeled positive.
2. **Constructing the final classifier**: Using the learned values from the first step, it constructs the traditional classifier to estimate the probability that a sample is actually positive.

#### Key Components or Modules of the System
1. **Modified Logistic Regression (MLR)**: A variant of logistic regression that has an upper bound on its output, which is learned during training, rather than fixed at 1. This helps in dealing with the SCAR (Selected Completely At Random) assumption.
2. **Weight Vector (𝑤̅)**: The learned parameters of the MLR model.
3. **Random Variable (𝑏)**: An additional variable introduced in the MLR model to control the upper bound.
4. **Adaptive Learning Rate (𝜆)**: Used during the training to converge the model.

#### Important Mathematical Formulations (if essential)
1. **Nontraditional Classifier**: 
   \[
   g(x) = p(s = 1|x)
   \]
2. **Modified Logistic Regression**:
   \[
   g_{MLR}(x) = \frac{e^{w^T x}}{1 + b^2 e^{w^T x}}
   \]
3. **Upper Bound Asymptote**:
   \[
   ĉ = \frac{1}{1 + b^2}
   \]
4. **Traditional Classifier**:
   \[
   f(x) = \frac{g(x)}{c}
   \]

#### Training Procedure or Optimization Approach
The training procedure involves maximizing the likelihood of the data samples and their labels (where available) using gradient ascent on the log-likelihood function. The algorithm iterates for a fixed number of epochs (𝜀) with an adaptive learning rate (𝜆) until convergence. The model parameters (𝑤̅ and 𝑏) are adjusted to maximize the likelihood, and the upper bound is learned as part of this process.

#### Assumptions Made by the Method
1. **Partial Separability or Positive Subdomain Assumption**: The region of highest density of labeled positive samples is assumed to consist entirely of positive samples.
2. **SCAR (Selected Completely At Random) Assumption**: Positive labeled samples are assumed to be selected randomly from the set of all positive samples without bias.

### Conceptual Explanation
The method works by first learning a nontraditional classifier that estimates the probability a sample is labeled positive, not necessarily that it is positive. The modified logistic regression ensures the output is bounded by an upper limit less than 1, which is learned during training. This approach accounts for the possibility that not all positive samples are labeled. Using the learned upper bound, the final traditional classifier estimates the probability that a sample is actually positive. The method's assumptions help in managing the uncertainties inherent in the PU data, ensuring accurate estimates of the class prior.

This method improves performance by effectively handling the limitations of PU data, providing a probabilistic framework that accounts for the labeling bias and overlap between positive and unlabeled samples.

## Results

### Summary of Results Section

#### 1. Main Performance Results of the Proposed Method
The proposed modified logistic regression (MLR) algorithm demonstrated superior performance in both simulated data and MNIST dataset evaluations. Specifically:
- In simulated data scenarios, the MLR algorithm outperformed other methods 96.3% of the time across 81 different conditions.
- For MNIST data, MLR consistently showed better results, particularly in classifying confusable digit pairs, achieving an average improvement of over 17% compared to other methods.

#### 2. Comparison with Baseline Methods
The MLR algorithm was compared against several baselines:
- An Oracle classifier (perfect classification with known true labels)
- Standard logistic regression (SLR) on positive-unlabeled (PU) data
- Three estimators from another study, with the best one referred to as 'Elka n and Noto'
The MLR algorithm outperformed all these baseline methods in the majority of simulated data scenarios and in all MNIST classification tasks.

#### 3. Key Quantitative Improvements
- In simulated data, MLR outperformed other methods in 78 out of 81 scenarios.
- On MNIST data, the average improvement of MLR over other methods was over 17% in classifying confusable digit pairs.

#### 4. Any Ablation Studies or Additional Analyses
The paper does not detail specific ablation studies but does conduct thorough evaluations by varying parameters (e.g., different data distributions, sizes, and values of \( c \)) and performing 50 Monte Carlo simulations for each scenario.

#### 5. Observations Highlighted by the Authors
The authors highlighted the following key observations:
- The MLR algorithm's robustness and effectiveness across various simulated data scenarios.
- The significant improvement in performance on real-world data (MNIST), especially for challenging binary classifications involving easily confused digits.
- The consistent superiority of MLR under different conditions, showcasing its reliability and generalizability.

Overall, the evidence supports the claims that the proposed MLR algorithm provides substantial improvements over existing methods, particularly in dealing with uneven class sizes and in practical image classification tasks.

## Conclusion

### 6. CONCLUSION

1. **Main Achievements**: 
   The research successfully developed a modified logistic regression approach for the positive unlabeled (PU) learning problem, demonstrating superior performance over existing state-of-the-art algorithms on both simulated data and the MNIST dataset for real-world image classification.

2. **Key Contributions**:
   The primary contribution lies in the proposed modified logistic regression technique, which effectively addresses the challenges of obtaining labeled data and accurately classifies data with only positive and unlabeled samples.

3. **Limitations Acknowledged**:
   While the proposed method has shown promising results, the authors acknowledge the need for further comparative analysis with more algorithms and across additional datasets to validate the generalizability of their approach.

4. **Future Research Directions**:
   The authors suggest future work will involve comparing their algorithm with others on a wider range of datasets to further evaluate its robustness and performance. This will help to solidify the method's applicability in diverse real-world scenarios.
