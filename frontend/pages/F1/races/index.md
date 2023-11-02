---
title: F1 Races
---

## Current Schedule

```sql current_races
select *,
'./' || year || '_' || REPLACE(name, ' ', '_') as race_link
from 'sources/races.csv'
where year = 2023
order by date;
```

<DataTable data="{current_races}" search="true" link=race_link rows=all>
    <Column id="name" title="Name" />
    <Column id="date" title="Date" />
    <Column id="url" title="Wikipedia" contentType="link" openInNewTab="true" />
</DataTable>