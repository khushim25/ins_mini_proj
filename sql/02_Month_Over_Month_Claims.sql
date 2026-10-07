-- For every month in the claims data, calculate:

-- month
-- total_claim_amount
-- previous_month_claim_amount
-- month_over_month_change
-- month_over_month_percentage_change 

WITH cte1 as (
	SELECT
		STRFTIME(claim_date, '%Y-%m') as claim_month,
		SUM(claim_amount) as total_claim
	FROM claims
	GROUP BY STRFTIME(claim_date, '%Y-%m')
),

cte2 as (
	SELECT
		claim_month,
		total_claim,
		LAG(total_claim) OVER (ORDER BY claim_month) as previous_month
FROM cte1
)

SELECT 
	claim_month,
	total_claim,
	previous_month,
	(total_claim - previous_month) as mom_change,
	round((mom_change / NULLIF(previous_month, 0)) * 100, 2) as mom_change_pcnt
FROM cte2
ORDER BY claim_month;