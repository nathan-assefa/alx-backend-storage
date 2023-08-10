-- Listing bands via their lifespan
-- and order them in descending order
SELECT band_name, IFNULL(split, 2022) - formed
AS lifespan from metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
