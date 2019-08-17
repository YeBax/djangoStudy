# －－单表分组查询－－
## 查询每一个部门名称以及对应的员工数
### emp:

+ id  name age   salary    dep
+ 1   alex  12   2000     销售部
+ 2   egon  22   3000     人事部
+ 3   wen   22   5000     人事部

### sql语句:
`select dep,Count(*) from emp group by dep;`
### ORM:
`emp.objects.all().values("dep").annotate(Count("id")`

# －－多表分组查询－－
## 多表分组查询：
查询每一个部门名称以及对应的员工数
### emp:
- id  name age   salary   dep_id
- 1   alex  12   2000       1
- 2   egon  22   3000       2
- 3   wen   22   5000       2
### dep
- id   name
- 1    销售部
- 2    人事部
### emp－dep:
- id  name age   salary   dep_id   id   name
- 1   alex  12   2000       1      1    销售部
- 2   egon  22   3000       2      2    人事部
- 3   wen   22   5000       2      2    人事部
### sql语句:
```
select dep.name,Count(*) from emp left join dep on emp.dep_id=dep.id group by emp.dep_id
select dep.name,Count(*) from emp left join dep on emp.dep_id=dep.id group by dep.id,dep.name
```
### ORM:
```
dep.objetcs.all().annotate(c=Count("emp")).values("name","c")
```