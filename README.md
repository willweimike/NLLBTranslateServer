# NLLBTranslateServer - Translate Locally

## Locally, Privately
Yandax Translate API / Google Translate API are all convenient to use, but people are concerned about "Privacy" since user data must be send to the remote to do the translation work

NLLBTranslateServer 100% run on your device, zero tracking

## Easy to set up
Please place the binary alongside with your model folder, **"The File and Folder Name"** must be the same as the picture

In terminal
1. type `sudo chmod 777 path/to/NTS_darwin` to allow the executable to run and fetch nllb files
2. type `xattr -cr path/to/NTS_darwin` to eliminate warning from Apple Signature
3. type `./NTS_darwin` to start server

Everything is now ready 🌟

![](https://github.com/willweimike/NLLBTranslateServer/blob/main/assets/Demo.png)

## Endpoints provided by NLLBTranslateServer
- http://127.0.0.1:8080/ : accept GET request, return current server status
- http://127.0.0.1:8080/help : accept GET request, return help message (available languages for translation)
- http://127.0.0.1:8080/translate: accept POST request, please contain the fields within the following picture

![](https://github.com/willweimike/NLLBTranslateServer/blob/main/assets/Demo2.png)

## NLLB - No Language Left Behind
Great model to be used in translation task

## Where to get the models?
Please go to this [link](https://huggingface.co/mikeforai/NLLB-200-Models-Collections) and download, the things that you would need are prepared for you 😃.
