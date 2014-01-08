/*
 * monit-remote sqlite database schema
 * 
 * $ sqlite3 monit-remote.db < monit-remote.sqlite
 *
 */

CREATE TABLE hosts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  monit_httpd_url TEXT NOT NULL,
  monit_httpd_username TEXT NOT NULL DEFAULT 'admin',
  monit_httpd_password TEXT NOT NULL DEFAULT 'monit',
  monit_config_directory TEXT NOT NULL DEFAULT '/etc/monit.d/',
  monit_binary_path TEXT NOT NULL DEFAULT '/bin/monit',
  ssh_ip TEXT NOT NULL DEFAULT 'localhost',
  ssh_username TEXT NOT NULL DEFAULT 'root',
  ssh_private_key TEXT NULL
);
CREATE UNIQUE INDEX monit_httpd_url_UNIQUE on hosts (monit_httpd_url);
INSERT INTO hosts (monit_httpd_url) VALUES('http://localhost:2812');
INSERT INTO hosts (monit_httpd_url) VALUES('http://localhost:2813');
