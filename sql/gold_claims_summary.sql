CREATE OR REPLACE TABLE workspace.default.gold_claims_summary
USING DELTA
AS
SELECT
    cl.claim_id,
    cl.policy_id,
    p.customer_id,
    c.name AS customer_name,
    c.city,
    p.ploicy_type,
    p.premium,
    p.start_date,
    p.end_date,
    cl.claim_date,
    cl.claim_type,
    cl.claim_amount,
    cl.claim_status
FROM workspace.default.silver_claims cl
LEFT JOIN workspace.default.silver_policies p
ON cl.policy_id = p.policy_id
LEFT JOIN workspace.default.silver_customers c
ON p.customer_id = c.customer_id;