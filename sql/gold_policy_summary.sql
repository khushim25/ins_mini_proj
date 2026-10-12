%sql
CREATE OR REPLACE TABLE workspace.default.gold_policy_summary
USING DELTA
AS
WITH claim_metrics AS (
    SELECT
        policy_id,
        COUNT(*) AS total_claims,
        SUM(claim_amount) AS total_claim_amount,
        AVG(claim_amount) AS avg_claim_amount
FROM workspace.default.silver_claims
GROUP BY policy_id
)

SELECT
    p.policy_id,
    p.customer_id,
    c.name as customer_name,
    c.city,
    c.occupation,
    p.ploicy_type as policy_type,
    p.start_date,
    p.premium,
    COALESCE(cm.total_claims, 0) AS total_claims,
    COALESCE(cm.total_claim_amount, 0) AS total_claim_amount,
    cm.avg_claim_amount
FROM workspace.default.silver_policies p
LEFT JOIN workspace.default.silver_customers c
ON p.customer_id = c.customer_id
LEFT JOIN claim_metrics cm
ON p.policy_id = cm.policy_id;