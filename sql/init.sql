-- Table: sources
CREATE TABLE IF NOT EXISTS sources (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    url TEXT NOT NULL,
    type TEXT NOT NULL -- e.g., 'rss' or 'reddit'
);

-- Table: articles
CREATE TABLE IF NOT EXISTS articles (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    body TEXT,
    published_at TIMESTAMP,
    source TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Table : filters
CREATE TABLE IF NOT EXISTS filters (
    id SERIAL PRIMARY KEY,
    url TEXT NOT NULL,
    embedding VECTOR(384),
    relevant BOOLEAN NOT NULL
);