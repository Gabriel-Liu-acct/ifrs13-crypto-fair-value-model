# Framework for Fair Value Measurement of Crypto Assets under IFRS 13 Level 3 Inputs 

> **Author:** Z. H. Liu  
> **Repository:** [Your GitHub Repository Link]  
> **Status:** Working Paper (Research in Progress)

---

## Abstract
This paper addresses a critical valuation gap in current accounting practices under IFRS 13 (Fair Value Measurement) regarding crypto assets. By bridging numerical analysis, we proposed a Level 3 inputs valuation technical guide with the assumption that the behavior of crypto assets follows american options and euroupean options. The report formulated an alternative measurement for such assets with the consideration of gas fee, providing a prototype with Python programming for reproduction by auditors and relevant researchers.

---

## 1. Introduction
Under the prevailing guidance and practice, crypto assets held by entities are frequently measured and recorded according to the regulations of IAS 38 Intangible Assets. However, crypto assets as smart contracts (i.e. DeFi staking, programmatic vesting schedules, or governance lock-ups) are dynamic and mainly generate income from financial activities. In other words, catagorizing them as intangible assets (i.e. patent, goodwill, or copyrights) that are mostly static and generate income from oprating activities, valuation failure may appear. Such error could eventually causing harm to shareholders' rights of receiving accurate financial information with appropriate disclosures, especially when these two types of assets are not substantially identical or similar. Improving current practices, the research attempted to propose a revised version of Black-Scholes Partial Differencial Equation (B-S PDE) with a new variable *gas* to represent the friction in processing on-chain transcations, corresponds to the gas fees, which details would be further discussed in Section 4. 

The choose of using B-S PDE is considered under few conditions to and the purpose of the research. Firstly, the lack of unified appropriate standards of crypto assets...

---

## 2. Theoretical Framework & Probability Space
To establish immutable mathematical boundaries for smart contract constraints, we formalize the asset dynamics within a filtered probability space ($\Omega$, $\mathcal{F}$, $\lbrace \mathcal{F}\_t \rbrace_{t \ge 0}$, $\mathbb{Q}$), where:
* $\Omega$ represents the sample space containing all possible continuous price paths of the asset.
* $\mathcal{F}$ is the global $\sigma$-algebra representing the collection of all verifiable events up to the terminal horizon.
* $\lbrace \mathcal{F}\_t \rbrace_{t \ge 0}$ defines the filtration, modeling the dynamic flow of market information and data availability over time.
* $\mathbb{Q}$ denotes the risk-neutral probability measure required for fair value expectations under IFRS 13.

The restriction imposed by a smart contract is mathematically framed as a constraint on the holder's filtration space. While the unconstrained market operates on $\mathcal{F}_t^{\text{open}}$, the locked holder's effective action space is projected onto a restricted information set $\mathcal{F}_t^{\text{restricted}} \subset \mathcal{F}_t^{\text{open}}$, rendering the asset non-transferable until a deterministic maturity $T$ or a stochastic stopping time $\tau$.

To capture extreme crypto-market volatility and idiosyncratic protocol shock risks (e.g., smart contract exploits), the underlying asset price $S_t$ is modeled via a modified **Merton Jump-Diffusion Process** adjusted for the continuous on-chain staking yield $q$:

$$dS_t = (r - q - \lambda \kappa) S_t dt + \sigma S_t dW_t + S_{t-} dN_t$$

Where:
* $r$: The risk-free interest rate.
* $q$: The continuous staking yield or programmatic rewards injected back into the contract by the protocol.
* $\sigma$: The annualized asset volatility calibrated from historical exchange data [2].
* $dW_t$: A standard Brownian motion under the risk-neutral measure $\mathbb{Q}$.
* $dN_t$: A Poisson process with intensity $\lambda$, capturing sudden downward price jumps triggered by protocol failures.

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
