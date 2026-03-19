# ML Techniques for Supply Chain Demand Forecasting

## Abstract

1. **Research Problem:** The paper addresses the challenge of forecasting demand in supply chains where full collaboration is hindered, leading to the bullwhip effect due to distorted demand at the end of the supply chain.

2. **Proposed Approach:** The study explores advanced machine learning techniques, specifically neural networks, recurrent neural networks (RNN), and support vector machines (SVM), to predict distorted demand. These are compared against traditional forecasting methods like naïve forecasting, trend analysis, moving average, and linear regression.

3. **Experimental Setup:** Experiments were conducted using two datasets: one from a simulated supply chain and another from actual Canadian Foundries orders.

4. **Key Results:** Recurrent neural networks and support vector machines demonstrated the best performance in forecasting, although the improvement in accuracy was not statistically significant compared to the linear regression model.

5. **Main Contribution:** The main contribution is the comparative analysis showing that while advanced machine learning techniques show promise, traditional regression models still hold competitive accuracy in forecasting distorted demand in supply chains, especially when dealing with limited or distorted information.

## Introduction

### Summary of the Introduction Section

**1. Background Context of the Research Area:**
The paper discusses the growing recognition among firms about the benefits of collaborative forecasting and replenishment (CFAR) across supply chain stakeholders. Despite these initiatives' ability to reduce forecast errors, their implementation remains inconsistent, leading to persistent forecast inaccuracies.

**2. The Main Problem Being Addressed:**
The primary issue addressed is the challenge of forecasting the distorted demand signal in supply chains where full collaboration is not possible. This distortion occurs due to demand signal processing by each member of the supply chain, which transforms the demand signal in a seemingly random manner as it moves up the supply chain.

**3. Limitations of Previous Approaches:**
Previous approaches to demand forecasting, such as moving average, naïve forecasting, and exponential smoothing, induce the bullwhip effect. Even the "1-1" policy without explicit information sharing struggles to maintain accuracy. Advanced techniques like genetic algorithm-based artificial agents have shown some promise but are not widely applicable.

**4. The Research Gap This Paper Identifies:**
The paper identifies a gap in the effective forecasting of distorted demand signals in supply chains lacking full collaboration. There is limited research on leveraging advanced machine learning techniques to improve forecast accuracy under these conditions.

**5. The Core Idea or Hypothesis of the Paper:**
The core idea is that advanced machine learning techniques, including Neural Networks (NN), Recurrent Neural Networks (RNN), and Support Vector Machines (SVM), can effectively forecast the distorted demand signal in supply chains without complete collaboration. These techniques can potentially achieve better forecasting accuracy compared to traditional methods.

**6. The Key Contributions Claimed by the Authors:**
The key contributions claimed by the authors are:
- Demonstrating the applicability of advanced machine learning techniques to improve demand forecasting accuracy in supply chains where full collaboration is not feasible.
- Comparing the performance of these advanced techniques against traditional methods like basic time series analysis.
- Showing how improved forecasting accuracy can lead to cost savings through reduced inventory and increased on-time deliveries, ultimately benefiting customer satisfaction.

## Methodology

### Methodology Summary

The methodology section focuses on advanced machine learning techniques for supply chain demand forecasting, highlighting neural networks, recurrent neural networks (RNNs), and support vector machines (SVMs). Here's a conceptual breakdown of the core elements of these methods:

#### 1. Core Idea of the Proposed Method
The main idea is to utilize advanced machine learning techniques to forecast supply chain demand, which often exhibits complex, non-linear behavior. Traditional linear models like naive forecasts, moving averages, and trend-based approaches are expected to be outperformed by more sophisticated, non-linear models.

#### 2. Model or Algorithm Structure

- **Neural Networks (NNs)**:
  - Composed of layers of interconnected neurons.
  - Input layer, one or more hidden layers, and an output layer.
  - Neurons in each layer pass their output to neurons in the next layer.
  - Universal approximators with sufficient hidden units.

- **Recurrent Neural Networks (RNNs)**:
  - Allow information from the output of some neurons to flow back as input to the same layer or previous layers.
  - Useful for time series data due to their ability to maintain state and learn temporal patterns.
  
- **Support Vector Machines (SVMs)**:
  - Based on structural risk minimization.
  - Projects data into a higher-dimensional space.
  - Maximizes margins between classes or minimizes the error margin for regression.
  - Utilizes kernels (like Radial Basis Function) for non-linear mapping.

#### 3. Key Components or Modules of the System

- **Simulation Model**:
  - Simulates an extended supply chain with multiple parties.
  - Introduces demand signal processing using a linear regression model.
  - Captures delays in order placement and goods delivery.

- **Data Preparation**:
  - Uses daily manufacturer orders from the simulation and actual foundry sales data.
  - Prepares input variables (percentage change in demand over past periods) and output variable (percentage change in demand over the next period).
  - Splits data into training and testing sets for model evaluation.

#### 4. Important Mathematical Formulations (if essential)
- **Neural Networks**:
  - Back-propagation algorithm for training.
  - Error minimization through gradient descent.

- **Recurrent Neural Networks**:
  - Back-propagation through time (BPTT) for training.

- **Support Vector Machines**:
  - Optimization problem to minimize a convex function to find optimal hyperplanes in higher dimensions.

#### 5. Training Procedure or Optimization Approach

- **Neural Networks**:
  - Supervised learning using back-propagation.
  - Training pairs (input-output) used to adjust weights.

- **Recurrent Neural Networks**:
  - Back-propagation through time (BPTT) for training, which allows the network to learn temporal dependencies.

- **Support Vector Machines**:
  - Solves a convex optimization problem to find the best separating hyperplane or margin.

#### 6. Assumptions Made by the Method

- **Neural Networks and RNNs**:
  - Assume sufficient data to train the model and generalize to unseen data.
  - Assume complex, non-linear relationships in demand patterns.

- **Support Vector Machines**:
  - Assume the data can be projected into a higher-dimensional space where a good margin can be found.

Overall, the methodology leverages the advanced capabilities of neural networks, RNNs, and SVMs to model the complex, non-linear nature of supply chain demand patterns, thereby aiming to improve forecasting accuracy over traditional linear methods.

## Results

### Summary of Experimental Results

#### 1. Main Performance Results of the Proposed Method

The proposed neural network models (both feed-forward and recurrent) and the Least Squares Support Vector Machine (LS-SVM) showed competitive performance in forecasting demand for both simulated and foundries data sets.

- **Recurrent Neural Networks (RNN)**: The RNN models exhibited the best performance in terms of Mean Average Error (MAE) on both datasets.
- **LS-SVM**: The LS-SVM performed well, particularly on the training sets, but had some limitations in generalization as seen in the testing set errors.
- **Neural Networks (NN)**: The feed-forward neural networks showed competitive performance but slightly lagged behind RNN and LS-SVM.
- **Multiple Linear Regression (MLR)**: This method outperformed the neural networks on both datasets, suggesting potential overfitting issues with neural networks.
- **Simpler Techniques**: Methods such as moving average, naïve, and trend forecasting were among the worst performers, indicating their inadequacy for complex demand forecasting.

#### 2. Comparison with Baseline Methods

The RNN and LS-SVM generally outperformed other methods in terms of MAE on both datasets. However, statistical tests revealed no significant differences in the accuracy of forecasts among RNN, SVM, NN, and MLR.

- **Simulation Dataset**:
  - RNN: MAE = 447.72
  - LS-SVM: MAE = 453.04
  - MLR: MAE = 453.22
  - NN: MAE = 455.41
  - Naïve: MAE = 520.53
  - Moving Average: MAE = 526.61
  - Trend: MAE = 618.02

- **Foundries Dataset**:
  - RNN: MAE = 20.352
  - LS-SVM: MAE = 20.485
  - MLR: MAE = 21.396
  - NN: MAE = 25.260
  - Moving Average: MAE = 25.481
  - Trend: MAE = 27.323
  - Naïve: MAE = 32.591

#### 3. Key Quantitative Improvements

- The RNN demonstrated better performance in capturing temporal patterns, leading to lower MAE scores compared to other methods.
- The LS-SVM excelled in training set accuracy but showed limitations in generalization.
- The MLR method outperformed NN in both datasets, likely due to neural networks' tendency to overfit.

#### 4. Ablation Studies or Additional Analyses

- The study did not explicitly detail ablation studies but did discuss the potential for neural networks to overfit, which is evidenced by the higher MAE on the test set compared to training set errors for some models.
- The comparison of p-values from t-tests indicated no significant differences in the accuracy of forecasts among RNN, SVM, NN, and MLR.

#### 5. Observations Highlighted by the Authors

- The Recurrent Neural Networks showed superior performance, likely due to their ability to capture temporal dependencies in the data.
- The LS-SVM showed strong training set accuracy but had issues with generalization.
- The Multiple Linear Regression method outperformed neural networks, suggesting that simpler models can sometimes provide more robust performance if not overfitted.
- Simpler forecasting methods like moving average, naïve, and trend forecasting had the highest MAE, indicating their inadequacies for more complex forecasting tasks.
- Statistical analysis showed that while RNN and LS-SVM performed better, the differences in accuracy among RNN, SVM, NN, and MLR were not statistically significant.

This summary encapsulates the key findings and comparative performance of the various forecasting methods tested in the study.

## Conclusion

### Conclusion Summary

1. **Main Achievements**: 
   The research demonstrates that advanced non-linear machine learning techniques, specifically Recurrent Neural Networks (RNN) and Support Vector Machines (SVM), offer more accurate forecasts for distorted demand signals in the extended supply chain compared to traditional methods like linear regression, moving averages, trend estimation, and naïve forecasts.

2. **Key Contributions**:
   - The study provides empirical evidence that machine learning techniques can significantly enhance forecasting accuracy, particularly in real-world foundry data.
   - It highlights the marginal gains from advanced models like RNN and SVM, although these come with higher computational complexity.
   - The research underscores the importance of forecasting accuracy in reducing costs and improving customer satisfaction through timely deliveries, especially in non-collaborative supply chain scenarios.

3. **Limitations Acknowledged**:
   The authors recognize that while advanced techniques showed better results, the improvements over traditional linear regression were not substantial for the simulation dataset. They also note the additional complexity and computational demands of advanced models.

4. **Future Research Directions**:
   The authors suggest future research should explore the impact of information sharing and collaborative forecasting facilitated by e-business technologies. They propose using the current models to incorporate additional supply chain information, which could further improve forecasting accuracy. However, they acknowledge that integration and collaboration constraints remain a challenge, which could potentially be mitigated by their proposed models.
