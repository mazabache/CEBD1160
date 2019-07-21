for i in ./*.csv; do
	echo $i
	awk -F, 'END {printf "Number of Rows : %s\nNumber of Columns = %s\n", NR, NF}' $i
	head -2 $i
done

