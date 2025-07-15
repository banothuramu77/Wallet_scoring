
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data

def process_transactions(data):
    df = pd.DataFrame(data)

    grouped = df.groupby('userWallet')

    wallet_scores = []

    for wallet, g in grouped:
        total_deposit_usd = 0.0
        total_borrow_usd = 0.0
        total_repay_usd = 0.0
        total_liquidations = len(g[g['action'] == 'liquidationcall'])
        num_txns = len(g)
        timestamps = pd.to_datetime(g['timestamp'], unit='s')
        active_days = (timestamps.max() - timestamps.min()).days + 1

        for _, row in g.iterrows():
            amount = float(row['actionData']['amount'])
            price = float(row['actionData']['assetPriceUSD'])
            amount_usd = amount * price

            if row['action'] == 'deposit':
                total_deposit_usd += amount_usd
            elif row['action'] == 'borrow':
                total_borrow_usd += amount_usd
            elif row['action'] == 'repay':
                total_repay_usd += amount_usd

        deposit_to_borrow_ratio = total_deposit_usd / (total_borrow_usd + 1e-5)
        repay_ratio = total_repay_usd / (total_borrow_usd + 1e-5)

        score = (
            0.3 * min(repay_ratio, 1) +
            0.2 * min(deposit_to_borrow_ratio / 2, 1) +
            0.1 * min(active_days / 365, 1) +
            0.1 * min(num_txns / 50, 1) +
            0.3 * (1 - min(total_liquidations / 5, 1))
        )

        final_score = int(score * 1000)

        wallet_scores.append({
            "wallet": wallet,
            "score": final_score,
            "total_deposit_usd": total_deposit_usd,
            "total_borrow_usd": total_borrow_usd,
            "total_repay_usd": total_repay_usd,
            "liquidations": total_liquidations,
            "num_txns": num_txns,
            "active_days": active_days
        })

    return pd.DataFrame(wallet_scores)

def plot_score_distribution(scores_df):
    plt.figure(figsize=(10, 6))
    sns.histplot(scores_df['score'], bins=20, kde=True, color='skyblue')
    plt.title('Wallet Score Distribution')
    plt.xlabel('Score')
    plt.ylabel('Number of Wallets')
    plt.savefig('score_distribution.png')
    plt.close()

if __name__ == "__main__":
    json_file_path = "user-wallet-transactions.json"
    data = load_data(json_file_path)
    scores_df = process_transactions(data)
    scores_df.to_csv("wallet_scores.csv", index=False)
    plot_score_distribution(scores_df)
    print("✅ Scores saved to wallet_scores.csv and plot saved as score_distribution.png")
