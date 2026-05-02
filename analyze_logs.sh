#!/bin/bash

total_lines=$(wc -l $1)
error_count=$(grep -io -E 'ERROR' $1 | sort | uniq -c)
warning_count=$(grep -io -E 'WARNING' $1 | sort | uniq -c)
info_count=$(grep -io -E 'INFO' $1 | sort | uniq -c)
uniq_errors=$(grep 'ERROR' $1| cut -d' ' -f 4- |uniq -c)

echo ""
echo "Generated: $(date)"
echo "Analyzing: $1"
echo ""
echo "===Server Log Analysis Report==="

echo "Total lines in the log are: $total_lines "
echo "The amount of errors in the file is: $error_count"
echo "The amount of warning in the file is: $warning_count"
echo "The amount of Info in the file is: $info_count"
echo ""

echo "Total Unique Errors are: "
echo "$uniq_errors"
echo ""
echo "The last 5 logs in the file are:"
tail -n 5 $1
echo ""
echo "=== End of Report ==="
