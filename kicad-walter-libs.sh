#!/bin/sh
TIMESTAMP="2014.03.13"

mkdir -p kicad-walter
cd kicad-walter
wget -r -l 1 -A zip http://smisioto.no-ip.org/elettronica/kicad/kicad-en.htm
cd smisioto.no-ip.org/kicad_libs/library
for i in *.zip ; do
  unzip -o $i
  rm -f $i
done
mv -f power.dcm w_power.dcm
mv -f power.lib w_power.lib
mv -f license.txt w_license.txt
cd ../modules
mv -f ../packages3d/* ./
for i in *.zip ; do
  unzip -o $i
  rm -f $i
done
mv -f license.txt w_license.txt
cd ..
rmdir packages3d
cd ..
mv -f kicad_libs kicad-walter-libraries-$TIMESTAMP
echo "Creating kicad-walter-libraries-$TIMESTAMP.tar.xz ..."
tar cJf kicad-walter-libraries-$TIMESTAMP.tar.xz kicad-walter-libraries-$TIMESTAMP
