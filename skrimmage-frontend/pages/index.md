---
title: Welcome to Evidence
---

_Build polished data products with SQL and Markdown_

## Write in Markdown

Evidence renders markdown files into web pages. This page is:
`[project]/pages/index.md`.

## Run SQL using Code Fences

```sql driver_query
select
  *
from drivers
```

In your markdown file, you can include SQL queries in code fences. Evidence will run these queries through your database and return the results to the page.

To see the queries on a page, click the 3-dot menu at the top right of the page and Show Queries. You can see both the SQL and the query results by interacting with the query above.

### Data Table

<DataTable data={driver_query} rows=10/>

> **More:** See [all components](https://docs.evidence.dev/components/all-components)

# Share with Evidence Cloud

Evidence Cloud is the easiest way to securely share your project. 
- Get your project online
- Authenticate users
- Schedule data refreshes

  <BigLink href='https://du3tapwtcbi.typeform.com/waitlist?utm_source=cloud-page&typeform-source=evidence.dev'>Deploy to Evidence Cloud &rarr;</BigLink>

You can use Netlify, Vercel or another static hosting provider to [self-host Evidence](https://docs.evidence.dev/deployment/overview).

# Get Support

- Message us on [Slack](https://slack.evidence.dev/)
- Read the [Docs](https://docs.evidence.dev/)
- Open an issue on [Github](https://github.com/evidence-dev/evidence)
