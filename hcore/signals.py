from django.db import transaction

@transaction.commit_manually
def after_syncdb(sender, **kwargs):
    import sys
    from django.db import connection
    if sender.__name__!='hydroscope.hcore.models': return
    cursor = connection.cursor()

    sys.stderr.write("Creating table ts_records...\n")
    try:
        cursor.execute("""CREATE TABLE ts_records
            (id INTEGER NOT NULL PRIMARY KEY,
            top TEXT NOT NULL, middle BYTEA, bottom TEXT NOT NULL,
            CONSTRAINT ts_records_id FOREIGN KEY (id)
                REFERENCES hcore_timeseries(id)
                DEFERRABLE INITIALLY IMMEDIATE
            )""")
        transaction.commit()
    except:
        sys.stderr.write(
            "ts_records creation failed; presumably it already existed\n")
        transaction.rollback()

    sys.stderr.write("Creating database function timeseries_start_date...\n")
    try:
        cursor.execute("""CREATE FUNCTION timeseries_start_date(aid INTEGER) 
            RETURNS timestamp AS $$
            DECLARE
                retvalue timestamp;
            BEGIN
                SELECT INTO retvalue
                    to_timestamp(substring(coalesce(top,bottom) from '^(.*?),'),
                        'YYYY-MM-DD HH24:MI')::timestamp
                FROM ts_records
                WHERE id=aid;
                RETURN retvalue;
            END
            $$ LANGUAGE plpgsql""")
        transaction.commit()
    except:
        sys.stderr.write(
            "ts_records creation failed; presumably it already existed\n")
        transaction.rollback()

    sys.stderr.write("Creating database function timeseries_end_date...\n")
    try:
        cursor.execute("""CREATE FUNCTION timeseries_end_date(aid INTEGER) 
            RETURNS timestamp AS $$
            DECLARE
                retvalue timestamp;
            BEGIN
                SELECT INTO retvalue to_timestamp(
                        substring(bottom from E'\n([^,]*?),[^\n]*?\n?$'),
                        'YYYY-MM-DD HH24:MI')::timestamp
                FROM ts_records
                WHERE id=aid;
                RETURN retvalue;
            END
            $$ LANGUAGE plpgsql""")
        transaction.commit()
    except:
        sys.stderr.write(
            "timeseries_end_date creation failed; maybe it already existed\n")
        transaction.rollback()
