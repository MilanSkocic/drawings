
.PHONY: clean logo figures

all: logo figures


logo:
	make -C logo

figures:
	make -C figures

clean:
	make -C logo clean
	make -C figures clean
