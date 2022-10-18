import requests
from pprint import pprint
username = "Rajini44"
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url).json()
pprint(user_data)


OUTPUT:
  
  {
  "login": "rajini44",
  "id": 38476958,
  "node_id": "MDQ6VXNlcjM4NDc2OTU4",
  "avatar_url": "https://avatars.githubusercontent.com/u/38476958?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/rajini44",
  "html_url": "https://github.com/rajini44",
  "followers_url": "https://api.github.com/users/rajini44/followers",
  "following_url": "https://api.github.com/users/rajini44/following{/other_user}",
  "gists_url": "https://api.github.com/users/rajini44/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/rajini44/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/rajini44/subscriptions",
  "organizations_url": "https://api.github.com/users/rajini44/orgs",
  "repos_url": "https://api.github.com/users/rajini44/repos",
  "events_url": "https://api.github.com/users/rajini44/events{/privacy}",
  "received_events_url": "https://api.github.com/users/rajini44/received_events",
  "type": "User",
  "site_admin": false,
  "name": null,
  "company": null,
  "blog": "",
  "location": null,
  "email": null,
  "hireable": null,
  "bio": null,
  "twitter_username": null,
  "public_repos": 4,
  "public_gists": 0,
  "followers": 0,
  "following": 0,
  "created_at": "2018-04-17T20:48:35Z",
  "updated_at": "2018-06-13T15:14:50Z"
}
