# <Value data={nhl_teams.filter(t => t.triCode === $page.params.triCode)} column=fullName/>

```sql nhl_teams
select *,
'./' || triCode as team_link
from nhl.nhl_teams
```
