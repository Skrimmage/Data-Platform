---
title: NHL Teams
---

```sql nhl_teams
select *,
'./' || triCode as team_link
from nhl.nhl_teams
```

---

<DataTable data="{nhl_teams}" search="true" link=team_link rows=all>
    <Column id="fullName" title="Name" />
</DataTable>