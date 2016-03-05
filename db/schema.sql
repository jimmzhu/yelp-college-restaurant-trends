CREATE TABLE IF NOT EXISTS businesses (
    business_id     VARCHAR(255)        NOT NULL,
    "type"          VARCHAR(16)         NOT NULL,
    name            VARCHAR(255)        NOT NULL,
    neighborhoods   VARCHAR(255) ARRAY  NOT NULL,
    full_address    VARCHAR(255)        NOT NULL,
    city            VARCHAR(255)        NOT NULL,
    state           VARCHAR(255)        NOT NULL,
    latitude        DECIMAL(10, 7)      NOT NULL,
    longitude       DECIMAL(10, 7)      NOT NULL,
    stars           DECIMAL(2, 1)       NOT NULL,
    review_count    INTEGER             NOT NULL,
    categories      VARCHAR(255) ARRAY  NOT NULL,
    open            BOOLEAN             NOT NULL,
    hours           JSON,
    attributes      JSON
);
CREATE UNIQUE INDEX index_businesses_on_business_id ON businesses (business_id);
CREATE INDEX index_businesses_on_city_and_state ON businesses (city, state);

CREATE TABLE IF NOT EXISTS reviews (
    "type"          VARCHAR(16)         NOT NULL,
    business_id     VARCHAR(255)        REFERENCES businesses(business_id),
    user_id         VARCHAR(255)        NOT NULL,
    review_id       VARCHAR(255)        NOT NULL,
    stars           DECIMAL(2, 1)       NOT NULL,
    text            TEXT                NOT NULL,
    "date"          DATE                NOT NULL,
    votes           JSON
);
CREATE INDEX index_reviews_on_business_id ON reviews (business_id);

CREATE TABLE IF NOT EXISTS checkins (
    "type"          VARCHAR(16)         NOT NULL,
    business_id     VARCHAR(255)        REFERENCES businesses(business_id),
    checkin_info    JSON
);
CREATE INDEX index_checkins_on_business_id ON checkins (business_id);
