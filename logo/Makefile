BUILD_FOLDER=build
SRC_FOLDER=./src
ICO_FOLDER=./ico
PNG_FOLDER=./png
BIN_FOLDER=./pdf

TEX=lualatex
TEX_OPTIONS=-output-directory=$(BUILD_FOLDER)

CONVERT=magick
CONVERT_DENSITY=300
CONVERT_RESIZE=200x200

TEX_SRC=$(SRC_FOLDER)/logo_color.tex $(SRC_FOLDER)/logo_bw.tex $(SRC_FOLDER)/logo_bwr.tex $(SRC_FOLDER)/name_bw.tex $(SRC_FOLDER)/name_bwr.tex $(SRC_FOLDER)/full_bw.tex $(SRC_FOLDER)/full_bwr.tex
OUTPUTS=$(patsubst $(SRC_FOLDER)/%.tex, $(PNG_FOLDER)/%.png, $(TEX_SRC)) $(patsubst $(SRC_FOLDER)/%.tex, $(ICO_FOLDER)/%.ico, $(TEX_SRC))

all: dirs $(OUTPUTS) 

dirs:
	mkdir -p $(BUILD_FOLDER)
	mkdir -p $(BIN_FOLDER)
	mkdir -p $(PNG_FOLDER)
	mkdir -p $(ICO_FOLDER)

$(BUILD_FOLDER)/%.pdf: $(SRC_FOLDER)/%.tex
	$(TEX) $(TEX_OPTIONS) $<
	cp $@ $(BIN_FOLDER)

$(PNG_FOLDER)/%.png: $(BUILD_FOLDER)/%.pdf
	$(CONVERT) -units pixelsperinch -density $(CONVERT_DENSITY) -quality 100 $<  $@
	$(CONVERT) $@ -resize 50% $@

$(ICO_FOLDER)/%.ico: $(PNG_FOLDER)/%.png
	$(CONVERT) -background transparent $< -define icon:auto-resize=64 $@

clean:
	rm -rf $(BUILD_FOLDER)/*
	rm -rf $(BIN_FOLDER)/*
	rm -rf $(ICO_FOLDER)/*
	rm -rf $(PNG_FOLDER)/*
