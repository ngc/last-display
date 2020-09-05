<br/>
<p align="center">
  <img src="webassets/lastdisplay.png" width="75%">

  <p align="center">
    The last display you'll ever need for your music player. 
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [License](#license)


<!-- ABOUT THE PROJECT -->
## About <img src="webassets/lastdisplay.png" width="15%" style="    position: relative;top: 3px;" alt="last display">

The most inconsistent thing across music players is how the album art is displayed. last.display takes advantage of last.fm's API to quickly get information about what music the user is currently playing, or what music they listen to in general. 

![](https://imgur.com/F5gQgLS.png)

Last.display is also 100% customizable. It comes with a premade template called `template.html` but the user is encouraged to change it and style it to their liking. Information is passed into the template through format strings. 

![](https://i.imgur.com/mg1YdCJ.png)

Since to last.display is powered by Chromium, it is fully responsive and can be displayed in any form you'd like. Although, it is originally made to work best with tiling window managers such as i3.

![](https://imgur.com/iCJYg60.png)

![](https://i.imgur.com/lEXafdy.png)

<!-- GETTING STARTED -->
## Getting Started

To get a local build up and running follow these steps.

### Prerequisites

* Python3.8
* Git
* chromium-browser
* [A last.fm account](https://secure.last.fm/login?next=/api/account/create)
  * [last.fm API key](https://www.last.fm/api/account/create)

To install the software requirements on Ubuntu or Debian, run this command.
```sh
sudo apt install python3.8 git chromium-browser python3-pip
```

### Installation
 
1. Clone the repo
```sh
git clone https://github.com/thaniel-c/last-display.git
cd last-display/
```
2. Install requirements
```sh
pip3 install -r requirements.txt 
```
3. Install API Key 
```sh
chmod +x install.sh && ./install.sh
```

<!-- USAGE EXAMPLES -->
## Usage

To run last.display, execute the following commands.
```sh
chmod +x run.sh
./run.sh USERNAME
```
If everything was correctly installed you should see a small window popup with the most recent track you played showing.

There's a chance the server didn't correctly run because there is already a process active on port `8099`. To fix this problem, simply kill the process on that port or change the port in line 15 of `main.py` to something else.

## Debugging

There's a good chance you'll want to do some debugging when making your own changes to last.display. To see stdout, run the following commands to start last.display along with chromium-browser. 
```sh
python3.8 main.py --user USERNAME
chromium-browser --app="http://0.0.0.0:8099/__display__.html"
``` 
---
<!-- LICENSE -->
## License

Distributed under the GNU GPL. See `LICENSE` for more information.