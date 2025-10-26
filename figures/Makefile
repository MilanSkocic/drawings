BUILD_FOLDER=build
SRC_FOLDER=./src
PNG_FOLDER=./png
PDF_FOLDER=./pdf

TEX=pdflatex
TEX_OPTIONS=-output-directory=$(BUILD_FOLDER)

PY=python

CONVERT=magick
CONVERT_DENSITY=300

TEX_SRC=$(wildcard ./src/PEC-*tex) $(wildcard ./src/EIS-*.tex)
TEX_OUTPUTS=$(patsubst $(SRC_FOLDER)/%.tex, $(PNG_FOLDER)/%.png, $(TEX_SRC))

PY_SRC=$(wildcard ./src/EIS-*.py)
PY_OUTPUTS=$(patsubst $(SRC_FOLDER)/%.py, $(PNG_FOLDER)/%.png, $(PY_SRC)) $(patsubst $(SRC_FOLDER)/%.py, $(PDF_FOLDER)/%.pdf, $(PY_SRC))


all: dirs $(TEX_OUTPUTS) $(PY_OUTPUTS)

dirs:
	mkdir -p $(BUILD_FOLDER)
	mkdir -p $(PDF_FOLDER)
	mkdir -p $(PNG_FOLDER)

$(BUILD_FOLDER)/%.pdf: $(SRC_FOLDER)/%.tex
	$(TEX) $(TEX_OPTIONS) $<
	cp $@ $(PDF_FOLDER)

$(PNG_FOLDER)/%.png: $(BUILD_FOLDER)/%.pdf
	$(CONVERT) -units pixelsperinch -density $(CONVERT_DENSITY) -quality 100 $<  $@
	# $(CONVERT) $@ -resize 50% $@

$(PNG_FOLDER)/%.png: $(SRC_FOLDER)/%.py
	$(PY) $< $@

$(PDF_FOLDER)/%.pdf: $(SRC_FOLDER)/%.py
	$(PY) $< $@
	
	
clean:
	rm -rf $(BUILD_FOLDER)/*
	rm -rf $(PDF_FOLDER)/*
	rm -rf $(PNG_FOLDER)/*

clean_tex:
	rm -rf ${TEX_OUTPUTS}

clean_py:
	rm -rf ${PY_OUTPUTS}
