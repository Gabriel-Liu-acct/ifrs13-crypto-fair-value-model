# Framework for Fair Value Measurement of Crypto Assets under IFRS 13 Level 3 Inputs 

> **Author:** Z. H. Liu  
> **Repository:** [Your GitHub Repository Link]  
> **Status:** Working Paper (Research in Progress)

---

## Abstract
This paper addresses a critical valuation gap in current accounting practices under IFRS 13 (Fair Value Measurement) regarding crypto assets. By bridging numerical analysis, we proposed a Level 3 inputs valuation technical guide with the assumption that the behavior of crypto assets follows american options and euroupean options. The report formulated an alternative measurement for such assets with the consideration of gas fee, providing a prototype with Python programming for reproduction by auditors and relevant researchers.

---

## 1. Introduction
[1], [2] Under prevailing practice, crypto assets held by entities are frequently accounted for under IAS 38 Intangible Assets. However, crypto assets in the form of smart contracts (i.e. DeFi staking, programmatic vesting schedules, or governance lock-ups) exhibit dynamic and path-dependent behaviour. While many discussions have questioned whether a framework designed for traditional intangible assets (i.e. patent, goodwill, or copyrights) could fully reflect the economic substance of various crypto assets, consensus has not been reached due to a lack of approriate definitions and methodologies. In particular, this study attempts to provide an alternative method by proposing [3], [4] a revised version of the Black-Scholes Partial Differencial Equation (B-S PDE) with a new variable *g* to represent the consideration of gas fees during processing on-chain transcations. Further details are discussed in Section 2. In Section 2.3 and "measurement.py", [3], [4], [5] the Crank-Nicolson Finite Difference Method (C-N FDM) is applied as the numerical model for practical implementation. 

It is worth noting that [1], [2] smart contracts cannot be readily accounted for under fair value measurement with the exsiting regulations, but the proposed model may remains meaningful for analysing complex crypto assets and the extension of ideas. While the model inputs, which will be analysed in Section 2.1, [6] are classified as Level 2 inputs under IFRS 13, many smart contracts lack comparable assets in active markets. [6] Their fair value is hence dependent on model estimation and would fall under Level 3 input classification. Consider the assumption related to derivatives of the corresponding cryptocurrencies, particularly options in this study, the application of the B-S PDE could be natrually feasible accordingly. The concept was inspired from an example when a smart contract is active, it is accounted under the cryptocurrencies assigned when made.

### 1.1 Applicable Assets to be Studied and Measured  
In this study, the model cannot natrually apply to all kinds of crypto assets, hence it is necassary to mention its limitation in the introduction, the phrase "smart contract" in the following discussion of this report will follow this set of limitations.
1. The model cannot measure fair value of cryptocurrencies. This is the input of the model.
2. A crypto asset shall have a maturity date, or at least a planned duration of holding the asset.
3. This model can only consider smart contracts behaving similar to options or similar financial derivatives on one cryptocurreny. While the programme provided in "measurement.py" can only process euroupean and american options, it holds space for amendment to all other exotic options and even on more than one cryptocurrencies. 
4. Holding crypto assets with control shall not be considered for fair value measurement.
5. Smart Contracts that are conventional intangible assets in nature (i.e. patent, copyrights) shall consider its economic substance, which may not be applicable to the model.

---

## 2. Valuation Model and Its Numerical Methods
In this section, it will first introduce the modification of B-S PDE to the condition of smart contracts. Followed by the explaination of theoretical numerical methods.

### 2.1 Theoretical Framwork for the Modification
To establise the formula that is applicable to measure fair value of crypto assets with the assumption associated with options, we may first recall [3], [4] the B-S PDE $BS(V) = \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^{2}S^{2}\frac{\partial^{2} V}{\partial S^{2}} + (r-q)S\frac{\partial V}{\partial S} - rV  \space$ (2.1) with the boundary conditions $BS(V) \le 0, \space V \ge \Phi, \space BS(V) \cdot (V - \Phi) = 0$, where $\Phi$ is the payoff fuction.

While in this study, the formula changes to $BS(W) = \frac{\partial W}{\partial t} + \frac{1}{2}\sigma^{2}P^{2}\frac{\partial^{2} W}{\partial P^{2}} + (r-q)P\frac{\partial W}{\partial P} - rW\space$ (2.2) with the boundary conditions $BS(W) \le 0, \space W \ge (\hat{\Phi} - g(\sigma)), \space BS(W) \cdot (W - \hat{\Phi} + g(\sigma)) = 0$ where:
* $W$ represents the fair value of the smart contract.
* $P$ represents the fair value of the cryptocurrency.
* $g(\sigma)$ represents the gas fee, explained in Section 3.
* $\hat{\Phi}$ represents the economic value function to the entity holding the smart contract at the maturity, details explained later.
* all other variables not mentioned have very similar properties to the original B-S PDE.

[3], [4] In formula 2.1, $\Phi$ is a simple payoff function $(S-K)^{+}$, which $K$ is the strike price of the option, assuming call options. In formula 2.2, $\hat{\Phi}$ becomes an economic value function defined as $(S-\hat{K})$

### 2.2 Theory behind the Numerical Methods


---

## 3. Studies on Gas Fee
In this section, the issues of gas fee are elabourated with respect to the assumptions, limitations, correlation studies, and the simple model concluded.
For the ease of elabouration, the general gas fee function is given in pesudo-code form to provide an intuition for understandings: Gas Fee = Gas Used $\times$ (Base Fee + Priority Fee). In most cases, the unit of gas used is deterministic as it represent the number of computational steps of each execution. Hence, the part worth studying would be the term (Base Fee + Priority Fee) as the actual variable of the final gas fee. Base fee is the minimum price programmed to adjust according to the level of congestion in the network, and priority fee is an optional fee to speed up the execution. In this study, both base and priority fees are assumed to be considered. 

### 3.1 Explanation of Gas Fee Function
For the $g(\sigma)$, this is an extra dummy variable compare to the equation 2.1. It represents the base fee plus priority fee to be amplified if you choose to execute the smart contract at time t with the corresponding volitility of the cryptocurrency. As gas fee acts similar to a commission fee in practice, it should not be affecting the B-S PDE itself but the boundary conditions. While it is stated that time is one of the factor should be considered to valuate the gas fee, the model did not include the variable. The reason is when the affect of time is considerated, gas fee shall be stocastic in nature and expressed in stochastic differential equation. However, such equations are very difficult to audit as random process cannot be assumped or neglected under numerical simulations. A more feasible alternative model would be using regression analysis to estimate such gas fee deterministically, and project the affect of time onto the volitility $\sigma$ which sensitivity could be test under usual accounting practice. 

---

## 4. Numerical Implementation


### 4.1 Crank-Nicolson Finite Difference Method


### 4.2 Concepts of Convergence

---

## 5. Sensitivity Test
*(To be processed).*

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

