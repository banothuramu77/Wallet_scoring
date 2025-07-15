# Wallet_scoring
Machine learning-based credit scoring system for Aave V2 DeFi wallets, assigning scores from 0–1000 based on historical transaction behavior to detect reliable vs. risky wallet patterns.

## ⚙️ Approach

### Engineered Features

- **Repay ratio**: Measures how much borrowed funds were repaid.
- **Deposit-to-borrow ratio**: Measures conservative vs. risky leverage.
- **Liquidation count**: Penalizes risky wallets.
- **Active longevity**: Number of active days.
- **Transaction frequency**: Total number of transactions.

### Scoring

- Normalize each feature to [0, 1].
- Weighted linear combination:
  - Repay ratio: 30%
  - Deposit-to-borrow: 20%
  - Liquidations penalty: 30%
  - Longevity: 10%
  - Transaction frequency: 10%
- Final score = weighted sum × 1000.

## 💻 How to Run
