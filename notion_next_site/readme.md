# site with notion

https://samuelkraft.com/blog/building-a-notion-blog-with-public-api

create an account in notion and get the token from one of the integration

https://www.notion.so/my-integrations/internal/0c734823d83f4d9798285fb2a2291752

from : https://developers.notion.com/docs/getting-started

```
import { Client } from "@notionhq/client"

const notion = new Client({ auth: process.env.NOTION_KEY })

const databaseId = process.env.NOTION_DATABASE_ID

async function addItem(text) {
  try {
    const response = await notion.pages.create({
      parent: { database_id: databaseId },
      properties: {
        title: { 
          title:[
            {
              "text": {
                "content": text
              }
            }
          ]
        }
      },
    })
    console.log(response)
    console.log("Success! Entry added.")
  } catch (error) {
    console.error(error.body)
  }
}

addItem("Yurts in Big Sur, California")
```

