# NLLBTranslateServer - Translate Locally

## Locally, Privately
Yandax Translate API / Google Translate API are all convenient to use, but people are concerned about "Privacy" since user data must be send to the remote to do the translation work

## Easy to set up
Please place the binary alongside with your model folder, **"The File and Folder Name"** must be the same as the picture 

In terminal, type `sudo chmod u+x NTS_darwin` to allow the executable to run, and then type `./NTS_darwin`. 

Everything is now ready 🌟

![](https://github.com/willweimike/NLLBTranslateServer/blob/main/assets/Demo.png)

## Endpoints provided by NLLBTranslateServer
- http://127.0.0.1:8080/ : Root Endpoint which accepts GET request, return current server status
- http://127.0.0.1:8080/help : Endpoint which accepts GET request, return help message (available languages for translation)
- http://127.0.0.1:8080//translate: Endpoint which accepts POST request, please contain the fields within the following picture
<img width="255" alt="image" src="https://github.com/user-attachments/assets/8ff2e29d-19d0-4cbd-b2dd-f4001543d768" />

## NLLB - No Language Left Behind
A good model to be used in translation task

## Where to get the models?
Please go to this [link](https://huggingface.co/mikeforai/NLLB-200-Models-Collections) and download, the things that you would need are prepared for you 😃.

## Compile the binary on your own? Packages are ready right here!
**just download "python-3.11.5-macos11.pkg", and `pip install [wheels within "nllb_server_use_packages"]`!!**
