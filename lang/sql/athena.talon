app: athena
-
active language: "SQL is working"
select: "SELECT "
select (star | everything | asterisk): "SELECT * "
distinct: "DISTINCT "
from: "FROM "
from <user.text>:
    "FROM "
    insert(user.formatted_text(user.formatted_text("{user.text}", "ALL_LOWERCASE"), "DOT_SEPARATED"))
    " "
where: "WHERE "
(enter|slap): key(enter)
and: "AND "
not: "NOT "
or: "OR "
in: "IN "
as: "AS "
group by: "GROUP BY "
group by <user.text>$:
    "GROUP BY "
    insert(user.formatted_text("{user.text}", "COMMA_SEPARATED"))
    " "
order by: "ORDER BY "
order by <user.text>$:
    "ORDER BY "
    insert(user.formatted_text("{user.text}", "COMMA_SEPARATED"))
    " "
having: "HAVING "
like: " LIKE "
limit: "LIMIT "
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
count (all | star | asterisk) as <user.text>:
    insert("COUNT() AS ")
    insert(user.formatted_text(text, "PRIVATE_CAMEL_CASE"))

state <user.text> equals: "{user.text} = "

transform:
    insert("TRANSFORM()")
    key("left")

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


app equals <user.text>:
    "app = '"
    insert(user.formatted_text("{user.text}", "ALL_LOWERCASE"))
    "' "

our: "hour"
(app date|update) our: "app, date, hour"
(app date|update): "app, date"
date our: "date, hour"




# noise controls
#parrot(blup):
#	key(ctrl-shift-z)
#parrot(pop):
#	key(ctrl-shift-z)
#parrot(tut):
#	key(ctrl-z)
