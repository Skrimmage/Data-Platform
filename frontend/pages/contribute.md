---
title: Contribute to Skrimmage
---

Add issues or pull requests to the [Skrimmage Data Platform](https://github.com/Skrimmage/Data-Platform/issues)

Things that we are looking for:

- New Data Sources
    - If you have public and open data, that can be added to the [Resources file](https://github.com/Skrimmage/Data-Platform/blob/main/skrimmage/resources.py).
- Data Transformations
    - After the API and Download information is available as a Resource within Dagster, we can create a pipeline that will pull that data. This will go into the [Assets folder](https://github.com/Skrimmage/Data-Platform/tree/main/skrimmage/assets).
- Data Analysis Front-end
    - New SQL queries
        - Lots of the sports pages will reuse the same queries. Those can be stored at the top-level. For example, the [F1 Queries](https://github.com/Skrimmage/Data-Platform/tree/main/frontend/sources/f1) help reduce the need for copying the same queries and allow them to be cached at build time.
    - Markdown pages with Charts and Tables
        - Plenty of examples of this in the [Sports](https://github.com/Skrimmage/Data-Platform/tree/main/frontend/pages/sports) directory. 
