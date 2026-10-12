SELECT
  policy_type,
  COUNT(*) AS policy_count
FROM workspace.default.gold_policy_summary
GROUP BY policy_type
ORDER BY policy_count DESC