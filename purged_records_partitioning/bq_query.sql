bq query --use_legacy_sql=false --batch --allow_large_results --destination_table=SCHEMA.TABLE\$PART_DAY  --format none --replace "
SELECT YDAY.*
  FROM (
        SELECT *
          FROM SCHEMA.TABLE
         WHERE var = '$YDAY'
       ) YDAY
  LEFT OUTER JOIN
       (
        SELECT KEY
          FROM SCHEMA.TABLE
         WHERE var = '$TDAY'
       ) TDAY
    ON YDAY.KEY = TDAY.KEY
 WHERE TDAY.KEY IS NULL
;
"

