BUILD_FOLDER=build
SRC_FOLDER=./src
PNG_FOLDER=./png
PDF_FOLDER=./pdf

TEX=pdflatex
TEX_OPTIONS=-output-directory=$(BUILD_FOLDER)

PY=python

CONVERT=magick
CONVERT_DENSITY=300

TEX_SRC=$(wildcard ./src/Python-*tex)
TEX_OUTPUTS=$(patsubst $(SRC_FOLDER)/%.tex, $(PNG_FOLDER)/%.png, $(TEX_SRC))


all: dirs $(TEX_OUTPUTS)

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

	
clean:
	rm -rf $(BUILD_FOLDER)/*
	rm -rf $(PDF_FOLDER)/*
	rm -rf $(PNG_FOLDER)/*
