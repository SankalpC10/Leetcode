WITH end_activity AS(
    Select machine_id, sum(timestamp)/count(*) as avg_time from Activity 
    where activity_type = 'end'
    group by machine_id
),
start_activity AS(
    Select machine_id, sum(timestamp)/count(*) as avg_time from Activity 
    where activity_type= 'start'
    group by machine_id
)
Select e.machine_id, ROUND((e.avg_time-s.avg_time)::numeric,3) as processing_time
FROM end_activity e join start_activity s
on e.machine_id = s.machine_id