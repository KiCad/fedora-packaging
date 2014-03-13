#!/bin/sh
bzr checkout lp:kicad kicad.bzr
bzr checkout lp:~kicad-product-committers/kicad/library kicad-library.bzr
bzr branch --stacked lp:~kicad-developers/kicad/doc kicad-doc.bzr
