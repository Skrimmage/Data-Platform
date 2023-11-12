---
title: Formula One
hide_title: True
---

<h1 class="text-center title">Formula One</h1>

<Links>
    <Link dest="/sports/F1/drivers/" text="Drivers" />
    <Link dest="/sports/F1/races/" text="Races" />
    <Link dest="/sports/F1/circuits/" text="Circuits" />
</Links>

### TODO:
- Add winners instead of Wikipedia link on the index page
- Move that into the detail page
- Add current standings on this page

```sql drivers
select CONCAT(forename, ' ', surname) as name,dob,nationality,url
from 'sources/drivers.csv'
```

---

Data via [Ergast Motor Racing Development API](https://ergast.com/mrd/) for now. It is being deprecated after the 2024 season, and Skrimmage will look into getting the data directly from the FIA in the future. 

