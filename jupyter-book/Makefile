all: html latex

latex:
	jupyter-book build . --builder pdflatex

html:
	mkdir -p _build/.jupyter_cache
	jupyter-book build .

clean:
	# keep jupyter-cache cache folder
	jupyter-book clean .

full-clean:
	rm -rf _build
