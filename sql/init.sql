-- Table: sources
CREATE TABLE IF NOT EXISTS sources (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    url TEXT NOT NULL,
    type TEXT NOT NULL -- e.g., 'rss' or 'reddit'
);

-- Table: articles
CREATE TABLE IF NOT EXISTS articles (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    body TEXT,
    published_at TIMESTAMP,
    source_id INTEGER REFERENCES sources(id),
    external_id TEXT, -- original id from RSS/Reddit
    url TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
