---
queries:
  - drivers: all_drivers.sql
---


# <Value data={drivers.filter(d => d.driverRef.toUpperCase() === $page.params.driverRef.toUpperCase())} column=name/>

<DataTable data="{drivers.filter(d => d.driverRef.toUpperCase() === $page.params.driverRef.toUpperCase())}">
    <Column id="dob" title="Date Of Birth" />
    <Column id="nationality" title="Nationality" />
    <Column id="url" title="Wikipedia" contentType="link" openInNewTab="true" />
</DataTable>

<BigValue
  data={driver_wins.filter(dw => dw.driverRef === $page.params.driverRef)}
  value='wins'
/>

<BigValue
  data={driver_podiums.filter(dw => dw.driverRef === $page.params.driverRef)}
  value='podiums'
/>

<BigValue
  data={driver_points.filter(dw => dw.driverRef === $page.params.driverRef)}
  value='points'
/>

---

{@partial "f1-links.md"}

```results
select 
  *
from f1.results
```

```driver_cross_results
select 
  d.driverId,
  d.driverRef,
  r.positionOrder,
  r.points
from ${drivers} d
LEFT OUTER JOIN ${results} r
ON r.driverId = d.driverId
```

```driver_wins
select 
  sum(CASE WHEN positionOrder = 1 then 1 else 0 END) as wins,
  driverId,
  driverRef
from ${driver_cross_results} 
group by driverId, driverRef
order by wins desc
```

```driver_podiums
select 
  sum(CASE WHEN positionOrder <= 3 then 1 else 0 END) as podiums,
  driverId,
  driverRef
from ${driver_cross_results} 
group by driverId, driverRef
order by podiums desc
```

```driver_points
select 
  sum(CAST(points as decimal)) as points,
  driverId,
  driverRef
from ${driver_cross_results} 
group by driverId, driverRef
order by points desc
```