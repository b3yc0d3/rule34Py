## Class > TopTag
- [class TopTag](#toptag)
    - [rank](#id)
    - [tagname](#hash)
    - [percentage](#score)


### TopTag
Type: `class`\
Symtax: `toptag = TopTag(<rank>, <tagname>, <percentage>)`\
Args:\
&ensp;&ensp;&ensp;`rank` __[int]__ Rank of tag\
&ensp;&ensp;&ensp;`tagname` __[str]__ Name of tag\
&ensp;&ensp;&ensp;`percentage` __[int]__ Usage of tag\

Returns:\
&ensp;&ensp;&ensp; __[TopTag]__ TopTag Object

### rank
Type: `property`\
Syntax: `<TopTag>.rank`\
Returns:\
&ensp;&ensp;&ensp; __[int]__ Tag rank

Get rank of tag

### tagname
Type: `property`\
Syntax: `<TopTag>.tagname`\
Returns:\
&ensp;&ensp;&ensp; __[str]__ Tag name

Get name of tag

### percentage
Type: `property`\
Syntax: `<TopTag>.percentage`\
Returns:\
&ensp;&ensp;&ensp; __[int]__ Usage as percentage

Get tag usage percentage