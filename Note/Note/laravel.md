1. composer:
	>> php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
	>> php composer-setup.php
	>> mv composer.phar /usr/local/bin/composer
	>> composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/
	>> 取消配置： composer config -g --unset repos.packagist
	>> composer install
	>> composer search xxx
	>> composer selfupdate
	>> composer show | composer show xxx 
	>> curl -sS https://getcomposer.org/installer | php 
	>> mv composer.phar /usr/local/bin/composer
	>> composer require xxx/xxx
	>> composer remove xxx/xxx | xxx 
	>>  composer.json 
			{
				"require": {
					"xxx/xxx":"1.0.*@beta",
					"xxx/xxx":"@dev"
				}
			}

2. Laravel  
Laravel install Tool:	composer global require "laravel/install"
添加laravel 到系统环境变量： 
		export PATH=“root/.config/composer/vendor/bin:$PATH
		$HOME/.composer/vendor/bin  主要让系统找到laravel的可执行文件
		laravel new xxx
composer install laravel:
		composer create-project --prefer-dist laravel/laravel xxx "5.5.*"

Web 服务器配置：
Nginx:	
		location / {
			try_files $uri $uri/ /index.php?$query_string;
		}
具体看微信图片收藏中的配置信息

php artisan serve
php artisan --version
php artisan down | up

