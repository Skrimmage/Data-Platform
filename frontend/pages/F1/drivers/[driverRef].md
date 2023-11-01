---
sources:
  - drivers: f1/drivers.sql
---

# <Value data={drivers.filter(d => d.driverRef.toUpperCase() === $page.params.driverRef.toUpperCase())} column=name/>

<DataTable data="{drivers.filter(d => d.driverRef.toUpperCase() === $page.params.driverRef.toUpperCase())}">
    <Column id="name" title="Name" />
    <Column id="dob" title="Date Of Birth" />
    <Column id="nationality" title="Nationality" />
    <Column id="url" title="Wikipedia" contentType="link" openInNewTab="true" />
</DataTable>
