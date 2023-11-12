---
title: F1 Drivers
hide_title: true
sources:
  - drivers: f1/drivers.sql
---
<Links>
    <Link dest="/sports/F1/drivers/" text="Drivers" />
    <Link dest="/sports/F1/races/" text="Races" />
    <Link dest="/sports/F1/circuits/" text="Circuits" />
</Links>

## List of drivers

<DataTable data="{drivers}" search="true" link=driver_link>
    <Column id="name" title="Name" />
    <Column id="dob" title="Date Of Birth" />
    <Column id="nationality" title="Nationality" />
    <Column id="url" title="Wikipedia" contentType="link" openInNewTab="true" />
</DataTable>
