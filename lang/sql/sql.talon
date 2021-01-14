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
on: " ON "
case when then end: "CASE WHEN  THEN  END"


# Aggregate functions
average:
    insert("AVG() ")
    edit.left()
    edit.left()
array (aggregation | agg):
    insert("ARRAY_AGG() ")
    edit.left()
    edit.left()
array transform:
    insert("TRANSFORM() ")
    edit.left()
    edit.left()
array sort:
    insert("ARRAY_SORT() ")
    edit.left()
    edit.left()
count:
    insert("COUNT() ")
    edit.left()
    edit.left()
count if:
    insert("COUNT_IF() ")
    edit.left()
    edit.left()
count (all | star | asterisk): "COUNT() "

state <user.text> equals:
    insert("{user.text} = ")
    edit.left()

# Presto functions
(approx | approximate) (perc | percentile):
    insert("approx_percentile(, 0.5) ")
    edit.left()
    edit.left()
    edit.left()
    edit.left()
    edit.left()
    edit.left()
    edit.left()

# Presto functions
cast as double:
    insert("CAST( AS DOUBLE) ")
    edit.left()
    edit.left()
    edit.left()
    edit.left()
    edit.left()
    edit.left()
    edit.left()
    edit.left()
    edit.left()
    edit.left()
    edit.left()
    edit.left()