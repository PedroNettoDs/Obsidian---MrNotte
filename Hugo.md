# Hugo
https://sal.as/post/install-hugo-on-wsl/

Montador e instalador do programas.

```bash
wget https://github.com/gohugoio/hugo/releases/download/v0.54.0/hugo_0.54.0_Linux-64bit.deb
```
> `wget` stands for “web get”. It is a command-line utility which downloads files over a network.

## Extract package
Now we will extract the package, make sure you type `sudo`.
```bash
sudo dpkg -i hugo_0.54.0_Linux-64bit.deb
```