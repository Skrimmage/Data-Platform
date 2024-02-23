---
title: F1 Circuits

---

```sql circuits
select 
    circuitId,
    circuitRef,
    name,
    location,
    country,
    lat,
    lng,
    alt,
    url,
    './' || circuitRef as circuit_link
from f1.circuits;
```

## List of Circuits

<DataTable data="{circuits}" search="true" link=circuit_link>
    <Column id="name" title="Name" />
    <Column id="location" title="Location" />
    <Column id="country" title="Country" />
    <Column id="url" title="Wikipedia" contentType="link" openInNewTab="true" />
</DataTable>

---

{@partial "f1-links.md"}
