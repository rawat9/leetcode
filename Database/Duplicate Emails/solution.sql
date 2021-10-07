SELECT Email
FROM (
		SELECT Email,
			COUNT(email) AS cnt
		FROM Person
		GROUP BY 1
	) a
WHERE cnt > 1