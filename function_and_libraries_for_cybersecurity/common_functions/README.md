## Sub process

___

* `.run()`: Main way to run commands since Python 3.5
* `.call()`: Returns the `returncode` attribute
* `check_call()`: Returns the `returncode` if 0, otherwise raises `CalledProcessError`
* `.Popen()`: Flexible to handle less common cases