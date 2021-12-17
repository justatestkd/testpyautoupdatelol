import requests
lastverlink = "https://raw.githubusercontent.com/justatestkd/testpyautoupdatelol/main/pkg/ver"
pkglink = "https://raw.githubusercontent.com/justatestkd/testpyautoupdatelol/main/pkg/main.py"

print("Package updater!")
print("Information: this package installing to the project folder.")
print("Last version: "+requests.get(lastverlink).text)
input("Press any key to start installing! ")
f = open("packageautoupdate.py","w")
f.write(requests.get(pkglink).text)
print("Successfully installed a package to this folder!")
