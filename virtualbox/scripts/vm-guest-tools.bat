# Install the Oracle certificate first
#certutil -addstore -f "TrustedPublisher" E:\cert\oracle-vbox.cer
cd "E:\cert"
VBoxCertUtil.exe add-trusted-publisher vbox*.cer --root vbox*.cer

Start-Process -FilePath "E:\VBoxWindowsAdditions.exe" -ArgumentList "/S" -Wait
