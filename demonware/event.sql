SELECT  DISTINCT ON ("event_type") "event_type", "value" FROM 
    (SELECT "event_type", "time" , "value" - lag("value") OVER (ORDER BY "event_type", "time") AS "value"
    FROM events 
    WHERE event_type in (SELECT "event_type" 
                         FROM events 
                         GROUP BY "event_type" 
                         HAVING count(*) > 1)) 
AS u_events
ORDER BY "event_type", "time" DESC;