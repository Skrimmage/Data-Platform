<Links>
    <Link dest="/sports/F1/drivers/" text="Drivers" />
    <Link dest="/sports/F1/races/" text="Races" />
    <Link dest="/sports/F1/circuits/" text="Circuits" />
</Links>

# <Value data={races.filter(r => r.year_race_name === $page.params.year_race_name)} column=name_year/>

```sql races
select *,
year || '_' || REPLACE(name, ' ', '_') as year_race_name,
name || ' - ' || year as name_year,
'./' || year || '_' || REPLACE(name, ' ', '_') as race_link
from 'sources/races.csv'
order by date;
```