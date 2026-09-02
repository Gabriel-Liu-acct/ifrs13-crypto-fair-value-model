# Framework for Fair Value Measurement of Crypto Assets under IFRS 13 with Level 3 Inputs 

> **Author:** Z. H. Liu  
> **Repository:** [Your GitHub Repository Link]  
> **Status:** Working Paper (Research in Progress)

---

## Abstract
This paper addresses a critical valuation gap in current accounting practices under IFRS 13 (Fair Value Measurement) regarding crypto assets. By bridging numerical analysis, we proposed a Level 3 inputs valuation technical guide with the assumption that the behavior of crypto assets follows american options and euroupean options. The report formulated an alternative measurement for such assets, providing a prototype with Python programming for reproduction by auditors and relevant researchers.

---

## 1. Introduction
[1], [2] Under prevailing practice, crypto assets held by entities are frequently accounted for under IAS 38 Intangible Assets. However, crypto assets in the form of smart contracts (e.g., option receipt, lending receipt, or locked tokens) exhibit dynamic and path-dependent behavior. While many discussions have questioned whether a framework designed for traditional intangible assets (e.g., patent, goodwill, or copyrights) could fully reflect the economic substance of various crypto assets, consensus has not been reached due to a lack of appropriate definitions and methodologies. In particular, this study attempts to provide an alternative method by proposing [3], [4] a revised version of the Black-Scholes-Merton (BSM) model<sup>1</sup>. Further details are discussed in Section 2. In Section 2.3 and "measurement.py", [3], [4], [5] the Crank-Nicolson Finite Difference Method (C-N FDM)<sup>2</sup> is applied as the numerical model for practical implementation. 

It is worth noting that [1], [2] smart contracts cannot be readily accounted for under fair value measurement with the existing regulations. Nevertheless, the proposed model offers a meaningful approach for analyzing complex crypto assets and for extending current valuation methodologies. [6] In the absence of active market, fair value measurement for such assets depends on model-based estimation and therefore falls under IFRS 13 Level 3 input classification. Given that these smart contracts often exhibit economic characteristics similar to derivatives referencing the underlying cryptocurrencies, particularly options in this study, the application of the BSM model becomes a natural and feasible starting point for valuation. The analogy is inspired by the observation that when a smart contract is active, its value is economically linked to the cryptocurrencies assigned.

### 1.1 Applicable Assets to be Studied and Measured  
The model proposed in this study is not universally applicable to all types of crypto assets. It is therefore necessary to outline its limitation at the outset. The term "smart contract" will refer exclusively to assets that satisfy the following criteria.
1. Standalone cryptocurrencies are excluded from the model's scope. The model requires a cryptocurrency as the underlying asset.  
2. The crypto asset must be held for long term with a fixed holding horizon.
3. This model is designed for smart contracts behaving similarly to options or other financial and non-financial derivatives referencing a single cryptocurrency. 
4. Crypto assets that grant the holder governance rights or influence over the underlying protocol (e.g., governance tokens) are excluded from the model. Such assets may require other valuation methods reflecting their economic substance. 
5. Smart Contracts that are conventional intangible assets in nature (e.g., patents, copyrights) shall consider their economic substance and not suitable for measurement with this model.
 

---

## 2. Valuation Model 
In this section, rational for modifying the conventional American option BSM for the application in smart contracts will be elaborated. 

### 2.1 Model Modification
To establish the model that is applicable to measure fair value of smart contracts with the assumption associated with options, we may first recall the BSM model [3], [4]: $L(V) = \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^{2}S^{2}\frac{\partial^{2} V}{\partial S^{2}} + (r-q)S\frac{\partial V}{\partial S} - rV  \space$ (2.1) with the complementarity conditions $L(V) \le 0, \space V \ge \Phi, \space L(V) \cdot (V - \Phi) = 0$ (2.1a), where $\Phi$ is the payoff function. Note that $L(\cdot)$ denotes the Black-Scholes differential operator but not a function.  
* $t$ denotes the time variable
* $V$ denotes the fair value of the option.
* $S$ denotes the fair value of the underlying asset.
* $\sigma$ denotes the implicit volatility of the asset.
* $r$ denotes the risk-free rate.
* $q$ denotes the dividend yield of the asset. 
* $\Phi$ is the standard payoff function, details explained later.

While in this study, the model changes to $L(W) = \frac{\partial W}{\partial t} + \frac{1}{2}\sigma^{2}P^{2}\frac{\partial^{2} W}{\partial P^{2}} + (r-q)P\frac{\partial W}{\partial P} - rW\space$ (2.2) with the complementarity conditions $L(W) \le 0, \space W \ge \hat{\Phi}, \space L(W) \cdot (W - \hat{\Phi}) = 0$ (2.2a) where:
* $W$ denotes the fair value of the smart contract.
* $P$ denotes the fair value of the cryptocurrency.
* $\hat{\Phi}$ is the economic value function to the entity holding the smart contract at the maturity, details explained later.
* All other variables not mentioned have very similar properties to the original BSM model.

### 2.2 Explanation of Changes in Variables
This subsection provides essential explanation towards the changed variables from (2.1) to (2.2). 

#### 2.2.1 Modification in Underlying Assets
The most significant difference to the variable set is the replacement of conventional underlying asset price $S$ with the cryptocurrency price $P$. The payoff of these smart contracts is economically referenced to the price of a specific cryptocurrency. Hence, the cryptocurrency price serves as the primary driver of the contract value, analogous to the role of the underlying assets in traditional financial markets. Emphasizing the auditability of the model, the value of $P$ is observable on public exchanges, owing to the maturity of centralized cryptocurrencies exchanges and their associated data infrastructure. [6] This satisfies the market participant assumption requirement for fair value measurement inputs, and such substitution is therefore economically grounded and practically feasible. 

#### 2.2.2 Standard Payoff Function
As stated in (2.1a), $\Phi$ denotes the standard payoff function for an option, defined as $(S-K)^{+}$ for call options (and $(K-S)^{+}$ for put options), where $K$ is the contractually fixed strike price. 

In (2.2a), the payoff function is generalized to $\hat{\Phi}$, defined as $(P-\hat{K})^{+}$, where $\hat{K}$ replaces the conventional strike price $K$ and represents the expected economic benefit derived from the smart contracts at maturity. Unlike the fixed $K$ in the standard framework, $\hat{K}$ is a firm-specific estimate, to be determined in accordance with related accounting and legal standards.

The interpretation of $\hat{K}$ is dependent to its context. For a lending receipt entitling the holder to services from a DAO entity, $\hat{K}$ corresponds to the expected economic value of those services by maturity. For contracts that obligate the return of a specified cryptocurrency amount, the expected cryptocurrency amount should be converted into its equivalent fiat value at maturity. Under all circumstances, $\hat{K}$ should remain expressed in the same currency unit as $P$. It is also noteworthy that basis of $\hat{K}$ and $P$ should remain consistent: when $\hat{K}$ represents the strike price, $P$ should be expressed as the price per unit of the cryptocurrency; when $\hat{K}$ represents the total expected economic value, $P$ should be expressed as the total value of cryptocurrency position. 

---

## 3. Numerical Model
This section elaborates on the logic of the program, variables used in the program, and the numerical robustness. For a better understanding, please refer to the accompanying program "Measurement.py"

### 3.1 Program Logic
The program implements C-N FDM for the numerical solution of the BSM model. The major reason is that C-N FDM is the most suitable numerical method for auditability. Firstly, C-N FDM does not require any assumption related to computation itself, such as assumption of probability measures in trinomial tree. Secondly, unlike Monte Carlo simulations which actual results depend on randomly generated numbers, the computation using C-N FDM is deterministic. 

The program applies logarithmic transformation to the price grid, which upper and lower bounds of the computational domain are determined with reference to the initial the cryptocurrency price $P$ in (2.2). One advantage of the log-normal distribution assumption is that negative asset values are excluded under normal circumstances, and the valuation output is not affected by this assumption in theory.  

The program is designed to process smart contracts under assumption of either European or American exercise style. Although the current implementation is limited to vanilla option analogs, its structure does not preclude extension of idea to exotic options, such as Asian option or lookback options. 

### 3.2 Variable Explanation
For intuitive understanding, the variables used in the program follows conventional notations as (2.1). In substance, the program computes the numerical solution of the BSM model. Users shall ensure that the inputs they provide correspond to the intended economic interpretation. 

#### 3.2.1 Variables in BSM Model
The program display input prompts for each variable. However, in case of confusion, the following mappings clarify the correspondence between the program's variable names and notation in (2.2): 
* $S$ in the program refers to $P$
* $K$ in the program refers to $\hat{K}$ in $\hat{\Phi}$ as at (2.2a)
* $div$ in the program refers to $q$
* $sig$ in the program refers to $\sigma$

#### 3.2.2 Variables Exclusive for Computation
In addition to the economic inputs, the program requires several parameters for computation, including: the number of time steps $N$; the number of price steps $N_j$; and the grid spacing $dx$. These parameters do not correspond to any economic variables but are essential for the implementation of C-N FDM. They also play a critical role in Subsection 3.3. Users shall select these parameters considering numerical stability and processing power. 

Certain lists used in the program also carry useful economic information for auditing purposes. Although printing those as output is not available in the original version of "Measurement.py", users may adjust the code for their own purposes. Some noteworthy examples are: 
* $apm$ represents the list of asset prices for the price grid, sequenced in ascending order.
* $ovm$ represents the list of option values to the corresponding asset prices, sequenced correspondingly to $apm$. Note that this list is updated iteratively during calculation; please refer to the code for details.

### 3.3 Robustness and Convergence Testing
In this subsection, the robustness and convergence of the program are tested for actual usage. In this test, input of $N$ and $N_j$ are set to the same value, with $N_j \times dx = 1$. Note that the actual number of price grids would be $2 N_j +1$. For instance, please refer to the appendix.

According to the appendix, the program is able to process large grid numbers in reasonable amounts of time. It is observed that when $N$ and $N_j$ grow larger under the aforementioned setting, the error converges to approximately -0.091% to the analytical value. Despite the immaterial error, such computational error could be improved by setting $N_j \times dx = 3$ in practice, exact value has to be analyzed case by case. Additionally, the computational time increases approximatly exponentially as the grid size increases. While the numerical accuracy did not improve significantly after $N = 1000$ under this setting, users shall consider available computational resources before increasing $N$ or $N_j$. 

Note that $dx$ is the discretization of continuous differential to asset price in numerical analysis, users shall determine the optimal value for better numerical approximation. When $dx$ is greater than optimum, error from discretization becomes significant; when $dx$ is smaller than optimum, error from truncation becomes significant. 

---

## 4. Sensitivity Analysis
*(To be processed).*


---

## 5. Scope and Limitations
*(To be processed).*




<sup>1</sup> (Denotes for BSM model)
<sup>2</sup> (Denotes for C-N FDM)

---

## References
[1] International Financial Reporting Interpretations Committee, "Holdings of Cryptocurrencies—Agenda decision to finalise," IFRS, London, United Kingdom, June 2019. Accessed Jul.20, 2026. [Online]. Available: https://www.ifrs.org/news-and-events/updates/ifric/2019/ifric-update-march-2019/#1

[2] Financial Accounting Standard Board and International Accounting Standard Board, "FASB | IASB Joint Education Meeting: Accounting for and Disclosure of Crypto Assets (Agenda Paper 12A)" FASB, Norwalk, CT, USA. Accessed: Jul. 20, 2026. [Online]. Available: https://www.ifrs.org/content/dam/ifrs/meetings/2022/september/fasb-iasb/ap12a-digital-assets-fasb-accounting-for-and-disclosure-of-crypto-assets-project-update.pdf

[3] L.C.G. Rogers and D. Talay, *Numerical Methods In Finance*. Canbridge University Press, 1997.

[4] L. Clewlow and C. Strickland, *Implementing Derivatives Models*. John Wiley & Sons Ltd, 1998.

[5] Crank and Nicolson

[6] IFRS Foundation, "IFRS 13 Fair Value Measurement." Accessed: Aug. 13, 2026. [Online]. Available: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-13-fair-value-measurement.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs13/

[?] F. A. Longstaff, “How Much Can Marketability Affect Security Values?” *J. Finance, vol. 50, no. 5, pp. 1767–1774, Dec. 1995, doi: 10.1111/j.1540-6261.1995.tb05197.x.

[?] R. Moro-Visconti, “Valuing Cryptocurrencies and Digital Assets: Can Value Exist Without Cash Flows?” *Augmented Corporate Valuation: From Digital Networking to ESG Complience*. Springer Nature Switzerland, pp. 497–529, 2026. doi: 10.1007/978-3-032-17903-6_11. 

[?] E. Beigman et al, “Fair Value Measurement in Inactive Crypto Asset Markets,” *J. Account. Audit. Finance*, vol. 40, no. 1, pp. 241–269, Apr. 2023, doi: 10.1177/0148558x231165557.

