---
title: F1 Circuits
queries:
  - circuits: all_circuits.sql
---

## List of Circuits

<DataTable data="{circuits}" search="true" link=circuit_link>
    <Column id="name" title="Name" />
    <Column id="location" title="Location" />
    <Column id="country" title="Country" />
    <Column id="url" title="Wikipedia" contentType="link" openInNewTab="true" />
</DataTable>

---

{@partial "f1-links.md"}
