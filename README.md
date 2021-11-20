# Junction/Edge Rename script - SUMO net xml file

The Map (***map.osm file***) is downloaded from Open Street Map and is then converted into a SUMO Network (***saltlake.net.xml***).
>Command used: netconvert --osm-files map.osm -o saltlake.net.xml

Execute the file ***index.py*** to obtain the desired result. The final output sumo network file is ***saltlake_final.net.xml***.

The Junction ids in the ***saltlake.net.xml*** file (NET file) are renamed as “a_<id-number>” and internal
junction ids as “b_<id-number>” using the python script ***junction-id-modification.py***. 
After the Junction ids are renamed, the Edge ids are renamed as “<from junction id>_<to junction id>” 
and internal edge ids as ie_<id-number> using the python scrips ***edge-id-modification***.

Make sure SUMO is installed.
Python version used - v3.7.6
