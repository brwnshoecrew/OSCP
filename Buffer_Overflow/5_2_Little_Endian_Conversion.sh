#!/bin/bash

variable = "$1"
i = ${#v}

while [ $i -gt 0 ]
do
    i = $[$i-2]
    echo -n "\x"${variable:$i:2}
done

echo
