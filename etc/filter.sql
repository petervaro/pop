SELECT artists.uuid,
       artists.gender,
       artists.age,
       artists.rate,
       artists.longitude,
       artists.latitude,
       haversine(:latitude, :longitude,
                 artists.latitude, artists.longitude) AS distance FROM artists
    WHERE artists.rate <= :rate AND
          artists.age BETWEEN :youngest AND :oldest AND
          distance <= :radius
    ORDER BY :age_rank * artists.age +
             :gender_rank * artists.gender +
             :rate_rank * artists.rate +
             :distance_rank * distance ASC
    LIMIT :count OFFSET :start
