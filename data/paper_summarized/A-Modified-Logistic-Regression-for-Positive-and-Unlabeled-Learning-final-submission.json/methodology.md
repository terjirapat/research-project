# A-Modified-Logistic-Regression-for-Positive-and-Unlabeled-Learning-final-submission — Methodology

### Summary of the Methodology Section

#### Core Idea of the Proposed Method
The core idea of the proposed method is to accurately estimate the overall percentage of positive samples (class prior) from positive and unlabeled data. This is achieved by introducing a modified logistic regression model that accounts for the "selected completely at random" (SCAR) assumption and the partial separability or positive subdomain assumption.

#### Model or Algorithm Structure
The proposed approach consists of two main steps: learning a non-traditional classifier and constructing the final traditional classifier. 

1. **Learning a Non-traditional Classifier**: This step involves using modified logistic regression to estimate the probability that a given sample is labeled positive.
2. **Constructing the Final Classifier**: This step uses the estimated probability from the first step to derive the traditional classifier, which estimates the probability that a given sample is actually positive.

#### Key Components or Modules of the System
1. **Modified Logistic Regression (MLR)**: This is the main component of the algorithm. It is a modified version of standard logistic regression that can output probabilities in the range [0, c], where c is a learned upper bound.
2. **Non-traditional Classifier**: This classifier estimates the probability that a sample is labeled as positive.
3. **Traditional Classifier**: This is the final classifier that estimates the probability that a sample belongs to the positive class.

#### Important Mathematical Formulations
1. **Probability of Label Being Positive**:
   \[
   p(y = 1 | x) = \frac{p(s = 1 | x)}{c}
   \]
   where \(c = p(s = 1 | y = 1)\) is the constant probability that a positive sample is labeled.
   
2. **Modified Logistic Regression Model**:
   \[
   g_{MLR}(x) = \frac{1}{1 + e^{-(\bar{w}^T \bar{x} + b^2)}}
   \]
   The upper bound of this model is given by:
   \[
   \hat{c} = \frac{1}{1 + b^2}
   \]

#### Training Procedure or Optimization Approach
The training procedure involves two main steps:
1. **Learning the Non-traditional Classifier**:
   - Initialize weights \(\bar{w}\) and variable \(b\).
   - Maximize the likelihood of the data by taking the gradient of the log-likelihood.
   - Train for a fixed number of epochs (\(\epsilon\)) with an adaptive learning rate (\(\lambda\)).
   
2. **Estimating the Constant \(c\)**:
   - Use the learned value of \(b\) to estimate \(\hat{c}\).
   - Construct the traditional classifier using the estimated \(\hat{c}\) and the non-traditional classifier.

#### Assumptions Made by the Method
1. **Partial Separability or Positive Subdomain Assumption**: The region of highest density of labeled positive samples must consist entirely of positive samples.
2. **SCAR Assumption**: Positive labeled samples are selected completely at random from the set of all positive samples. This ensures that the model can reasonably estimate the distributions of positive and negative samples.

### Conceptual Explanation
The proposed method leverages a modified logistic regression to address the challenges of learning from positive and unlabeled data. By introducing a non-traditional classifier that outputs probabilities within a range [0, c], the method ensures that the upper bound c is learned from the data rather than being fixed. This approach allows for more accurate estimation of the class prior and improves the performance of the final traditional classifier. The assumptions of partial separability and SCAR are crucial for ensuring the validity of the derived probabilistic relationships.
