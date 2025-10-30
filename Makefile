
.PHONY: clean logo figures computing

all: logo figures computing


logo:
	make -C logo

figures:
	make -C figures

computing:
	make -C computing

clean:
	make -C logo clean
	make -C figures clean
	make -C computing clean
