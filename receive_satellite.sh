#!/bin/bash
# save as: receive_satellite.sh

OUT_NAME="sat_$(date +%s)"
rtl_fm -f 137.62M -s 208k -g 40 | sox -t raw -r 208k -es -b 16 -c 1 -V1 - "$OUT_NAME.wav"
wxtoimg -e HVCT "$OUT_NAME.wav" "$OUT_NAME.png"