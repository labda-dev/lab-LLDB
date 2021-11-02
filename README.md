# lab-LLDB
*__LLDB util script for iOS/MacOS__*
- _v1.0.0_
- _Tested on Python 3.8.2._

## Installation
### Quick Installation
```sh
$ git clone https://github.com/labda-dev/lab-LLDB.git ~/.lab_lldb
$ echo "command script import ~/.lab_lldb/lab_LLDB.py" >> ~/.lldbinit
```
### Manual Import
```sh
$ git clone https://github.com/labda-dev/lab-LLDB.git ~/.lab_lldb
$ lldb
(lldb) command script import ~/.lab_lldb/lab_LLDB.py
```

## Command
### __bbb__ - set Breakpoint By Base address
Set breakpoint using base address (0x100000000) or binary offset.
Automatic calculate address/offset to virtual memory. (ASLR)
```sh
(lldb) bbb hex_address
```
#### example
```sh
(lldb) bbb 0x1000A29F4
(lldb) bbb 0xA29F4
(lldb) bbb a29f4
```
> (lldb) image list
> [0] E6B1E95D-FDD9-3978-9BB9-0481240AFF50 0x0000000102340000  /private/var/containers/Bundle/Application/344548E9-C58F-41B2-9223-B23DAF5F09B1/Sample.app/Sample (0x0000000102340000)
> ... 
> (lldb) b 0x1023E29F4

vs

> (lldb) bbb 0xa29f4