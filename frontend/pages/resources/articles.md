---
title: Sports Analytics Articles
comments: 
    - From https://docs.google.com/spreadsheets/d/1ku4oav1JUB7Qz3ydu1zG-HxkFer19xP_rPkf32SFeP8/edit#gid=0
    -  Extracted links with the following excel/googlesheets:
    - =mid(B2,FIND("~",SUBSTITUTE(B2,CHAR(34),"~",1))+1,(FIND("~",SUBSTITUTE(B2,CHAR(34),"~",2))-FIND("~",SUBSTITUTE(B2,CHAR(34),"~",1)))-1)
---

```metahockey
select * from articles.metahockey_articles_with_links_cleaned;

```

If you have suggestions for articles to add to this repository, please open a [Pull Request](https://github.com/Skrimmage/Data-Platform/tree/main/frontend/sources/articles), or [drop me an email](mailto:danny@skrimmage.com?subject=Articles).

## Hockey Articles

These articles are provided from the [Metahockey](https://metahockey.vercel.app/) archive.

<DataTable data={metahockey} search=true rowShading=true rowLines=false rows=10 link=Link openInNewTab="true">
    <Column id="Title" wrap=true />
    <Column id=Author title="Primary Author(s)" wrap=true />
    <Column id=Year />
    <Column id=Source />
    <Column id=Keywords wrap=true />
</DataTable>

_Note: Click the row to navigate to the article._
