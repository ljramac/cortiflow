CREATE TABLE IF NOT EXISTS Asset VALUES (
    id INT NOT NULL AUTO_INCREMENT,
    filepath VARCHAR(255) UNIQUE,
    size BIGINT NOT NULL,
    md5 VARCHAR(32) NOT NULL,
    status VARCHAR(32) NOT NULL,
    error_message VARCHAR(32),
    related_files TEXT,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    created_by VARCHAR(32) NOT NULL,
    updated_by VARCHAR(32) NOT NULL,
    metadata TEXT,
    PRIMARY KEY(id)
);
