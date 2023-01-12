--  ranks country origins of bands, ordered by the number of (non-unique)  fans
SELECT COUNT(fans) as nb_fans, origin FROM metal_bands GROUP BY origin;
