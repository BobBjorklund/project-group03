create or replace view yob as select animal_id, extract(year from dob) as year, extract(month from dob) as month  from goat;
create or replace view ww as select y.animal_id, w.alpha_value from yob as y join weight as w on (y.animal_id=w.animal_id) and (extract(year from w.when_measured)=y.year) and ((extract(month from w.when_measured)=8) or (extract(month from w.when_measured)=9)) and y.month<8;
