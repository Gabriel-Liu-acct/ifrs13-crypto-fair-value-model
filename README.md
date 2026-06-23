# IFRS 13 Smart Contract-Bound Valuation Framework

## Project Overview
This repository provides a **Level 3 valuation technical guide** under **IFRS 13 (Fair Value Measurement)** for digital assets subject to rigid smart contract restrictions. 

In traditional financial accounting, public holdings of crypto assets are often measured using Level 1 spot prices (IAS 38 / IFRS 13). However, when assets are locked in smart contracts (e.g., DeFi staking, programmatic vesting, or governance lock-ups), they exhibit severe contractual illiquidity. Directly adopting exchange spot prices overlooks asset-specific restrictions and introduces valuation bubbles.

This framework bridges the gap by translating blockchain code constraints into continuous mathematical boundaries, deriving a precise **Discount for Lack of Marketability (DLOM)** to guide auditors and practitioners.

---

## Theoretical Framework

The framework formalizes smart contract constraints within a filtered probability space ($\Omega$, $\mathcal{F}$, $\lbrace \mathcal{F}\_t \rbrace_{t \ge 0}$, $\mathbb{Q}$), where $\mathbb{Q}$ represents the risk-neutral pricing measure.

### 1. Asset Price Dynamics
To capture the extreme volatility and "flash crash" risks inherent in decentralized protocols, the underlying asset price $S_t$ is modeled via a **Merton Jump-Diffusion Process** adjusted for the continuous staking yield $q$:

$$dS_t = (r - q - \lambda \kappa) S_t dt + \sigma S_t dW_t + S_{t-} dN_t$$

Where:
* $r$: Risk-free interest rate
* $q$: Continuous staking yield/reward rate injected by the protocol
* $\sigma$: Asset volatility calibrated from historical exchange data
* $dN_t$: A Poisson process with intensity $\lambda$, modeling smart contract/protocol shock events

### 2. Conditioning and Stopping Times
* **Deterministic Lock-ups:** For fixed vesting periods, the fair value is projected onto a constrained filtration $\mathcal{F}_t^{\text{restricted}}$ up to maturity $T$.
* **Conditional Unlocking:** For state-dependent contract releases (e.g., TVL thresholds), the maturity is modeled as an $\mathcal{F}_t$-stopping time $\tau$.

The economic loss of liquidity is framed as a lookback option boundary problem, establishing the upper bound of DLOM through the evaluation of conditional expectations $\mathbb{E}^{\mathbb{Q}}[\cdot \mid \mathcal{F}_0]$.

---

## Numerical Implementation

Since the incorporation of jump-diffusion and non-linear liquidation penalty functions yields no closed-form analytical solution, this framework utilizes **Numerical Analysis** to approximate the fair value.

### Methodologies Covered:
1. **Finite Difference Method (FDM):** Solving the governing Partial Integro-Differential Equation (PIDE) backward in time using an implicit-explicit (IMEX) scheme on a standardized $(S, t)$ grid.
2. **Monte Carlo Simulations:** Generating $10^5$ stochastic paths under $\mathbb{Q}$ with variance reduction techniques (Antithetic Variates) to simulate dynamic stopping times $\tau$.

### Expected Output Visualization:
*(Once you run the simulation notebook, your generated 3D sensitivity surface plot will be placed here)*
`[Insert 3D Surface Plot: DLOM vs. Volatility and Lock-up Period]`

---

## Repository Structure

```text
├── data/                   # Calibrated market parameters (BTC, ETH, stETH)
├── models/                 # Core mathematical solvers
│   ├── contract_pde.py     # FDM solver for the valuation PIDE
│   └── stopping_mc.py      # Monte Carlo simulator for stopping times
├── notebooks/              # Interactive laboratory & sensitivity analysis
│   └── valuation_analysis.ipynb
└── README.md
