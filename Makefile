default: all

CFLAGS := -I./include -g --std=gnu99
CC := gcc

BINARIES := helloworldMG
all : $(BINARIES)

LIBS := -lach 

helloworldMG: helloworldMG.o
	gcc -o $@ $< $(LIBS)

%.o: %.c
	$(CC) $(CFLAGS) -o $@ -c $<

clean:
	rm -f $(BINARIES) src/*.o
