--
-- Database: `yubikeys`
--

-- --------------------------------------------------------

--
-- Table `apikeys`
--

CREATE TABLE IF NOT EXISTS apikeys (
  nickname varchar(64) default NULL,
  secret varchar(28) default NULL,
  id SERIAL PRIMARY KEY
);

-- --------------------------------------------------------

--
-- Table `oathtokens`
--

CREATE TABLE IF NOT EXISTS oathtokens (
  nickname varchar(64) NOT NULL UNIQUE,
  publicname varchar(12) NOT NULL UNIQUE,
  created varchar(24) NOT NULL,
  secret varchar(40) NOT NULL,
  active smallint default '1',
  counter integer NOT NULL default '1'
);

-- --------------------------------------------------------

--
-- Table `yubikeys`
--

CREATE TABLE IF NOT EXISTS yubikeys (
  nickname varchar(64) NOT NULL UNIQUE,
  publicname varchar(16) NOT NULL UNIQUE,
  created varchar(24) NOT NULL,
  internalname varchar(12) NOT NULL,
  aeskey varchar(32) NOT NULL,
  active smallint default '1',
  counter integer NOT NULL default '1',
  time integer NOT NULL default '1'
);

-- --------------------------------------------------------

--
-- Table `yubikeys_audit`
--

CREATE TABLE IF NOT EXISTS yubikeys_audit (
  id SERIAL PRIMARY KEY,
  publicname varchar(16) NOT NULL,
  actiontimestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  result varchar(24)
);

