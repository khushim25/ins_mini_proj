SELECT
  claim_status,
  COUNT(*) AS claim_count
FROM workspace.default.gold_claims_summary
GROUP BY claim_status
ORDER BY claim_count DESC