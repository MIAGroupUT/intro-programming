# Inspired from https://github.com/aramis-lab/DL4MI/blob/main/Makefile

notebook:
	@python .build/build_versions.py
clean:
	@rm -rf ./notebooks/*
	@echo "Erased content of folder notebooks"
