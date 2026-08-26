# Framework for Fair Value Measurement of Crypto Assets under IFRS 13 Level 3 Inputs 

> **Author:** Z. H. Liu  
> **Repository:** [Your GitHub Repository Link]  
> **Status:** Working Paper (Research in Progress)

---

## Abstract
This paper addresses a critical valuation gap in current accounting practices under IFRS 13 (Fair Value Measurement) regarding crypto assets. By bridging numerical analysis, we proposed a Level 3 inputs valuation technical guide with the assumption that the behavior of crypto assets follows american options and euroupean options. The report formulated an alternative measurement for such assets, providing a prototype with Python programming for reproduction by auditors and relevant researchers.

---

## 1. Introduction
[1], [2] Under prevailing practice, crypto assets held by entities are frequently accounted for under IAS 38 Intangible Assets. However, crypto assets in the form of smart contracts (e.g., option receipt, lending receipt, or locked tokens) exhibit dynamic and path-dependent behavior. While many discussions have questioned whether a framework designed for traditional intangible assets (e.g., patent, goodwill, or copyrights) could fully reflect the economic substance of various crypto assets, consensus has not been reached due to a lack of appropriate definitions and methodologies. In particular, this study attempts to provide an alternative method by proposing [3], [4] a revised version of the Black-Scholes Partial Differential Equation (B-S PDE)<sup>1</sup>. Further details are discussed in Section 2. In Section 2.3 and "measurement.py", [3], [4], [5] the Crank-Nicolson Finite Difference Method (C-N FDM)<sup>2</sup> is applied as the numerical model for practical implementation. 

It is worth noting that [1], [2] smart contracts cannot be readily accounted for under fair value measurement with the existing regulations, but the proposed model may remain meaningful for analyzing complex crypto assets and the extension of ideas. While some of the model inputs, which will be analyzed in Section 2.1, [6] are classified as Level 2 inputs under IFRS 13, many smart contracts lack comparable assets in active markets. [6] Their fair value is hence dependent on model estimation and would fall under Level 3 input classification. Consider the assumption related to derivatives of the corresponding cryptocurrencies, particularly options in this study, the application of the B-S PDE could be naturally feasible accordingly. The concept was inspired from an example when a smart contract is active, it is accounted under the cryptocurrencies assigned when made.

### 1.1 Applicable Assets to be Studied and Measured  
The model proposed in this study is not universally applicable to all types of crypto assets. It is therefore necessary to outline its limitation at the outset. The term "smart contract" will refer exclusively to assets that satisfy the following criteria.
1. Standalone cryptocurrencies are excluded from the model's scope. The model requires a cryptocurrency as the underlying asset.  
2. The crypto asset must be held for long term with a fixed holding horizon.
3. This model is designed for smart contracts behaving similarly to options or other financial and non-financial derivatives referencing a single cryptocurrency. 
4. Crypto assets that grant the holder governance rights or influence over the underlying protocol (e.g., governance tokens) are excluded from the model. Such assets may require other valuation methods reflecting their economic substance. 
5. Smart Contracts that are conventional intangible assets in nature (e.g., patents, copyrights) shall consider their economic substance and not suitable for measurement with this model.
 

---

## 2. Valuation Model and Its Numerical Methods 
To establish the formula that is applicable to measure fair value of crypto assets with the assumption associated with options, we may first recall [3], [4] the B-S PDE $BS(V) = \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^{2}S^{2}\frac{\partial^{2} V}{\partial S^{2}} + (r-q)S\frac{\partial V}{\partial S} - rV  \space$ (2.1) with the boundary conditions $BS(V) \le 0, \space V \ge \Phi, \space BS(V) \cdot (V - \Phi) = 0$, where $\Phi$ is the payoff function.
* $t$ denotes the time variable
* $V$ denotes the fair value of the option.
* $S$ denotes the fair value of the underlying asset.
* $\sigma$ denotes the implicit volatility of the asset.
* $r$ denotes the risk-free rate.
* $q$ denotes the dividend yield of the asset. 
* $\Phi$ is the standard payoff function, details explained later.

While in this study, the formula changes to $BS(W) = \frac{\partial W}{\partial t} + \frac{1}{2}\sigma^{2}P^{2}\frac{\partial^{2} W}{\partial P^{2}} + (r-q)P\frac{\partial W}{\partial P} - rW\space$ (2.2) with the boundary conditions $BS(W) \le 0, \space W \ge \hat{\Phi}, \space BS(W) \cdot (W - \hat{\Phi}) = 0$ where:
* $W$ denotes the fair value of the smart contract.
* $P$ denotes the fair value of the cryptocurrency.
* $\hat{\Phi}$ is the economic value function to the entity holding the smart contract at the maturity, details explained later.
* All other variables not mentioned have very similar properties to the original B-S PDE.

[3], [4] In formula (2.1), $\Phi$ denotes the standard payoff function for an option, defined as $(S-K)^{+}$ for call options (and $(K-S)^{+}$ for put options), where $K$ is the contractually fixed strike price. 

In formula (2.2), the payoff function is generalized to $\hat{\Phi}$, defined as $(S-\hat{K})^{+}$ for call options, where $\hat{K}$ replaces the conventional strike price $K$ and represents the expected economic benefit derived from the smart contracts at maturity. Unlike the fixed K in the standard framework, $\hat{K}$ is a firm-specific estimate, to be determined in accordance with related accounting and legal standards.

The interpretation of $\hat{K}$ is context-dependent. For a lending receipt that entitles the holder to services from a DAO entity, $\hat{K}$ corresponds to the expected economic value of those services by maturity. For contracts that obligate the return of a specified cryptocurrency amount, the expected cryptocurrency amount should be converted into its equivalent fiat value by maturity. Under all circumstances, $\hat{K}$ should remain expressed in the same currency unit as $S$. 

---

## 3. Numerical Implementation
In this study, Crank-Nicolson Finite Difference Method would be applied for the numerical implementation. Meanwhile, explanation of the numerical convergence and the accompanying program would be elabourated.

### 3.1 Crank-Nicolson Finite Difference Method


### 3.2 Concepts of Convergence


### 3.3 Program Explanation

---

## 4. Sensitivity Test
*(To be processed).*


---

## 5. Limitation of the Study
*(To be processed).*




<sup>1</sup> (Denotes for B-S PDE)
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

