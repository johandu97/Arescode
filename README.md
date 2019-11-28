[![Follow on Twitter](https://img.shields.io/twitter/follow/johandu0.svg?logo=twitter)](https://twitter.com/johandu0) <br/>
[![License](https://img.shields.io/badge/license-MIT-red.svg)](https://github.com/johandu1997/Arescode/blob/master/LICENSE)  [![Version](https://img.shields.io/badge/Release-1.1.0-blue.svg?maxAge=259200)]()  [![Build](https://img.shields.io/badge/Supported_OS-Linux-yellow.svg)]()  [![Build](https://img.shields.io/badge/Supported_WSL-Windows-blue.svg)]() [![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/johandu1997/Arescode/issues)  [![Youtube](https://img.shields.io/badge/Youtube-Demo-red.svg)](https://www.youtube.com/watch?v=5btrMPHi8Y8&t=6s)


![Arescode](images/arescode.png)

## About Arescode

Create responsive code directory structure based on living URLs. Return redirect and error information.

## Installation

```
git clone https://github.com/johandu1997/Arescode.git
```

## Dependencies

* Installation on Linux

```
pip install -r requirements.txt
```

## Setup

* Installation on Linux
```
./build.sh
```
## Usage

```
arescode -f <subdomains_file>
```

Short Form    | Long Form     | Description
------------- | ------------- |-------------
-f            | --file        | Enter the filename contain URLs
-t            | --thread      | Number of threads
-h            | --help        | Show the help message and exit

## Examples

1. Make a search of living subdomains and return responsive code directory structure
  
```
arescode -f sony.com-final.txt
```

2. Make a search of living subdomains and return responsive code directory structure with threading
  
```
arescode -f sony.com-final.txt -t 50
```

## Issues and requests

If you have a problem or a feature request, open an [issue](https://github.com/johandu1997/Arescode/issues).

## License

Domains is licensed under the GNU GPL license. take a look at the [LICENSE](https://github.com/johandu1997/Arescode/blob/master/LICENSE) for more information.

## Thanks

* Special Thanks to infosec community.

## Version

**Current version is 1.0**

## Donate me

If you want the tool to keep growing, you can donate to me to keep me motivated to develop more new features in the future.

[![Donate with PayPal](images/paypal-donate-button.png)](https://www.paypal.me/johandu97)
