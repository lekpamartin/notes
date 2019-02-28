# GPG

### Create key
```bash
gpg --gen-key
```
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
```bash
dd if=/dev/sda of=/dev/zero
```

### List key
```bash
gpg --list-keys
```
 
### Export key
```bash
gpg --export -a <key> > RPM-GPG-KEY-<key>
gpg
 
### Default path
```bash
/etc/pki/rpm-gpg/
```
 
### Import key into the RPM database
```bash
sudo rpm --import RPM-GPG-KEY-<key>
```
 
### Check key into the RPM database
```bash
rpm -q gpg-pubkey --qf '%{NAME}-%{VERSION}-%{RELEASE}\t%{SUMMARY}\n'
```
