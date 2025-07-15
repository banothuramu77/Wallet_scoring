
# 📊 Analysis of Wallet Scores

## Distribution

The plot (`score_distribution.png`) shows score distribution.

### Score Buckets

| Range     | Behavior Summary                                    |
|-------------|------------------------------------------------|
| 0–100   | High risk, repeated liquidations. |
| 100–400 | Aggressive leverage, partial repayments.             |
| 400–700 | Moderate risk, good repayments. |
| 700–900 | Strong repayment, consistent usage. |
| 900–1000 | Highly reliable, conservative borrowing. |

## Observations

- Scores >700 represent disciplined, reliable users.
- Scores <300 often reflect bots or exploitative behavior.

## Future Improvements

- Add token diversity metric.
- Use time-weighted recent behaviors.
- Train ML models in future iterations.
