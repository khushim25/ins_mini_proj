-- For every month in claims data, calculate
-- claim_month
-- monthly_claim
-- running_total_claim

WITH cte1 AS (
	 SELECT
		STRFTIME(claim_date, '%Y-%m') AS claim_month,
		SUM(claim_amount) AS monthly_claim
	 FROM claims
	 GROUP BY STRFTIME(claim_date, '%Y-%m')
)

SELECT
	claim_month,
	monthly_claim,
	SUM(monthly_claim) OVER (ORDER BY claim_month) AS running_total_claim
FROM cte1;