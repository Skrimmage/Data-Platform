<Links>
    <Link dest="/sports/F1/drivers/" text="Drivers" />
    <Link dest="/sports/F1/races/" text="Races" />
    <Link dest="/sports/F1/circuits/" text="Circuits" />
</Links>

## All Races

```sql all_races
select *,
'/sports/F1/races/' || year || '_' || REPLACE(name, ' ', '_') as race_link
from 'sources/races.csv'
order by date;
```

<DataTable data="{all_races}" search="true" link=race_link rows=20>
    <Column id="name" title="Name" />
    <Column id="date" title="Date" />
    <Column id="url" title="Wikipedia" contentType="link" openInNewTab="true" />
</DataTable>



