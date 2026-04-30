#!/bin/bash

echo "$(date)"
echo "===Server Log Analysis Report==="
total_lines=$(wc -l $1)
echo "Total lines in the log are: $total_lines "
echo ""
grep -io -E 'ERROR' $1 | sort | uniq -c
grep -io -E 'WARNING' $1 | sort | uniq -c
grep -io -E 'INFO' $1 | sort | uniq -c
uniq_errors=$(grep -io -E 'ERROR' $1 | cut -d' ' -f 3 |sort|uniq -c)
echo "Total Unique Errors are: $uniq_errors"
echo ""
tail -n 5 $1
echo "=== End of Report ==="
