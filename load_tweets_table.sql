CREATE TABLE tweets (
    id VARCHAR(18) PRIMARY KEY,
    geom GEOMETRY(Point, 4326),
    text TEXT
);
