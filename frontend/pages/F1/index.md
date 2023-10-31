---
title: F1 Data
---

```sql drivers
select CONCAT(forename, ' ', surname) as name,dob,nationality,url
from 'sources/drivers.csv'
```

```sql competitive_seasons
WITH race_count
     AS (SELECT Count(raceid) num_of_races,
                Max(raceid)   max_race,
                year
         FROM   'sources/races.csv'
         GROUP  BY year),
     race_and_year
     AS (SELECT r.raceid,
                year
         FROM   'sources/races.csv' r),
     top_points
     AS (SELECT ry.raceid,
                Max(Cast(ds.points AS INT)) top_points
         FROM   race_and_year ry,
                'sources/driver_standings.csv' ds
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
                'sources/driver_standings.csv' ds,
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

```

## List of drivers

<DataTable data="{drivers}" search="true">
    <Column id="name" title="Name" />
    <Column id="dob" title="Date Of Birth" />
    <Column id="nationality" title="Nationality" />
    <Column id="url" title="Wikipedia" contentType="link" openInNewTab="true" />
</DataTable>

---

## Most Competitive Seasons

Points is a calculation of the number of drivers within 80%, 90%, and 95% of the leader at each race. A driver being within 5% points of the leader counts as 3, 90%->2 points, 80%->1 point. "Weighted Points" gives more points for it happening later in the season, so a final race clash is weighted more than early races. The race 25% into the season gives 0.25 points per driver, while the last race gives 1 point per driver. This is not a very scientific algorithm, but hopefully it highlights the most exciting seasons in F1 for those who want to go and watch historical seasons on F1TV.

- 2010 was the most competitive season, with 4 drivers potentially taking the championship in the final race. 
- 2012 had 7 different winners in the first 7 races, keeping the pack tight early, and resulting in a tight 2 way battle into the final race. 
- 2021 was a duel between Hamilton and Verstappen, which was tied going into the final race of the season and ending in _spectacular_ fashion. 

<DataTable data="{competitive_seasons}">
    <Column id="year" title="Season" />
    <Column id="points" />
    <Column id="weighted_points" />
</DataTable>

---

Data via [Ergast Motor Racing Development API](https://ergast.com/mrd/) for now. It is being deprecated after the 2024 season, and Skrimmage will look into getting the data directly from the FIA in the future. 