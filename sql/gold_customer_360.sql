CREATE OR REPLACE TABLE workspace.default.gold_customer_360
USING DELTA
AS
WITH policy_metrics AS (
    SELECT
        customer_id,
        COUNT(*) AS total_policies,
        SUM(premium) AS total_premium
    FROM workspace.default.silver_policies
    GROUP BY customer_id
),
claim_metrics AS (
    SELECT
        p.customer_id,
        COUNT(cl.claim_id) AS total_claims,
        SUM(cl.claim_amount) AS total_claim_amount
    FROM workspace.default.silver_policies p
    LEFT JOIN workspace.default.silver_claims cl
    ON p.policy_id = cl.policy_id
    GROUP BY p.customer_id
)
SELECT
    c.customer_id,
    c.name,
    c.age,
    c.city,
    c.occupation,
    COALESCE(pm.total_policies, 0) AS total_policies,
    COALESCE(pm.total_premium, 0) AS total_premium,
    COALESCE(cm.total_claims, 0) AS total_claims,
    COALESCE(cm.total_claim_amount, 0) AS total_claim_amount
FROM workspace.default.silver_customers c
LEFT JOIN policy_metrics pm
ON c.customer_id = pm.customer_id
LEFT JOIN claim_metrics cm
ON c.customer_id = cm.customer_id;