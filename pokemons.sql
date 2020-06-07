/* q1 */
select count(classification_name) , classification_name 
from pokemons as p join classification as c on p.classification_classification_id=c.classification_id
group by classification_name
order by count(classification_name) desc
limit 1;

/* q2 */
select avg(value) from stats as s join pokemon_stats as ps on s.idstats=ps.stats_idstats
where stats_name like "base_happiness"; 

/* q3 */

select count(*) from pokemons
where is_legendary=1;

/* q4 */

select max(value) as a, pokemons_pokedex_number, name 
from stats as s 
join pokemon_stats as ps on s.idstats=ps.stats_idstats
join pokemons as p on p.pokedex_number=ps.pokemons_pokedex_number
where stats_name like "against_bug"
group by pokemons_pokedex_number
order by a desc
limit 1;

/* q5 */ 
select avg(value) from pokemon_stats as ps join stats as s on ps.stats_idstats=s.idstats
where stats_name like "weight_kg";

/* q6 */
select max(value) as max_height from pokemon_stats as ps join stats as s on ps.stats_idstats=s.idstats
where stats_name like "height_m";

/* q7 */

select max(value) as highest_attack, name 
from stats as s 
join pokemon_stats as ps on s.idstats=ps.stats_idstats
join pokemons as p on ps.pokemons_pokedex_number=p.pokedex_number
where stats_name like "attack"
group by name
order by highest_attack desc
limit 1
;

/* q8 */

select min(value) as speed, name 
from stats as s 
join pokemon_stats as ps on s.idstats=ps.pokemons_pokedex_number
join pokemons as p on p.pokedex_number=ps.pokemons_pokedex_number
where stats_name like "speed"
group by name
order by speed asc
limit 1;

/* q9 */

select count(pokedex_number)/2 from 
types as t 
join pokemon_types as pt on t.type_id=pt.types_type_id
join pokemons as p on p.pokedex_number=pt.pokemons_pokedex_number
where not type_name = 'null';

/* q10 */

select name from
abilities as a 
join pokemon_abilities as pa on a.ability_id=pa.abilities_ability_id
join pokemons as p on p.pokedex_number=pa.pokemons_pokedex_number
where ability_name = 'Overgrow';
/**********************************/

create view pokemon_tipleri_view as
select name,type_name from types as t join pokemon_types as pt on t.type_id=pt.types_type_id
join pokemons as p on p.pokedex_number=pt.pokemons_pokedex_number
order by name asc;

select * from pokemon_tipleri_view;



/**********************************/
/OUT/
call countPokemons(@selam);
select @selam;
/**********************************/

/INOUT/
set @Name='Pikachu';

call is_legendary(@Name);
select @Name;

/**********************************/
/IN/

set @asd='Pikachu';
call pokeStats(@asd);
