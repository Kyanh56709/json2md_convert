# Cách dùng repo để convert json to MD

## 1. Clone repo
## 2. Cài dependencies
```bash
npm install
```

## 3. Cách chạy
```bash
npm run convert my-articles.json
```

Template json
```json
[
{
  "title": "Article Title",
  "url": "https:\/\/www.hust.edu.vn\/something_here",
  "author": {
    "name": "Author Name",
    "bio": "Author bio or description",
    "email": "author@example.com"
  },
  "date_published": "2024-07-30",
  "content": "This is the main HTML content of the article.",
  "summary": "This is a brief summary of the article.",
  "categories": [
    "category1",
    "category2"
  ],
  "tags": [
    "tag1",
    "tag2",
    "tag3"
  ],
  "keywords": [
    "keyword1",
    "keyword2",
    "keyword3"
  ],
  "related_articles": [
    {
      "title": "Related Article 1",
      "link": "https://example.com/related-article-1"
    },
    {
      "title": "Related Article 2",
      "link": "https://example.com/related-article-2"
    }
  ]
}
]
```




