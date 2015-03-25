* find all variable names

    egrep '\<[A-z_][0-z_]*\>' file

* find two continious identical word

    egrep '\<([A-z]+) +\1\>' file

* changing any 1 or 2 character with a comma into desired parttern

      s/[a-z]\{1,2},/"&"/g

* find anyline contains any characters in the Square Bracket `[]`

      grep [$KU] file_name
