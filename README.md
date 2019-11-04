[![Follow on Twitter](https://img.shields.io/twitter/follow/johandu0.svg?logo=twitter)](https://twitter.com/johandu0)


![Subdomains](images/arescode.png)

## About Arescode

Create responsive code directory structure based on liveURLs. Return redirect and error information.

## Installation

```
git clone https://github.com/johandu1997/Arescode.git
```

## Dependencies

* Installation on Linux

```
sudo pip install -r requirements.txt
```

## Setup

* Installation on Linux
```
sudo ./build.sh
```
## Usage

```
arescode -f <urls_file> -o <results_directory>
```

Short Form    | Long Form     | Description
------------- | ------------- |-------------
-f            | --file        | Enter the filename contain URLs
-o            | --output      | Return the resulting directory name
-h            | --help        | Show the help message and exit

## Examples

1. Make a search of responsive code and return responsive code directory structure
  
```
arescode -f live_https.txt -o result_https
```

```
arescode -f live_http.txt -o result_http
```

## Issues and requests

If you have a problem or a feature request, open an [issue](https://github.com/johandu1997/Arescode/issues).

## License

Domains is licensed under the GNU GPL license. take a look at the [LICENSE](https://github.com/johandu1997/Arescode/blob/master/LICENSE) for more information.

## Thanks

* Special Thanks to infosec community.

## Version

**Current version is 1.0**
