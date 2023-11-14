---
title: Most Competitive F1 Seasons
sources:
  - competitive_seasons: reports/most_competitive_f1_seasons.sql
---

Points is a calculation of the number of drivers within 80%, 90%, and 95% of the leader at each race. A driver being within 5% points of the leader counts as 3, 90%->2 points, 80%->1 point. "Weighted Points" gives more points for it happening later in the season, so a final race clash is weighted more than early races. The race 25% into the season gives 0.25 points per driver, while the last race gives 1 point per driver. This is not a very scientific algorithm, but hopefully it highlights the most exciting seasons in F1 for those who want to go and watch historical seasons on F1TV.

- 2010 was the most competitive season, with 4 drivers potentially taking the championship in the final race. 
- 2012 had 7 different winners in the first 7 races, keeping the pack tight early, and resulting in a tight 2 way battle into the final race. 
- 2021 was a duel between Hamilton and Verstappen, which was tied going into the final race of the season and ending in _spectacular_ fashion. 

<DataTable data="{competitive_seasons}">
    <Column id="year" title="Season" />
    <Column id="points" />
    <Column id="weighted_points" />
</DataTable>

<script>
console.log('https://github.com/Skrimmage/Data-Platform/tree/main/frontend/pages' + $page.route['id'] + '/index.md')
</script>