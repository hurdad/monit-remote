/*
 * monit-remote sqlite database schema
 * 
 * $ sqlite3 monit-remote.db < monit-remote.sqlite
 *
 */

CREATE TABLE monit_hosts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  monit_httpd_url TEXT NOT NULL,
  monit_httpd_username TEXT NOT NULL DEFAULT 'admin',
  monit_httpd_password TEXT NOT NULL DEFAULT 'monit',
  monit_httpd_timeout_ms INT NOT NULL DEFAULT '500',
  monit_config_directory TEXT NOT NULL DEFAULT '/etc/monit.d/',
  monit_binary_path TEXT NOT NULL DEFAULT '/bin/monit',
  ssh_ip TEXT NOT NULL DEFAULT 'localhost',
  ssh_username TEXT NOT NULL DEFAULT 'root',
  ssh_private_key TEXT NULL,
  is_enabled TINYINT(1) NOT NULL DEFAULT 1
);
CREATE UNIQUE INDEX monit_httpd_url_UNIQUE on monit_hosts (monit_httpd_url);
INSERT INTO monit_hosts (monit_httpd_url) VALUES('http://localhost:2812');
