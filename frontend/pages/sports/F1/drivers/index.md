---
title: F1 Drivers
hide_title: true
sources:
  - drivers: f1/drivers.sql
---

## List of drivers

<DataTable data="{drivers}" search="true" link=driver_link>
    <Column id="name" title="Name" />
    <Column id="dob" title="Date Of Birth" />
    <Column id="nationality" title="Nationality" />
    <Column id="url" title="Wikipedia" contentType="link" openInNewTab="true" />
</DataTable>

---

{@partial "f1-links.md"}