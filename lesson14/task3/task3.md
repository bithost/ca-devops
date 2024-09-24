# Designa simple database schema for a library system 

## Requirments

### Have these tables

* Books
* Authors
* Patrons (library users)

### Links
 
 Each book should be linked to an author, and you should be able to track which patron has borrowed which book.


 ![Scheme](http://www.plantuml.com/plantuml/png/bP11geCm48RtESNWzf4BY8YlYswwyGPbh06bcfJ9s5AqTszqcY9I2jte33__buyfF2Fnq7VAM6xv3idEkRDF03rKymIZ0lXRvcDRGmfsw2j3a6Nb8Sz3fdNuX6fdGdX5EZL82W07RXnjAdkfN939sK_PGxqz_XU0c0WikiZsnSPYlv9PGylbPO6AHOJAzXCqMasJrcvydIk51hqIsZOAVo9tCxKgZAtdepy1)

In this schema:

The Books table has:
 a primary key book_id, and foreign keys author_id and patron_id linking to the Authors and Patrons tables respectively.
The Authors table has a primary key author_id.
The Patrons table has a primary key patron_id.
Each book is linked to an author and a patron (library user). The relationships are represented by the lines connecting the entities (tables).