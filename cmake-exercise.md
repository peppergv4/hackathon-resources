# CMake Exercise

In this exercise you will build and run a CMake executable.

## Forking the repository

Before we begin, we first must fork the repository.

1. In your browser, navigate to https://github.com/mayhemheroes/mayhem-cmake-example.

2. Click "Fork" near the top of the page.

    ![Fork](assets/images/gh-click-fork.png)

3. When asked where you want to create the fork, select your username.

Now you have your own fork of the `mayhem-cmake-example` repo. Next, we'll clone and run the toy target locally.

## Clone and Run Locally

1. In a terminal, clone mayhem-cmake-example and change into the directory. (You'll want to leave the `hackathon-resources` directory first)

    ```
    cd ~/
    git clone https://github.com/<Your Github Username>/mayhem-cmake-example
    cd mayhem-cmake-example/
    ```

2. Now, create a build directory and change into it.

    ```
    mkdir build
    cd build/
    ```

3. Run cmake to generate the Makefile and build tree.

    ```
    cmake ..
    ```

    Note: if you're on macOS, you will first need to install the Homebrew package manager and cmake. Run the following command to install Homebrew.
    ```
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
    The install script will output two commands similar to:
    ```
    echo 'eval "\$(${HOMEBREW_PREFIX}/bin/brew shellenv)"' >> ${shell_profile}
    eval "\$(${HOMEBREW_PREFIX}/bin/brew shellenv)"
    ```
    Run the provided commands to add the brew command to your terminal.
    Once complete, run 
    ```
    brew update
    brew install cmake
    cmake ..
    ```

4. Run Make

    ```
    make
    ```

5. Once the build completes, try running the resulting executable.

    ```
    ./fuzzme
    ```

You should see output similar to the following:

```
usage: ./fuzzme PAYLOAD
```

Congratulations, you've just built an executable using CMake!
