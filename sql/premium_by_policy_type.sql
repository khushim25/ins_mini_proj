SELECT
  policy_type,
  SUM(premium) AS total_premium
FROM workspace.default.gold_policy_summary
GROUP BY policy_type
ORDER BY total_premium DESC