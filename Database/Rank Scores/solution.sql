SELECT score, DENSE_RANK() OVER (order by score desc) rank FROM scores
order by 2 asc
