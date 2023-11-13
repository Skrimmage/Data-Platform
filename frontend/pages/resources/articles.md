---
title: Sports Analytics Articles 
---

```metahockey
select * from 'sources/articles/metahockey_articles.csv'
order by Year desc
```

## Hockey Articles

(Will be grabbing adding links soon, but I believe you should be able to find most via Google)

<DataTable data={metahockey} search=true rowShading=true rowLines=false rows=10>
    <Column id=Title wrap=true />
    <Column id="Primary Author(s)" />
    <Column id=Year />
    <Column id=Source />
    <Column id=Keywords wrap=true />
</DataTable>


