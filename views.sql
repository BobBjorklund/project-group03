-- all commented lines have to do with wean weight, sale weight, or winter weights.
-- waiting on guidance from stakeholder
--Create view winws as select * from winter_weight natural join weight order by weight.animal_id;
--Create view weanws as select * from wean_weight  natural join weight order by weight.animal_id;
--Create view sws as select * from sale_weight natural join weight order by weight.animal_id;
Create view damtags as select distinct dam as tag from animal;
Create view dams as a.* from animal as a natural join damtags as d; 
Create view kids as select a.* from animal as a inner join dams as d on a.dam = d.tag order by a.dam;
Create view nk as select dam, count(animal_id) as num_kids from kids group by dam;
Create view damwnk as select * from dams join nk on dams.tag = nk.dam;
Create view kidwns as select kids.*, nk.num_kids from kids join nk on kids.dam = nk.dam;
Create view damwbw as select d.*, b.WValue from damwnk as d join birth_weight as b on d.animal_id = b.animal_id;
Create view kidwbw as select k.*, b.WValue from kidwns as k join birth_weight as b on b.animal_id = b.animal_id;
--Create view damwweanw as select d.*, w.WValue from damwbw as d join weanws as w on d.animal_id = w.animal_id;
--Create view kidwweanw as select k.*, w.WValue from kidwbw as k join weanws as w on b.animal_id = w.animal_id;


--Create view damwsw as select d.*, s.WValue from damwweanw as d join sws as s on d.animal_id = s.animal_id;
--Create view kidwsw as select k.*, s.WValue from kidwweanw as k join winws as s on b.animal_id = s.animal_id;
