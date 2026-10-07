-- For each custome, return:
-- -> customer_id
-- -> name 
-- -> total number of policies
-- -> total number of claims
-- -> total claim amount
-- -> average claim amount

-- Include customers who have never made a claim.

SELECT
	c.customer_id,
	c.name,
	COUNT(DISTINCT p.policy_id) as policy_count,
	COUNT(cl.claim_id) as claim_count,
	COALESCE(SUM(cl.claim_amount), 0) as total_claim,
	ROUND(AVG(cl.claim_amount), 2) as avg_claim,
FROM customer c
LEFT JOIN policies p
ON c.customer_id = p.customer_id
LEFT JOIN claims cl
ON p.policy_id = cl.policy_id
GROUP BY c.customer_id, c.name
ORDER BY c.customer_id;

