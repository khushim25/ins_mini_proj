SELECT
  city,
  COUNT(*) AS total_customers
FROM workspace.default.gold_customer_360
GROUP BY city
ORDER BY total_customers DESC