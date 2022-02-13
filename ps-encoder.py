import sys, base64

if len(sys.argv) < 3 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
  print("Usage: " + sys.argv[0] + " [OPTION]... [FILE]")
  print("PowerShell Base64 encode or decode FILE, or standard input, to standard output.")
  print("\nWith no FILE provided as the second argument, the second argument will be encoded or decoded\n")
  print("  -d, --decode".ljust(20, " ") + "decode the powershell FILE or argument.")
  print("  -e, --encode".ljust(20, " ") + "encode the powershell FILE or argument.")
  print("  -h, --help".ljust(20, " ") + "display this help and exit.")
  print("\n If you want to ouput to a file use the stdout > operator.\n")
  sys.exit()

try:
  f = open(sys.argv[2], "r")
  ps = f.read()
  f.close()
except:
  ps = sys.argv[2]

if sys.argv[1] == "-e" or sys.argv[1] == "--encode":
  bytes = ps.encode('utf-16-le')
  b64 = base64.b64encode(bytes)
  print("powershell.exe -exec bypass -enc " + b64.decode())

elif sys.argv[1] == "-d" or sys.argv[1] == "--decode":
  b64 = base64.b64decode(ps)
  script = b64.decode('utf-16-le')
  print(script)
