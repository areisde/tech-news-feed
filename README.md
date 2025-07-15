# Real-Time IT News — Front-End  
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](LICENSE)

Vue 3 + **Nuxt 3** single-page interface that consumes the _IT-News Relevance & Ranking_ API and presents the latest, most critical incidents to IT managers.

> **This repo only contains the UI layer.**  
> The crawling, filtering and ranking pipeline lives in the companion project:  
> <https://github.com/areisde/tech-news-backend>

---

## ✨  What you can do today

* **Live feed** — left screen part shows “Important updates” based on the ranking algorithm; right screen part has tabs that break down the news by  
  _Critical Severity • Widespread Scope • High User Impact_.  If you want to display ranking by category.
* **Source toggles** — dropdown lets you hide/show articles from different sources on-the-fly.  
* **Instant refresh** — one click pulls `/api/retrieve` and re-renders.

For demo purposes the component hard-codes an article to belong to a category if its score in the category is **0.5** or higher; next iterations will let the user drag these.

---

## 🗄️ Adding more news sources
Back-end keeps feeds in Supabase sources table:
```sql
INSERT INTO sources (name, url, type)
VALUES ('AWS Status', 'https://status.aws.amazon.com/rss/all.rss', 'rss');
```

Next automated crawling will include articles from the new feed and thus will be propagated to the UI.

<em>Planned:</em> “Add source” modal → POST /api/sources/add (no SQL needed).

## 🛣️ Road-map

| Status | Feature | Notes / ETA |
|--------|---------|-------------|
| ✅ | **Live feed** with manual *Refresh* | implemented |
| ✅ | Source visibility and selection dropdown | implemented |
| ⏳ | **Per-user thresholds** (sliders for severity / scope / impact) | Q3 ’25 |
| ⏳ | **Source management UI** (add / remove / test feed) | Q3 ’25 |
| ⏳ | **Web-push / Email notifications** for “critical” stories | Q4 ’25 |
| ⏳ | **Dark theme** via `@nuxtjs/color-mode` | Q4 ’25 |
| ⏳ | i18n (English / French / German) | Q1 ’26 |
---

## 🧰 Tech stack

| Layer | Library / Service | Why we chose it |
|-------|-------------------|-----------------|
| **Frontend Framework** | **Nuxt 3** (Vue 3) | File-based routing, SSR/SPA switch, zero-config DX |
| **Styling** | Tailwind | Ease of use |
| **UI Components** | **nuxt.ui**, **lucide-icons** | Easy to setup and modern |
| **Backend API** | Azure Functions (`retrieve`) | Serverless, cron + HTTP in one place |
| **Hosting (UI)** | AWS S3 + CloudFront | Cheap, global, zero-ops static hosting |
| **CI/CD** | GitHub Actions | Lint, test, deploy on push |

## 🚀  Quick start

```bash
# clone repo

npm install
npm run dev