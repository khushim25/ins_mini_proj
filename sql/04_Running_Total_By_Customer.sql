-- For each Customer, how much they have claimed cumulatively over time

-- return
-- customer_id,
-- claim_month,
-- monthly_claimcustomer_running_claim

SELECT
	c.customer_id,
	STRFTIME(cl.claim_date, '%Y-%m') as claim_month,
	SUM(cl.claim_amount) as monthly_claim,
	SUM(monthly_claim) OVER( PARTITION BY c.customer_id ORDER BY claim_month) as customer_running_claim
FROM customer c
JOIN policies p
ON c.customer_id = p.customer_id
JOIN claims cl
ON p.policy_id = cl.policy_id
GROUP BY c.customer_id, STRFTIME(cl.claim_date, '%Y-%m')
ORDER BY c.customer_id;