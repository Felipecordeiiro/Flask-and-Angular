USE Pycodebr;

CREATE TABLE tasks (
    id_file integer not null auto_incremet,
    url_file varchar(100)
    PRIMARY KEY (id_file)
)

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;