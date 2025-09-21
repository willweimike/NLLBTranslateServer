# NLLBTranslateServer - Translate Locally

![Latest Release](https://img.shields.io/github/v/release/willweimike/NLLBTranslateServer?display_name=tag&label=Latest%20Release&sort=semver) ![Downloads](https://img.shields.io/github/downloads/willweimike/NLLBTranslateServer/total?label=Downloads)

> Because I am a student, I could not afford the fee of Apple Developer, so the binary is not code-signed.

## Translate Locally, Privately
Google Translate API are convenient to use, but people may concern about "privacy" since data must be send to the remote to do the translation work

## Setup
Place the binary alongside with your model folder, **"The File and Folder Name"** must be the same as the picture

In terminal
1. type `sudo chmod 777 path/to/NTS_darwin` to allow the executable to run and fetch nllb files
2. type `xattr -cr path/to/NTS_darwin` to eliminate warning from Apple Signature
3. type `./NTS_darwin` to start server

Everything is now ready

![](https://github.com/willweimike/NLLBTranslateServer/blob/main/assets/Demo.png)

## Endpoints provided by NLLBTranslateServer
- http://127.0.0.1:8080/ : accept GET request, return current server status
- http://127.0.0.1:8080/help : accept GET request, return help message
- http://127.0.0.1:8080/translate: accept POST request for translation, please contain the fields within the following picture

![](https://github.com/willweimike/NLLBTranslateServer/blob/main/assets/Demo2.png)


## Where to get the AI models?
Please go to this [link](https://huggingface.co/mikeforai/NLLB-200-Models-Collections) and download, the things that you would need are prepared for you 😃.
