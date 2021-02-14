# Auto idUFF Reports
> This repository aims to apply some automation to repetitively work that I do at Universidade Federal Fluminense.

During the pandemic caused by SARS-COV19, Universidade Federal Fluminense had started to give remote classes for its students. Some professors like to use Moodle LMS, but it is not integrated with idUFF database. On account of this all data transfer between both databases are made manually and pass by three distinct departments:
* The first one for register on idUFF database the subjects that students have being subscribed;
* The second one for generate reports from idUFF, prepare data applying filters, deleting valueless information,  splitting data by class and finally send the processed reports by e-mail for the third;
* The third one for process all data inclusion from reports at Moodle database.
Those three departments are independents from each other. Thus, I don't know the level of automation that the first and third ones have, but all work being developed at the second departament today is manual and this repository is to try to solve this problem.

## Development setup

If you want to help to develop this project, you will need:
* [Python 3.9.1][python-url];
* [Firefox Browser][firefox-url];
* Package selenium for Python;
```sh
pip install selenium
```
* [geckodriver][geckodriver-url]

It is important to note that _geckodriver_ must be added to path of system. To add geckodriver to path, if you are using a Debian-based Linux System, you can do it exporting the path editing _.bashrc_ file, or just moving the driver opening terminal on the same directory that geckodriver is and executing the command below:

```sh
sudo mv geckodriver /usr/local/bin
```

## Release History

* 0.0.1
    * Work in progress

## Meta

Jefferson Peralva

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/j-peralva/auto_iduff_reports](https://github.com/j-peralva/auto_iduff_reports)

## Contributing

1. Fork it (<https://github.com/j-peralva/auto_iduff_reports/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[geckodriver-url]:https://github.com/mozilla/geckodriver/releases/tag/v0.29.0
[python-url]:https://www.python.org/
[firefox-url]:https://www.mozilla.org/pt-BR/firefox/new/