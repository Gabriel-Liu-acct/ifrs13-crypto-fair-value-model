# Framework for Fair Value Measurement of Crypto Assets under IFRS 13 Level 3 Inputs 

> **Author:** Z. H. Liu  
> **Repository:** [Your GitHub Repository Link]  
> **Status:** Working Paper (Research in Progress)

---

## Abstract
This paper addresses a critical valuation gap in current accounting practices under IFRS 13 (Fair Value Measurement) regarding crypto assets. By bridging numerical analysis, we proposed a Level 3 inputs valuation technical guide with the assumption that the behavior of crypto assets follows american options and euroupean options. The report formulated an alternative measurement for such assets with the consideration of gas fee, providing a prototype with Python programming for reproduction by auditors and relevant researchers.

---

## 1. Introduction
Under the prevailing guidance and practice, crypto assets held by entities are frequently measured and recorded according to the regulations of IAS 38 Intangible Assets. However, crypto assets as smart contracts (i.e. DeFi staking, programmatic vesting schedules, or governance lock-ups) are dynamic and path-dependent. In other words, catagorizing them as intangible assets (i.e. patent, goodwill, or copyrights) that are mostly static and generate income from oprating activities, substance-form mismatch may appear. Such error could eventually causing harm to shareholders' rights of receiving accurate financial information with appropriate disclosures, using either amortized cost or cost-less-impairment method would significantly underestimate the actual value. Improving current practices, the study attempted to propose a revised version of Black-Scholes Partial Differencial Equation (B-S PDE) with a new variable *gas* to represent the friction in processing on-chain transcations, corresponds to the gas fees, which details would be further discussed in Section 4. In Section 2.2, Section 5, and "measurement.py", Crank-Nicolson Finite Difference Method (C-N FDM) will be introduced as the numerical model for practical usage. 

[IFRS13] While the inputs of the model will be analysed in Section 2.1 are Level 2 inputs, most smart contracts are infeasible to find comparable assets in the market (some may not even be exchanged or traded). The fair value of the smart contracts are dependent to the model estimation would be defined under the standards of Level 3 input. Althought smart contracts are mostly not reconised to be handled under fair value measurement with the exsiting regulations, this study could still be meaningful for analysing more complicated crypto assets. Consider the assumption related to derivatives of the corresponding cryptocurrencies, options in this study, the application of B-S PDE is natrually feasible accordingly. This concept comes from an example when a smart contract is active, it is accounted under the cryptocurrencies assigned when made.

1.1. Applicable Assets to be Studied and Measured  
In this study, the model cannot natrually apply to all kinds of crypto assets, hence it is necassary to mention its limitation in the introduction.
1. The model cannot measure fair value of cryptocurrencies. This is the input of the model.
2. A crypto asset shall have a maturity date, or at least a planned duration of holding the asset.
3. This model can only consider smart contracts behaving similar to options or similar financial derivatives on one cryptocurreny. While the programme provided in "measurement.py" can only process euroupean and american options, it holds space for amendment to all other exotic options and even on more than one cryptocurrencies. 
4. Holding crypto assets with control shall not be considered for fair value measurement.
5. Smart Contracts that are conventional intangible assets in nature (i.e. patent, copyrights) shall consider its economic substance.

---

## 2. Theoretical Framework and Numerical Methods
To establise the formula that is applicable to measure fair value of crypto assets with the assumption associated with options, we may first recall the B-S PDE $\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^{2}S^{2}\frac{\partial^{2} V}{\partial S^{2}} + rS\frac{\partial V}{\partial S} - rV = 0 \space$ with the terminal condition $\forall S, \space V(T, S) = K(S)$, where:
* $V$ represents the option price.
* $S$ represents the asset price.
* $T$ represents the time to maturity.
* $K$ represents the payoff at maturity.
* $\sigma$ is the volitility of the asset.
* $r$ is the risk-free rate.
* $t$ is the time variable.



---

## 3. Numerical Implementation & Discretization
Because the introduction of jump-diffusion operators ($\int$) and non-linear liquidation penalties strips the governing Partial Integro-Differential Equation (PIDE) of any closed-form analytical solution, this framework leverages **Numerical Analysis** to approximate the Level 3 fair value.

### 3.1 Grid Setup and Finite Difference Method (FDM)
We discretize the continuous $(S, t)$ domain into a uniform two-dimensional grid. To guarantee unconditional stability under high-volatility regimes, an Implicit-Explicit (IMEX) finite difference scheme is formulated. 

The terminal boundary condition at contract maturity $t = T$ (or at the evaluation of stopping time $\tau$) forces the restricted asset value to converge perfectly back to the active market spot price:

$$V(S, T) = S$$

The continuous derivatives are approximated via central and backward differences, translating the PIDE into a sequence of linear matrix equations $A \mathbf{V}^{n} = \mathbf{V}^{n+1}$, solved backward in time to solve for the fair value at $t=0$.

The complete, modular Python code implementation for this numerical grid matrix solver can be reviewed directly in our repository:
[`/models/contract_pde.py`](./models/contract_pde.py)

---

## 4. Results and Audit Guidelines
*(To be populated with generated 3D sensitivity surfaces plotting DLOM against Volatility and Lock-up periods, alongside the finalized Valuation Matrix for practitioners).*

---

## References
[?] IFRS Foundation, "IFRS 13 Fair Value Measurement." Accessed: Aug. 13, 2026. [Online]. Available: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-13-fair-value-measurement.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs13/

[?] F. A. Longstaff, “How Much Can Marketability Affect Security Values?,” *J. Finance, vol. 50, no. 5, pp. 1767–1774, Dec. 1995, doi: 10.1111/j.1540-6261.1995.tb05197.x.

[?] R. Moro-Visconti, “Valuing Cryptocurrencies and Digital Assets: Can Value Exist Without Cash Flows?,” *Augmented Corporate Valuation: From Digital Networking to ESG Complience*. Springer Nature Switzerland, pp. 497–529, 2026. doi: 10.1007/978-3-032-17903-6_11. 

[?] E. Beigman et al, “Fair Value Measurement in Inactive Crypto Asset Markets,” *J. Account. Audit. Finance*, vol. 40, no. 1, pp. 241–269, Apr. 2023, doi: 10.1177/0148558x231165557.

[?] L. Clewlow and C. Strickland, *Implementing Derivatives Models*. John Wiley & Sons Ltd, 1998.

[?] L.C.G. Rogers and D. Talay, *Numerical Methods In Finance*. Canbridge University Press, 1997.
