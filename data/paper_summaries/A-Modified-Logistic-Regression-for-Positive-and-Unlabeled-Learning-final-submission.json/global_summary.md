# A-Modified-Logistic-Regression-for-Positive-and-Unlabeled-Learning-final-submission — Global Summary

### Global Summary

The research addresses the positive and unlabeled (PU) learning problem, a semi-supervised classification challenge where only a subset of positive samples is known, and the rest, including both positive and negative samples, are unlabeled. This issue is particularly relevant in real-world applications where obtaining labeled data is costly or impractical.

The proposed solution introduces a modified logistic regression model with a variable upper bound to improve upon existing probabilistic PU learning algorithms. This two-step approach first estimates the probability of a sample being labeled positive using a non-traditional classifier and then constructs the final probabilistic classifier using an estimated constant probability \( c \).

Experiments on both simulated data and the MNIST dataset demonstrated that the modified logistic regression model outperformed existing methods, achieving an average improvement of over 17% in classification accuracy on the MNIST dataset. The method improved results in 78 out of 81 simulated scenarios (96.3% of the time).

The main contributions of this research include the development of a theoretical approach for PU learning, the introduction of a modified logistic regression model that provides more accurate estimation of the labeling probability, and the demonstration of significant performance improvements in practical applications. This work represents a robust solution to the PU learning problem and has the potential to impact a wide range of applications where labeled data is scarce.
