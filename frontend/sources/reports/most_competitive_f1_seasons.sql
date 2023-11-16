WITH race_count
     AS (SELECT Count(raceid) num_of_races,
                Max(raceid)   max_race,
                year
         FROM   'sources/f1/races.csv'
         GROUP  BY year),
     race_and_year
     AS (SELECT r.raceid,
                year
         FROM   'sources/f1/races.csv' r),
     top_points
     AS (SELECT ry.raceid,
                Max(Cast(ds.points AS INT)) top_points
         FROM   race_and_year ry,
                'sources/f1/driver_standings.csv' ds
         WHERE  ry.raceid = ds.raceid
         GROUP  BY ry.raceid),
     race_breakdowns
     AS (SELECT ry.*,
                Cast(ds.points AS INT)
                   AS points,
                Round(( Cast(ds.points AS FLOAT) / tp.top_points ) * 100, 1)
                   AS percent_points,
                ( Cast(max_race AS FLOAT) - Cast(ry.raceid AS
                FLOAT) ) / rc.num_of_races
                   AS
                percent_race
         FROM   race_and_year ry,
                'sources/f1/driver_standings.csv' ds,
                top_points tp,
                race_count rc
         WHERE  ry.raceid = ds.raceid
                AND ry.raceid = tp.raceid
                AND ry.year = rc.year),
     close_driver_races
     AS (SELECT raceid,
                year,
                Sum(CASE
                      WHEN Cast(percent_points AS FLOAT) > 80 THEN 1
                      ELSE 0
                    END) - 1                    AS close_drivers_80,
                Sum(CASE
                      WHEN Cast(percent_points AS FLOAT) > 90 THEN 1
                      ELSE 0
                    END) - 1                    AS close_drivers_90,
                Sum(CASE
                      WHEN Cast(percent_points AS FLOAT) > 95 THEN 1
                      ELSE 0
                    END) - 1                    AS close_drivers_95,
                percent_race * ( Sum(CASE
                                       WHEN Cast(percent_points AS FLOAT) > 80
                                     THEN 1
                                       ELSE 0
                                     END) - 1 ) AS weighted_close_drivers_80,
                percent_race * ( Sum(CASE
                                       WHEN Cast(percent_points AS FLOAT) > 90
                                     THEN 1
                                       ELSE 0
                                     END) - 1 ) AS weighted_close_drivers_90,
                percent_race * ( Sum(CASE
                                       WHEN Cast(percent_points AS FLOAT) > 95
                                     THEN 1
                                       ELSE 0
                                     END) - 1 ) AS weighted_close_drivers_95
         FROM   race_breakdowns rb
         GROUP  BY raceid, year, percent_race)
SELECT Max(year) as year,
       ( Sum(close_drivers_80)
         + Sum(close_drivers_90)
         + Sum(close_drivers_95) )             points,
       Sum(close_drivers_95),
       Sum(close_drivers_90),
       Sum(close_drivers_80),
       Round(Sum(weighted_close_drivers_95)
             + Sum(weighted_close_drivers_90)
             + Sum(weighted_close_drivers_80)) AS weighted_points,
       Round(Sum(weighted_close_drivers_95)),
       Round(Sum(weighted_close_drivers_90)),
       Round(Sum(weighted_close_drivers_80))
FROM   close_driver_races
GROUP  BY year
ORDER  BY points DESC, weighted_points DESC 