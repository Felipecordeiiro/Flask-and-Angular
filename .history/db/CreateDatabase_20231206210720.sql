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

INSERT INTO tasks (id_file, url_file) VALUES (1, 'url_file')
INSERT INTO tasks (id_file, url_file) VALUES (2, 'url_file2')
INSERT INTO tasks (id_file, url_file) VALUES (3, 'url_file')

'id_file': 1,
        'url_file': 'url_file'
    },
        {
        'id_file': 2,
        'url_file': 'url_file2'
    },
        {
        'id_file': 3,
        'url_file': 'url_file3'