# A-Modified-Logistic-Regression-for-Positive-and-Unlabeled-Learning-final-submission — Methodology

### Summary of Methodology

#### 1. Core Idea of the Proposed Method
The proposed method addresses the challenge of estimating the class prior \( p(y = 1) \) from positive and unlabeled data. The key idea is to construct a modified logistic regression model that can account for the assumptions about the data distribution, particularly the "selected completely at random" (SCAR) assumption and the positive subdomain assumption. This allows the method to derive a probabilistic classifier that can better estimate the likelihood of a sample being labeled positive.

#### 2. Model or Algorithm Structure
The proposed method utilizes a two-step process involving a modified logistic regression algorithm. The first step involves learning a non-traditional classifier that estimates the probability of a sample being labeled positive. The second step constructs the final classifier using this non-traditional classifier and an estimated constant probability \( c \).

#### 3. Key Components or Modules of the System
- **Non-traditional Classifier (𝑔(𝑥))**: Estimates the probability that a sample is labeled positive.
- **Modified Logistic Regression (MLR)**: A logistic regression model modified to have an upper bound less than 1, allowing it to learn the probability \( p(s = 1|𝑥) \) accurately.
- **Constant Probability Estimator (𝑐̂)**: An estimate of the constant probability \( c \) that a positive sample is labeled, derived from the learned parameters of the MLR.

#### 4. Important Mathematical Formulations
- The relationship between the traditional classifier \( f(𝑥) \), the non-traditional classifier \( g(𝑥) \), and the constant \( c \) is given by:
  \[
  f(𝑥) = \frac{g(𝑥)}{c}
  \]
  where \( f(𝑥) = p(𝑦 = 1|𝑥) \) and \( g(𝑥) = p(𝑠 = 1|𝑥) \).

- The modified logistic regression function is:
  \[
  g_{MLR}(𝑥) = \frac{1}{1 + e^{-(\bar{w} \cdot \bar{x} + b^2)}}
  \]
  This formulation ensures the output of \( g_{MLR}(𝑥) \) is in the range [0, \( c \)].

#### 5. Training Procedure or Optimization Approach
- **Step 1: Learning the Non-traditional Classifier**
  - The model learns the weight vector \( \bar{w} \) and the variable \( b \) by maximizing the likelihood of the data samples and their labels.
  - The learning process involves taking the gradient of the log-likelihood and training for a fixed number of epochs \( \epsilon \) with an adaptive learning rate \( \lambda \).

- **Step 2: Constructing the Final Classifier**
  - Once \( b \) is learned, the constant probability \( c \) is estimated as \( \hat{c} = \frac{1}{1 + b^2} \).
  - Using \( \hat{c} \) and \( g(𝑥) \), the traditional classifier \( p(𝑦 = 1|𝑥) \) is estimated.

#### 6. Assumptions Made by the Method
- **Positive Subdomain Assumption**: The region of highest density of labeled positive samples consists entirely of positive samples, indicating homogeneous positive samples.
- **SCAR Assumption**: The positive labeled samples are selected completely at random from the set of all positive samples, ensuring no bias in the training set.

### Conceptual Explanation
The proposed method addresses the problem of estimating the class prior from positive and unlabeled data by leveraging probabilistic modeling. The modified logistic regression approach allows for a more accurate estimation of the labeling probability, which is constrained by the SCAR assumption. By learning a non-traditional classifier that outputs probabilities within a range of [0, \( c \)], the method can more precisely estimate the likelihood of a sample being labeled positive. This two-step approach first learns the necessary parameters and then constructs the final probabilistic classifier, enabling better performance in scenarios where traditional logistic regression may fall short due to the inherent challenges of positive and unlabeled data.
