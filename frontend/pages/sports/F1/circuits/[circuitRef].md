---
queries:
  - circuits: all_circuits.sql
---

# <Value data={circuits.filter(d => d.circuitRef.toUpperCase() === $page.params.circuitRef.toUpperCase())} column=name/>

<DataTable data="{circuits.filter(d => d.circuitRef.toUpperCase() === $page.params.circuitRef.toUpperCase())}">
    <Column id="name" title="Name" />
    <Column id="location" title="Location" />
    <Column id="country" title="Country" />
    <Column id="url" title="Wikipedia" contentType="link" openInNewTab="true" />
</DataTable>

---

{@partial "f1-links.md"}
