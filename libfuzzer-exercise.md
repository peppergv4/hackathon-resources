
# libFuzzer Exercise

  

In this exercise, we'll convert our cmake example into a libFuzzer target. While we could analyze our `fuzzme` executable as-is in Mayhem, converting to a libFuzzer target allows us to take advantage of libFuzzer's extra features.
  

1. Open `fuzzme.c` in your favorite text editor (this file is under the top-level `mayhem-cmake-example/` directory, not the `mayhem-cmake-example/build` directory).

2. In a libFuzzer target, you don't need a main function. Instead, payloads are deliviered directly to a function with the following signature: `int LLVMFuzzerTestOneInput(char* data, size_t size)`. Try modifying `fuzzme.c` so that a function called `LLVMFuzzerTestOneInput` calls the candidate function (`fuzzme(...)`).


If you can't figure it out, ask! (There is also a solution branch on the repo if you get really stuck)

3. Back in your build folder, try running `make` again. You should see output indicating that the build failed.

	```
	[ 50%] Building C object CMakeFiles/fuzzme.dir/fuzzme.c.o
	[100%] Linking C executable fuzzme
	/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/9/../../../x86_64-linux-gnu/Scrt1.o: in function `_start':
	(.text+0x24): undefined reference to `main'
	collect2: error: ld returned 1 exit status
	make[2]: *** [CMakeFiles/fuzzme.dir/build.make:84: fuzzme] Error 1
	make[1]: *** [CMakeFiles/Makefile2:76: CMakeFiles/fuzzme.dir/all] Error 2
	make: *** [Makefile:84: all] Error 2
	```

The build failed because the linker is expecting a main function, but we removed it! libFuzzer targets provide their own main, so we need to modify the build system to take this into account.

4. Now open `CMakeLists.txt` in your favorite text editor and uncomment the compilation and linker options. The end of your `CMakeLists.txt` should look similar to this:

	```
	...
	if (NOT CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
		message(FATAL_ERROR "Clang is required for libFuzzer!")
	endif()
	target_compile_options(fuzzme PUBLIC -fsanitize=fuzzer)
	target_link_options(fuzzme PUBLIC -fsanitize=fuzzer)
	```

5. Try running `make` in your build folder again. Again, it will fail. We need to tell CMake to configure our build to use clang because libFuzzer depends on clang.

	```
	CMake Error at CMakeLists.txt:8 (message):
	Clang is required for libFuzzer!
	-- Configuring incomplete, errors occurred!
	```

6. Delete the contents of your build tree (remember, you should be in the `build` folder we created earlier):

	```
	rm -rf *
	```

7. Now re-run cmake with the `CC` and `CXX` environment variables set to `clang` and `clang++` respectively. This will override the CMake default of `gcc` and `g++`.

	```
	CC=clang CXX=clang++ cmake ..
	```

	Note, if you're on macOS, you need to use a different, non-Apple Clang. We suggest using Homebrew to install (if you haven't already) with:

	```
	brew install llvm
	```

	However, you will need to change CC and CXX variables to reflect the location where the clang is located. If you're using the homebrew llvm package, you can use this command:

	```
	CC=/usr/local/Cellar/llvm/$(ls -1 /usr/local/Cellar/llvm/ | head -1)/bin/clang CXX=/usr/local/Cellar/llvm/$(ls -1 /usr/local/Cellar/llvm/ | head -1)/bin/clang++ cmake ..

	# OR

	cmake .. -DCMAKE_C_COMPILER=/usr/local/Cellar/llvm/$(ls -1 /usr/local/Cellar/llvm/ | head -1)/bin/clang -DCMAKE_CXX_COMPILER=/usr/local/Cellar/llvm/$(ls -1 /usr/local/Cellar/llvm/ | head -1)/bin/clang++
	```

	- ##### macOS Homebrew LLVM Installation Note:

		Based on a combination of factors, such as chiptype (Intel vs. Apple Silicon), installation directory, and other unknown factors, the place that Homebrew installs llvm may differ. In the code above, it is assumed Homebrew's installations are located in `/usr/local/Cellar/`, and `clang` and `clang++` are in `/usr/local/Cellar/llvm/version/bin/`. However, it's possible that your version of Homebrew installs packages in `/opt/homebrew/Cellar`. If

		```
		cmake .. -DCMAKE_C_COMPILER=/usr/local/Cellar/llvm/$(ls -1 /usr/local/Cellar/llvm/ | head -1)/bin/clang -DCMAKE_CXX_COMPILER=/usr/local/Cellar/llvm/$(ls -1 /usr/local/Cellar/llvm/ | head -1)/bin/clang++
		```

		gives an error, try changing the location to match your system-specific location. For some users, this is as follows:

		```
		cmake .. -DCMAKE_C_COMPILER=/opt/homebrew/Cellar/llvm/$(ls -1 /opt/homebrew/Cellar/llvm/ | head -1)/bin/clang -DCMAKE_CXX_COMPILER=/opt/homebrew/Cellar/llvm/$(ls -1 /opt/homebrew/Cellar/llvm/ | head -1)/bin/clang++
		```

		This should be sufficient to set the proper locations for the CC and CXX variables to access the right version of clang and clang++ needed to compile with libfuzzer.

8. Now run `make` to build.

9. You should now have a new `fuzzme` executable. Run it.

	```
	./fuzzme
	```

If you see output similar to the above, congratulations you just created a libFuzzer target!
 
```
INFO: Seed: 2682090316
INFO: Loaded 1 modules (7 inline 8-bit counters): 7 [0x4e8040, 0x4e8047),
INFO: Loaded 1 PC tables (7 PCs): 7 [0x4be940,0x4be9b0),
INFO: -max_len is not provided; libFuzzer will not generate inputs larger than 4096 bytes
INFO: A corpus is not provided, starting from an empty corpus
#2 INITED cov: 3 ft: 4 corp: 1/1b exec/s: 0 rss: 24Mb
#3 NEW cov: 4 ft: 5 corp: 2/2b lim: 4 exec/s: 0 rss: 24Mb L: 1/1 MS: 1 ShuffleBytes-
#2769 NEW cov: 5 ft: 6 corp: 3/3b lim: 29 exec/s: 0 rss: 24Mb L: 1/1 MS: 1 ChangeByte-
#19447 NEW cov: 6 ft: 7 corp: 4/5b lim: 191 exec/s: 0 rss: 24Mb L: 2/2 MS: 3 InsertByte-ShuffleBytes-ChangeBinInt-
==37703== ERROR: libFuzzer: deadly signal
#0 0x4aded0 in __sanitizer_print_stack_trace (/home/nathan/src/mayhem-cmake-example/build/fuzzme+0x4aded0)
#1 0x45a1d8 in fuzzer::PrintStackTrace() (/home/nathan/src/mayhem-cmake-example/build/fuzzme+0x45a1d8)
#2 0x43f323 in fuzzer::Fuzzer::CrashCallback() (/home/nathan/src/mayhem-cmake-example/build/fuzzme+0x43f323)
#3 0x7f6e0d50f3bf (/lib/x86_64-linux-gnu/libpthread.so.0+0x143bf)
#4 0x7f6e0d1d003a in __libc_signal_restore_set /build/glibc-sMfBJT/glibc-2.31/signal/../sysdeps/unix/sysv/linux/internal-signals.h:86:3
#5 0x7f6e0d1d003a in raise /build/glibc-sMfBJT/glibc-2.31/signal/../sysdeps/unix/sysv/linux/raise.c:48:3
#6 0x7f6e0d1af858 in abort /build/glibc-sMfBJT/glibc-2.31/stdlib/abort.c:79:7
#7 0x4ae2e3 in fuzzme (/home/nathan/src/mayhem-cmake-example/build/fuzzme+0x4ae2e3)#8 0x4ae370 in LLVMFuzzerTestOneInput (/home/nathan/src/mayhem-cmake-example/build/fuzzme+0x4ae370)
#9 0x4409e1 in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/home/nathan/src/mayhem-cmake-example/build/fuzzme+0x4409e1)
#10 0x440125 in fuzzer::Fuzzer::RunOne(unsigned char const*, unsigned long, bool, fuzzer::InputInfo*, bool*) (/home/nathan/src/mayhem-cmake-example/build/fuzzme+0x440125)
#11 0x4423c7 in fuzzer::Fuzzer::MutateAndTestOne() (/home/nathan/src/mayhem-cmake-example/build/fuzzme+0x4423c7)
#12 0x4430c5 in fuzzer::Fuzzer::Loop(std::__Fuzzer::vector<fuzzer::SizedFile, fuzzer::fuzzer_allocator<fuzzer::SizedFile> >&) (/home/nathan/src/mayhem-cmake-example/build/fuzzme+0x4430c5)
#13 0x431a7e in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/home/nathan/src/mayhem-cmake-example/build/fuzzme+0x431a7e)
#14 0x45a8c2 in main (/home/nathan/src/mayhem-cmake-example/build/fuzzme+0x45a8c2)
#15 0x7f6e0d1b10b2 in __libc_start_main /build/glibc-sMfBJT/glibc-2.31/csu/../csu/libc-start.c:308:16
#16 0x40681d in _start (/home/nathan/src/mayhem-cmake-example/build/fuzzme+0x40681d)
NOTE: libFuzzer has rudimentary signal handlers.
Combine libFuzzer with AddressSanitizer or similar for better crash reports.
SUMMARY: libFuzzer: deadly signal
MS: 1 InsertByte-; base unit: 6721d9fb11ca730b528749d7e4f9e8c52766e450
0x62,0x75,0x67,
bug
artifact_prefix='./'; Test unit written to ./crash-6885858486f31043e5839c735d99457f045affd0
Base64: YnVn
```