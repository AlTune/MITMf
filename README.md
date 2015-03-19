MITMf V0.9.5
============

Framework for Man-In-The-Middle attacks

Dev updates at http://sign0f4.blogspot.it

This tool is based on [sergio-proxy](https://github.com/supernothing/sergio-proxy) and is an attempt to revive and update the project.

**Before submitting issues please read the appropriate [section](#submitting-issues).**

Dependency change!
===================
As of v0.9.5 DNS tampering support needs NetfilterQueue v0.6 which is currently a fork, so it *cannot* be installed via pip or easy_install.

Download it from here https://github.com/fqrouter/python-netfilterqueue and manually install it.

Availible plugins
=================
- Responder - LLMNR, NBT-NS and MDNS poisoner
- SSLstrip+ - Partially bypass HSTS
- Spoof - Redirect traffic using ARP Spoofing, ICMP Redirects or DHCP Spoofing and modify DNS queries
- Sniffer - Sniffs for various protocol login and auth attempts
- BeEFAutorun - Autoruns BeEF modules based on clients OS or browser type
- AppCachePoison - Perform app cache poison attacks 
- SessionHijacking - Performs session hijacking attacks, and stores cookies in a firefox profile
- BrowserProfiler - Attempts to enumerate all browser plugins of connected clients
- CacheKill - Kills page caching by modifying headers
- FilePwn - Backdoor executables being sent over http using bdfactory
- Inject - Inject arbitrary content into HTML content
- JavaPwn - Performs drive-by attacks on clients with out-of-date java browser plugins
- jskeylogger - Injects a javascript keylogger into clients webpages
- Replace - Replace arbitary content in HTML content
- SMBAuth - Evoke SMB challenge-response auth attempts
- Upsidedownternet - Flips images 180 degrees

Changelog
=========

- Addition of the Sniffer plugin which integrates [Net-Creds](https://github.com/DanMcInerney/net-creds) currently supported protocols are:
  FTP, IRC, POP, IMAP, Telnet, SMTP, SNMP (community strings), NTLMv1/v2 (all supported protocols like HTTP, SMB, LDAP etc..) and Kerberos

- Integrated [Responder](https://github.com/SpiderLabs/Responder) to poison LLMNR, NBT-NS and MDNS, and act as a WPAD rogue server.

- Integrated [SSLstrip+](https://github.com/LeonardoNve/sslstrip2) by Leonardo Nve to partially bypass HSTS as demonstrated at BlackHat Asia 2014 

- Addition of the SessionHijacking plugin, which uses code from [FireLamb](https://github.com/sensepost/mana/tree/master/firelamb) to store cookies in a Firefox profile 

- Spoof plugin now supports ICMP, ARP and DHCP spoofing along with DNS tampering

- Spoof plugin can now exploit the 'ShellShock' bug when DHCP spoofing! 

- Usage of third party tools has been completely removed (e.g. ettercap)

- FilePwn plugin re-written to backdoor executables and zip files on the fly by using [the-backdoor-factory](https://github.com/secretsquirrel/the-backdoor-factory) and code from [BDFProxy](https://github.com/secretsquirrel/BDFProxy)

- Added [msfrpc.py](https://github.com/byt3bl33d3r/msfrpc/blob/master/python-msfrpc/msfrpc.py) for interfacing with Metasploits rpc server

- Added [beefapi.py](https://github.com/byt3bl33d3r/beefapi) for interfacing with BeEF's RESTfulAPI

- Addition of the app-cache poisoning attack by [Krzysztof Kotowicz](https://github.com/koto/sslstrip) (blogpost explaining the attack here http://blog.kotowicz.net/2010/12/squid-imposter-phishing-websites.html)

Submitting Issues
=================
If you have *questions* regarding the framework please email me at byt3bl33d3r@gmail.com

If you find a *bug* please open an issue and include at least the following in the description:

- Full command string you used
- OS your using

Also remember: Github markdown is your friend!

How to install on Kali
======================

```apt-get install mitmf```
