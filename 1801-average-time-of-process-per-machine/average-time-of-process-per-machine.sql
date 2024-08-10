Select A1.machine_id, ROUND(AVG((A1.timestamp-A2.timestamp)::numeric),3) as processing_time
FROM Activity A1 join Activity A2
on A1.machine_id = A2.machine_id 
AND A1.process_id = A2.process_id
AND A1.activity_type = 'end'
AND A2.activity_type = 'start'
group by A1.machine_id