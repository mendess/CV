ifeq ($(CONFIG),)
CONFIG := rust-go.config
endif

gen:
	./generate.py $(CONFIG)

auto:
	echo cv_template.tex | entr make CONFIG=$(CONFIG)

