# IFRS 13 Smart Contract-Bound Digital Asset Valuation Framework

> **Author:** Z. H. Liu  
> **Repository:** [Your GitHub Repository Link]  
> **Status:** Working Paper (Research in Progress)

---

## Abstract
This paper addresses a critical valuation bubble in current accounting practices under IFRS 13 (Fair Value Measurement) regarding digital assets locked within rigid smart contract constraints. By bridging measure-theoretic probability with numerical analysis, we propose a Level 3 valuation technical guide. We formalize the economic loss of contractual illiquid assets using a modified jump-diffusion option-pricing framework, providing practitioners and auditors with a mathematically rigorous, reproducible framework for deriving the Discount for Lack of Marketability (DLOM).

---

## 1. Introduction and Accounting Pain Points
Under the prevailing guidance of IFRS 13, crypto-assets held by entities are frequently measured using Level 1 spot prices fetched directly from active exchanges. However, when these assets are programmatically locked within smart contracts (e.g., DeFi staking, programmatic vesting schedules, or governance lock-ups), they exhibit absolute contractual illiquidity. 

Per IFRS 13.B2, a fair value measurement must reflect the characteristics of the asset that market participants would take into account, specifically including asset-specific restrictions. Blindly adopting unadjusted exchange spot prices overlooks these intrinsic legal and algorithmic constraints, creating significant artificial asset bubbles on corporate balance sheets [1]. Because these contract-specific inputs are not readily observable in active markets, the valuation must logically transition from Level 1 to a Level 3 framework.

Traditional quantitative models employed by the "Big 4" audit firms to calculate the Discount for Lack of Marketability (DLOM)—such as the Chaffe or Finnerty models—are wholly adapted from traditional corporate finance [3, 4]. These legacy frameworks fail catastrophically in the Web3 domain, as they cannot account for continuous on-chain staking yields, protocol-level smart contract vulnerabilities, or dynamic unlocking conditions.

---

## 2. Theoretical Framework & Probability Space
To establish immutable mathematical boundaries for smart contract constraints, we formalize the asset dynamics within a filtered probability space $(\Omega, \mathcal{F}, \lbrace \mathcal{F}_t \rbrace_{t \ge 0}, \mathbb{Q})$, where:
* $\Omega$ represents the sample space containing all possible continuous price paths of the asset.
* $\mathcal{F}$ is the global $\sigma$-algebra representing the collection of all verifiable events up to the terminal horizon.
* $\lbrace \mathcal{F}_t \rbrace_{t \ge 0}$ defines the filtration, modeling the dynamic flow of market information and data availability over time.
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

## 📚 References
[1] IFRS Foundation, *IFRS 13 Fair Value Measurement*, International Accounting Standards Board (IASB), 2020.

[2] F. A. Longstaff, "How much can marketability afford to lose? An economic valuation of illiquid assets," *The Journal of Finance*, vol. 50, no. 5, pp. 1767-1774, 1995.

[3] D. B. Chaffe, "Options pricing as a proxy for discounts for lack of marketability," *Business Valuation Review*, vol. 12, no. 4, pp. 182-188, 1993.

[4] J. E. Finnerty, "An average-strike option-pricing model for valuing restricted stock," *The Journal of Derivatives*, vol. 19, no. 4, pp. 43-58, 2012.
