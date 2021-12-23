-- tables
CREATE
    TABLE
        IF NOT EXISTS AIRBYTE_CONFIGS(
            id BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
            config_id VARCHAR(36) NOT NULL,
            config_type VARCHAR(60) NOT NULL,
            config_blob JSONB NOT NULL,
            created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
        );

-- indices
CREATE
    UNIQUE INDEX IF NOT EXISTS airbyte_configs_type_id_idx ON
    AIRBYTE_CONFIGS(
        config_type,
        config_id
    );

CREATE
    INDEX IF NOT EXISTS airbyte_configs_id_idx ON
    AIRBYTE_CONFIGS(config_id);
