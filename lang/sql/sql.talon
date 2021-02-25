mode: user.sql
mode: command
and code.language: sql
-
active language: "SQL is working"
select: "SELECT "
select (star | everything): "SELECT * "
distinct: "DISTINCT "
from: "FROM "
where: "WHERE "
and: "AND "
not: "NOT "
or: "OR "
in: "IN "
as: "AS "
group by: "GROUP BY "
having: "HAVING "
like: " LIKE "
limit: "LIMIT "
order by: "ORDER BY "
descending: " DESC"
between: " BETWEEN "
ascending: " ASC"
dot i d: ".id"
is not null: " IS NOT NULL"
is null: " IS NULL"
inner join: " INNER JOIN "
left join: " LEFT JOIN "
right join: " RIGHT JOIN "
outer join: " OUTER JOIN "
full outer join: " FULL OUTER JOIN "
on: " ON "
case when then end: "CASE WHEN  THEN  END"
case when:
  insert("CASE WHEN  THEN  END")
    key("left left left left left left left left left left")


# Aggregate functions
average:
    insert("AVG() ")
    key("left left")
array (aggregation | agg):
    insert("ARRAY_AGG() ")
    key("left left")
array transform:
    insert("TRANSFORM() ")
    key("left left")
array sort:
    insert("ARRAY_SORT() ")
    key("left left")
count:
    insert("COUNT() ")
    key("left left")
count if:
    insert("COUNT_IF() ")
    key("left left")
count (all | star | asterisk): "COUNT() "

state <user.text> equals: "{user.text} = "

# Presto functions
(approx | approximate) (perc | percentile):
    insert("approx_percentile(, 0.5) ")
    key("left left left left left left left")

# Presto functions
cast as double:
    insert("CAST( AS DOUBLE) ")
    key("left left left left left left left left left left left left left")

# Presto functions: regex
regex extracts:
    insert("regexp_extract(, '', 1) ")
    key("left left left left left left left left left")