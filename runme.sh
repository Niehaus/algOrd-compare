for dir in entradas/random; do
  for subdir in ${dir}/*; do
    echo ${subdir}
    for file in ${subdir}/*; do
	    echo "$(python3 main.py ${file})"
    done
  done
done
