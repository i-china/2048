### composer的安装和使用
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
### Laravel 安装
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
php artisan --version | php artisan -V
php artisan down | up

// 设置时区
在 app.php 中
'timezone' => 'Asia/Shanghai';
'timezone' => 'PRC';

初始化完成后，修改.env配置文件，配置数据库等
exec: php artisan migrate:install	// 检测数据是否迁移成功

























