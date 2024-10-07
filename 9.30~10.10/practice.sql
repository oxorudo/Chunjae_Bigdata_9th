select distinct "proc_ymd",
    case
        when substring("proc_ymd", -4, 2) in ('01','03','05','07','08','10','12')
            then if(substring("proc_ymd", -2) in ('31'), 'Y', 'N')
        when substring("proc_ymd", -4, 2) in ('02')
            then if(substring("proc_ymd", -2) in ('28'), 'Y', 'N')
        else if(substring("proc_ymd", -2) in ('30'), 'Y', 'N')
        end as "last_day_yn"
from "learning_analytics"."e_media"
where 1=1
    and substring("proc_ymd", 1, 6) = '202403'
order by "proc_ymd" asc
limit 50;