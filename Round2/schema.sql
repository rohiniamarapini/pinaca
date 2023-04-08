DROP TABLE IF EXISTS company;

CREATE TABLE company
               (ROWID NUMBER PRIMARY KEY,
                Continent TEXT,
                Country TEXT,
                Name TEXT,
                MIC TEXT,
                LastChanged DATE
                );