#!/usr/bin/bash

currentVer='1.0'

xgettext *.py -o ./locales/unobot.pot --foreign-user \
  --package-name="reyuno_bot" \
  --package-version="$currentVer" \
  --msgid-bugs-address='uno@reyn0pe.de' \
  --keyword=__ \
  --keyword=_ \
  --keyword=_:1,2 \
  --keyword=__:1,2