SELECT * FROM artists
    WHERE
        (artists.age BETWEEN :youngest AND :oldest) AND
        (artists.rate <= :rate) AND
        (haversine(:latitude, :longitude,
                   artists.latitude, artists.longitude) <= :radius)
        ORDER BY artists.rate ASC;
