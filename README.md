# NLLBTranslateServer - Translate Locally

## Locally, Privately
Yandax Translate API / Google Translate API are all convenient to use, but people are concerned about "Privacy" since user data must be send to the remote to do the translation work

NLLBTranslateServer 100% run on your device, zero tracking

## Easy to set up
Please place the binary alongside with your model folder, **"The File and Folder Name"** must be the same as the picture 

In terminal, type `sudo chmod 777 NTS_darwin` to allow the executable to run and fetch nllb files, and then type `./NTS_darwin`. 

Everything is now ready 🌟

![](https://github.com/willweimike/NLLBTranslateServer/blob/main/assets/Demo.png)

## Endpoints provided by NLLBTranslateServer
- http://127.0.0.1:8080/ : accept GET request, return current server status
- http://127.0.0.1:8080/help : accept GET request, return help message (available languages for translation)
- http://127.0.0.1:8080/translate: accept POST request, please contain the fields within the following picture

![](https://github.com/willweimike/NLLBTranslateServer/blob/main/assets/Demo2.png)

## NLLB - No Language Left Behind
A good model to be used in translation task

## Where to get the models?
Please go to this [link](https://huggingface.co/mikeforai/NLLB-200-Models-Collections) and download, the things that you would need are prepared for you 😃.

## Run on your own? Packages are ready right here!
**Sometimes the binary doesn't work (Not sure why).**
1. Download "NLLBTranslateServer.zip" from the release section
2. `pip install [wheels within "nllb_server_use_packages"]`
3. Put model folder (see above) alongside with app.py, run `python app.py`
4. You are good to go!
